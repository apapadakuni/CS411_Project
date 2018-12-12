from __future__ import print_function # In python 2.7
import flask
from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask import Flask, redirect, url_for, session
from flask_oauth import OAuth
import ast
import sys
from API_request import *
import datetime
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from pymongo import MongoClient
from pprint import pprint
import subprocess
import os
import time
import signal
import atexit
# from db_fcns import *     I tried to make it modular, but i couldnt for some reason and it is 6:25am so i m jsut gonna put all DB stuff here



def db_add_user(email, name):
    try:
        db.insert({
            "email": email,
            "name": name
        })
        return 0
    except: return -1

def db_check_user(email):
    user = db.find_one({
        'email':email
        })
    if user == None:
        return False
    else:
        return True

def db_update_personal_info(email, height, weight, sex, age):
    #assuming they are already registered as a user
    try:
        db.update({
            'email':email
            },{'$set':
            {
            'height': height,
            'weight': weight,
            'sex': sex,
            'age': age,
            }}, multi = False)
        return 0
    except:
        return -1

def db_update_calendar(email, cal):
    #assuming they are already registered as a user
    for i in cal:
        db.update({
            "email": email
            },
            {'$push':{
                "calendar_events": i
                    }
            }
        )

def db_update_schedule(email, sched):
    for i in sched:
        db.update({
            "email":email
            },
            {'$push':{
                "schedule": i
                    }
            }
        )


#create connection to db
pro = subprocess.Popen(["mongod"], stdout = subprocess.PIPE,shell=True, preexec_fn=os.setsid)
time.sleep(1)
client_DB = MongoClient('mongodb://localhost:27017')
collection = client_DB['CS411_Project']
db = collection.users


# You must configure these 3 values from Google APIs console
# https://code.google.com/apis/console
GOOGLE_CLIENT_ID = ''
GOOGLE_CLIENT_SECRET = ''
REDIRECT_URI = '/oauth2callback'  # one of the Redirect URIs from Google APIs console
# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
user_schedule = []
SECRET_KEY = 'development key'
DEBUG = True

app = Flask(__name__)
app.debug = DEBUG
app.secret_key = SECRET_KEY
oauth = OAuth()
user_email = ''
user_first_name = ''
google = oauth.remote_app('google',
                          base_url='https://www.google.com/accounts/',
                          authorize_url='https://accounts.google.com/o/oauth2/auth',
                          request_token_url=None,
                          request_token_params={'scope': 'https://www.googleapis.com/auth/userinfo.email',
                                                'response_type': 'code'},
                          access_token_url='https://accounts.google.com/o/oauth2/token',
                          access_token_method='POST',
                          access_token_params={'grant_type': 'authorization_code'},
                          consumer_key=GOOGLE_CLIENT_ID,
                          consumer_secret=GOOGLE_CLIENT_SECRET)

@app.route('/', methods=['GET', 'POST'])
def index():
        return render_template('welcome.html')

@app.route('/sign-in', methods=['GET', 'POST'])
def sign_in():
    #Displayed data in the end
    access_token = session.get('access_token')
    if access_token is None:
        return redirect(url_for('login'))

    access_token = access_token[0]
    from urllib2 import Request, urlopen, URLError

    headers = {'Authorization': 'OAuth '+access_token}
    req = Request('https://www.googleapis.com/oauth2/v1/userinfo',
                  None, headers)
    try:
        res = urlopen(req)

    except URLError, e:
        if e.code == 401:
            # Unauthorized - bad token
            session.pop('access_token', None)
            return redirect(url_for('login'))
        return res.read()

    a = res.read()
    #Need to capitalize True or Flase in order to convert to dictionary


    user_info_str = a.replace('true', 'True')
    user_info_str = user_info_str.replace('false', 'False')
    user_info = ast.literal_eval(user_info_str)
    global user_email
    user_email = user_info['email']
    try:
        user_first_name = user_info['given_name']
    except:
        at_char_index = user_email.index('@')
        user_first_name = user_email[:at_char_index]

    user_exists = db_check_user(user_email)
    if user_exists == True:
        return redirect(url_for('profile'))
    else:
        res = db_add_user(user_email, user_first_name)
        if (res == -1):
            print("Failed to add user to DB", file = sys.stderr)
            return redirect(url_for('welcome'))
        else:
            return redirect(url_for('ask_info'))

@app.route('/profile')
def profile():
    user = db.find_one({
            'email':user_email
        })
    name=user['name']
    age=user['age']
    height=user['height']
    weight=user['weight']
    sex=user['sex']
    return render_template('profile.html', name=name,age=age,height=height,weight=weight,sex=sex)


@app.route('/login')
def login():
    print('at login', file=sys.stderr)
    callback=url_for('authorized', _external=True)
    return google.authorize(callback=callback)

@app.route(REDIRECT_URI)
@google.authorized_handler
def authorized(resp):
    print('at authorized', file=sys.stderr)
    access_token = resp['access_token']
    session['access_token'] = access_token, ''
    return redirect(url_for('sign_in'))


@google.tokengetter
def get_access_token():
    print('at get_access_token', file=sys.stderr)
    return session.get('access_token')


@app.route('/ask_info', methods = ['GET', 'POST'])
def ask_info():
    print(user_email, file = sys.stderr)
    if request.method == 'POST':
        print('in ask_info:POST', file = sys.stderr)
        user_age = str(request.form['user_age'])
        user_height = str(request.form['user_height'])
        user_weight = str(request.form['user_weight'])
        user_sex = str(request.form['user_sex'])
        res = db_update_personal_info(user_email, user_height, user_weight, user_sex, user_age)
        return redirect(url_for('select_calendar_options'))
    else:
        return render_template('ask_info.html')


@app.route('/select_calendar_options', )
def select_calendar_options():
    print('at select_calendar_options', file = sys.stderr)
    user = db.find_one({
            'email':user_email
        })
    name=user['name']
    return render_template('select_calendar_options.html', name=name)


def get_googlecalendar_events():
    os.system('rm token.json')
    time.sleep(0.3)
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
    	creds = tools.run_flow(flow, store)
    service = build('calendar', 'v3', http=creds.authorize(Http()))

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    # print('Getting the upcoming 10 events')
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=75, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])
    # print (events)

    first_time = 1
    if not events:
        print('No upcoming events found.')
    event_by_day = []
    for event in events:  #go through 75 events
    #Events are given one after the other starting from the current time we made the Request

        #getting and parsing info
        start = event['start'].get('dateTime', event['start'].get('date'))
        start_date = start[0:10]
        start_time = start[11:16]
        end = event['end'].get('dateTime', event['end'].get('date'))
        end_date = end[0:10]
        end_time = end[11:16]
        event_name = event['summary']
        # event_start_day = datetime.datetime.strptime(start_date, '%Y-%m-%d').strftime('%a')

        #Not all events have locations
        try:
            event_location = event['location']
        except:
            event_location = ''

        if (first_time == 1):
            first_day = int(start_date[8:10])
            last_day = first_day + 6
            if (last_day > 31):         #assuming all months are 30 days long. This is not an issue, since if we have crossed another month,
                                        #we just add more events of repeated days
                last_day = last_day - 31
            first_time = 0
        else:
            if (last_day < int(start_date[8:10])):
                return event_by_day


        #creating event dictionary
        parsed_event = {
            "name" : event_name,
            "day" : (start_date),
            "start_hour" : (start_time.split(':')[0]),
            "start_min" : (start_time.split(':')[1]),
            "end_hour" : (end_time.split(':')[0]),
            "end_min" : (end_time.split(':')[1]),
            "location" : event_location
        }
        event_by_day.append(parsed_event)      #adding event to specific day



@app.route('/google_calendar', methods=['GET','POST'])
def google_calendar():
    user_google_calendar_events = get_googlecalendar_events()
    print(user_google_calendar_events)
    new_events = []
    for a in user_google_calendar_events:
        new_event = {
            "name" :a["name"],
            "start_time" : a["start_hour"] + ":" + a["start_min"],
            "end_time" : a["end_hour"] + ":" + a["end_min"],
            "location" : a["location"],
            "date": a["day"]
        }
        new_events.append(new_event)
    db_update_calendar(user_email, new_events)

    print(a, file = sys.stderr)
    # with app.app_context():
    #NEED TO: events on calendar can't be deleted or modified. I feel like we should fix that, so that if a user wants to change the location or something
    return render_template('calendar.html', calendar_events=new_events)

@app.route('/get_calendar_data', methods = ['GET','POST'])
def get_calendar_data():
    #NEED TO: events from google calendar need to be sent here as well. I tried to do an asynchronous POST
    #request here through the for loop with the google calendar events but failed. Feel like it will be easy for u
    #remember to add them in the same format as the actual calendar events
    if request.method == 'POST':
        c = request.json
        print(c,file = sys.stderr)
        new_event = {
            'name' : c['name'],
            'start_time' : c['start_time'][11:16],
            'end_time': c['end_time'][11:16],
            'location': c['location'],
            'date': c['start_time'][:10]
        }
        global user_schedule
        user_schedule.append(new_event)
    # a = get_googlecalendar_events()
    # # user_schedule.append(a)
    # print("TEST")
    # print(user_schedule, file = sys.stderr)
    # return "yeet on them"
    else:
        try:
            all_user_info = db.find_one({
            'email':user_email
            })
            events = all_user_info['calendar_events']
        except:
            events = []
        return render_template('calendar.html', calendar_events = events)



@app.route('/make_schedule', methods = ['GET','POST'])
def make_schedule():
    # print(user_schedule, file = sys.stderr)
    global user_schedule
    db_update_calendar(user_email, user_schedule)
    # global user_schedule
    user_schedule = []
    all_user_info = db.find_one({
        'email':user_email
        })
    res = can_I_walk_all_events(all_user_info)          #FROM API REQUEST.py
    print(res, file = sys.stderr)
    db_update_schedule(user_email, res)
    return render_template('result.html', results=res)



#NEED TO: this part is for me. I still need to actually call the API and create a data structure based on that
#Then that data structure can be passed to the front end for a nice display of how to go where
#I can also make it so that a pdf or something is downloadable


#--------------------------------------------------------------
#OLD CODE, NOT NEEDED
@app.route('/add_events', methods=['GET', 'POST'])
def add_events():
        return render_template('calendar.html')




if __name__ == "__main__":
	app.run(port=5000, debug=True)

#LINE UNDERNEATH: kills connection to mongodb, add when USER exits from app
#os.killpg(os.getpgid(pro.pid), signal.SIGTERM)  # Send the signal to all the process groups

# ANDREAS: OS command isn't working
# def exit_handler():
#     os.killpg(os.getpgid(pro.pid), signal.SIGTERM)
#     print("bye")
# atexit.register(exit_handler)
