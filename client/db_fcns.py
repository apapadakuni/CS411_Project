from pymongo import MongoClient
from pprint import pprint
import subprocess
import os
import time
import signal

# #create connection to db
# pro = subprocess.Popen(["mongod"], stdout = subprocess.PIPE,shell=True, preexec_fn=os.setsid)
# time.sleep(1)
# client = MongoClient('mongodb://localhost:27017')
# collection = client['CS411_Project']
# db = collection.users


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

def db_update_personal_info(email, height, weight, sex, age, dist):
	#assuming they are already registered as a user
	try:
		db.update({
			'email':email
			},
			{
			'height': height,
			'weight': weight,
			'sex': sex,
			'age': age,
			'min_dist': dist
			}, multi = False)
		return 0
 	except:
 		return -1

# def db_terminate_connection():

# em = "example@gmail.com"
# s = db_make_connection()
# sup = db_check_user(s, em)
# print("user %d\n" % sup)
# b = db_update_personal_info(em, 4, 5, 6, 8, 8)
# print(b)
# os.killpg(os.getpgid(pro.pid), signal.SIGTERM)  # Send the signal to all the process groups

# all_user_info = db.users
# cource = {'hi':5}
# # res = courses.insert(cource)
# courses.update({
#     'hi': 5
#     },
#     {
#         '$set':{
#             'bitch': 'changed value'
#         }
#     }, multi = False)
