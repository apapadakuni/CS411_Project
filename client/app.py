import flask
from flask import Flask, render_template, request, redirect, url_for, jsonify
from API_request import *
from flaskext.mysql import MySQL
import flask_login

mysql = MySQL()
app = Flask(__name__)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'cs460iscool' #INSERT YOUR MYSQL PASSWORD
app.config['MYSQL_DATABASE_DB'] = 'cs411_db'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

conn = mysql.connect()
cursor = conn.cursor()

@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'GET': #if request is get (user navigated to the URL)
        return render_template('register.html')
    else:
        email=request.form.get('email')
        password=request.form.get('password')
        # age=request.form.get('age')
        # height = request.form.get('height')
        # weight= request.form.get('weight')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO User_Accounts (email, password) VALUES ('{0}', '{1}')".format(email, password))
        conn.commit()
        return render_template('index.html', message="Successfully registered! Welcome :)")

#main page of website
#default method is only GET
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET': #if request is get (user navigated to the URL)
        return render_template('index.html')
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

#search page
@app.route('/result/', methods=['GET','POST'])
def result():
    return render_template('result.html')

if __name__ == "__main__":
	app.run(port=5000, debug=True)
