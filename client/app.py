'''
Author: Craig Einstein
File: search_app.py
Description: A simple web application that connects to the sakila database and implements a query execution feature
'''

from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)


#main page of website
#default method is only GET
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')





