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

# You must configure these 3 values from Google APIs console
# https://code.google.com/apis/console
GOOGLE_CLIENT_ID = '279331729673-1187c5t7eja4tao5lmcikbnf443fj040.apps.googleusercontent.com'
GOOGLE_CLIENT_SECRET = 'aNuew-vKzjQxUz1pZLLigQ-w'
REDIRECT_URI = '/oauth2callback'  # one of the Redirect URIs from Google APIs console
# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'

SECRET_KEY = 'development key'
DEBUG = True

app = Flask(__name__)
app.debug = DEBUG
app.secret_key = SECRET_KEY
oauth = OAuth()
email = ''
first_name = ''
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
        #Need to capitalize True or Flase in order to conert to dictionary


        user_info_str = a.replace('true', 'True')
        user_info_str = user_info_str.replace('false', 'False')
        user_info = ast.literal_eval(user_info_str)
        user_email = user_info['email']
        user_first_name = user_info['given_name']

        # #Printing just for checking
        print(user_email, file = sys.stderr)
        print(user_first_name, file = sys.stderr)
        return res.read()


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
    return redirect(url_for('select_calendar_options'))


@google.tokengetter
def get_access_token():
    print('at get_access_token', file=sys.stderr)
    return session.get('access_token')

@app.route('/select_calendar_options')
def select_calendar_options():
    return render_template('select_calendar_options.html')


def get_googlecalendar_events():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
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
    # event_by_day['Mon'] = []
    # event_by_day['Tue'] = []
    # event_by_day['Wed'] = []
    # event_by_day['Thu'] = []
    # event_by_day['Fri'] = []
    # event_by_day['Sat'] = []
    # event_by_day['Sun'] = []
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
            "day" : start_date.split('-')[2],
            "start_hour" : start_time.split(':')[0],
            "start_min" : start_time.split(':')[1],
            "end_hour" : end_time.split(':')[0],
            "end_min" : end_time.split(':')[1],
            "location" : event_location
        }


        event_by_day.append(parsed_event)      #adding event to specific day


@app.route('/google_calendar', methods=['GET','POST'])
def google_calendar():
    a = get_googlecalendar_events()
    # with app.app_context():
    return render_template('calendar.html', calendar_events=a)


@app.route('/add_events', methods=['GET', 'POST'])
def add_events():
    if request.method == 'GET': #if request is get (user navigated to the URL)
        return render_template('calendar.html')
    else:
        event1_name = request.form['event1_name']
        event1_start = request.form['event1_start']
        event1_end =  request.form['event1_end']
        location1 =  request.form['location1']
        event2_name = request.form['event2_name']
        event2_start = request.form['event2_start']
        event2_end =  request.form['event2_end']
        location2 =  request.form['location2']
        event3_name = request.form['event3_name']
        event3_start = request.form['event3_start']
        event3_end =  request.form['event3_end']
        location3 =  request.form['location3']
        event4_name = request.form['event4_name']
        event4_start = request.form['event4_start']
        event4_end =  request.form['event4_end']
        location4 =  request.form['location4']

        event1 = {
            "name" : str(event1_name),
            "start": str(event1_start),
            "end" : str(event1_end),
            "location" : str(location1)
        }
        event2 = {
            "name" : str(event2_name),
            "start": str(event2_start),
            "end" : str(event2_end),
            "location" : str(location2)
        }
        event3 = {
            "name" : str(event3_name),
            "start": str(event3_start),
            "end" : str(event3_end),
            "location" : str(location3)
        }
        event4 = {
            "name" : str(event4_name),
            "start": str(event4_start),
            "end" : str(event4_end),
            "location" : str(location4)
        }
        results = [dict] * 3
        results[0] = can_I_walk_it(event1, event2)
        results[1] = can_I_walk_it(event2, event3)
        results[2] = can_I_walk_it(event3, event4)

        return render_template('result.html', event1 = event1, event2 = event2, event3= event3, event4 = event4, results = results)

# #search page
# @app.route('/result/', methods=['GET','POST'])
# def result():
#     return render_template('result.html')

if __name__ == "__main__":
	app.run(port=5000, debug=True)
