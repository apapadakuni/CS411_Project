'''
Author: Craig Einstein
File: search_app.py
Description: A simple web application that connects to the sakila database and implements a query execution feature
'''

from flask import Flask, render_template, request, redirect, url_for, jsonify
from API_request import *
app = Flask(__name__)


#main page of website
#default method is only GET
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET': #if request is get (user navigated to the URL)
        return render_template('index.html')
    else:
        event1 = {
            "name" : str(request.form['event1_name']),
            "start": str(request.form['event1_start']),
            "end" : str(request.form['event1_end']),
            "location" : str(request.form['location1'])
        }
        event2 = {
            "name" : str(request.form['event2_name']),
            "start": str(request.form['event2_start']),
            "end" : str(request.form['event2_end']),
            "location" : str(request.form['location2'])
        }
        event3 = {
            "name" : str(request.form['event3_name']),
            "start": str(request.form['event3_start']),
            "end" : str(request.form['event3_end']),
            "location" : str(request.form['location3'])
        }
        event4 = {
            "name" : str(request.form['event4_name']),
            "start": str(request.form['event4_start']),
            "end" : str(request.form['event4_end']),
            "location" : str(request.form['location4'])
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



