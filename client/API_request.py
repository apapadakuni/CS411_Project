import requests
import json


def get_calories_info(miles, gender, weight, height, age):
    #all necessary information for GET API
    API_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
    API_ID = ""
    API_KEY = ""
    request_url = API_ENDPOINT + "?x-app-id=" + API_ID + "&x-app-key=" + API_KEY + "&x-remote-user-id=0&content-type=application/json"

    query = "walked " + str(miles) + "miles"
    data = {
        'query': query,
        'gender': gender,
        'weight_kg': weight,
        'height_cm': height,
        'age': age
    }
  
    # sending post request and saving response as response object 
    r = requests.post(url = request_url, data = data) 
    
    #converting response object to json format
    y = json.loads(r.text)
    calories = y['exercises'][0]['nf_calories']
    return calories



def get_calories_info_byonlymiles(miles):
    API_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
    API_ID = ""
    API_KEY = ""
    request_url = API_ENDPOINT + "?x-app-id=" + API_ID + "&x-app-key=" + API_KEY + "&x-remote-user-id=0&content-type=application/json"

    query = "walked " + str(miles) + "miles"
    data = {
        'query': query
    }
  
    # sending post request and saving response as response object 
    r = requests.post(url = request_url, data = data) 
    
    #converting response object to json format
    y = json.loads(r.text)
    calories = y['exercises'][0]['nf_calories']
    return calories



def get_google_directions(origin, destination):
    #Funcrion receives two addresses as strings, origin and destination
    #and returns the time spent walking from one to the other based on 
    #GOOGLE MAPS DIRECTIONS API
    url = "https://maps.googleapis.com/maps/api/directions/json"
    querystring = {"origin":origin,
        "destination":destination,
        "key":"",
        "mode":"walking"
        }
    headers = {
        'cache-control': "no-cache",
        'Postman-Token': ""
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = json.loads(response.text)

    time = data['routes'][0]['legs'][0]['duration']['text']
    distance = data['routes'][0]['legs'][0]['distance']['text']
    distance = str(distance)
    distance = float(distance[:distance.find(" ")])

    time = str(time)
    if time.find("hour") == -1:
        space_index = time.find(" ")
        minutes = int(time[0:space_index])
    else:
        hours = int(time[0:time.find("hour")])
        minute_str = time[time.find("hour"):]
        minute_str = minute_str[minute_str.find(" ")+1:]
        minutes = int(minute_str[:minute_str.find(" ")])
        minutes = hours*60+minutes
    results = {
        "miles":distance,
        "minutes":minutes
    }
    return results

def can_I_walk_it(event1, event2, user):
    google_res = get_google_directions(event1["location"],event2["location"])
    time_needed = google_res["minutes"]
    miles_needed = google_res["miles"]
    hour1 = event1["end_time"]
    hour2 = event2["start_time"]
    print(hour1[0:2])
    print(hour2)
    hour1 = int(hour1[0:2])*60+int(hour1[3:5])              #time is in format "xx:xx"
    hour2 = int(hour2[0:2])*60+int(hour2[3:5])
    print(hour1)
    print(hour2)
    time_available= hour2 - hour1                           #in minutes
    print(time_available)
    print(time_needed)
    if (time_available < time_needed):                      #NEED TO: add a public transportation API call, since there is no available time to walk the distance
        results = {
            "calories": "You don't have enought time to walk it!",
            "miles": miles_needed,
            "time": time_needed
        }
    else:
        calories_burnt = get_calories_info(miles_needed, user['sex'], user['weight'], user['height'], user['age'])                #change function here for user needs
        results = {
            "calories": calories_burnt,
            "miles":miles_needed,
            "time":time_needed
        }
    return results
    
def sort_calendar_events(events):
    for passnum in range(len(events)-1,0,-1):
        for i in range(passnum):
            if int(events[i]['date'][8:])>=int(events[i+1]['date'][8:]) and int(events[i]['start_time'][0:2]) > int(events[i+1]['start_time'][0:2]):
                print("yooo")
                temp = events[i]
                events[i] = events[i+1]
                events[i+1] = temp


def can_I_walk_all_events(sup):    
    events = sup['calendar_events']
    schedule_all_events = []
    sort_calendar_events(events)
    print(events)
    for i in range(0,len(events)-1):
        event1 = events[i]
        event2 = events[i+1]
        if event1['date'] == event2['date']:
            res = can_I_walk_it(event1, event2, sup)
            schedule = {
                "Event_1": event1,
                "Event_2":event2,
                "Results": res
            }
            schedule_all_events.append(schedule)
    return schedule_all_events

        
# sup = {u'name': u'apapadak', u'weight': u'97', u'min_dist': u'2', u'age': u'21', u'sex': u'male', u'height': u'187', u'_id': "ObjectId('5c0fcb0733abd7ba4fc85169')", u'email': u'apapadak@bu.edu', u'calendar_events': [{u'date': u'2018-12-10', u'start_time': u'12:30', u'end_time': u'13:30', u'location': u'21 Quint Ave, Allston, MA', u'name': u'Sleeping'}, {u'date': u'2018-12-10', u'start_time': u'14:30', u'end_time': u'16:00', u'location': u'700 Commonwealth Ave, Boston, MA', u'name': u'Networking'}, {u'date': u'2018-12-10', u'start_time': u'17:00', u'end_time': u'19:30', u'location': u'720 Commonwealth Ave, Boston, MA', u'name': u'CS411'}, {u'date': u'2018-12-13', u'start_time': u'17:00', u'end_time': u'19:00', u'location': u'Boston Commons', u'name': u'Chilling'}, {u'date': u'2018-12-13', u'start_time': u'12:30', u'end_time': u'14:30', u'location': u'Kenmore Square, Boston', u'name': u'Studying'}, {u'date': u'2018-12-13', u'start_time': u'07:00', u'end_time': u'09:30', u'location': u'870 Beacon St, Boston, MA', u'name': u'Visiting my pretend GF'}]}
# a = can_I_walk_all_events(sup)
# print(a)


