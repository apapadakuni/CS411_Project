import requests
import json


def get_calories_info(miles, gender, weight, height, age):
    #all necessary information for GET API
    API_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
    API_ID = "428a1f39"
    API_KEY = "080f20a722118011a86c2b7f3a32c47a"
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
    API_ID = "428a1f39"
    API_KEY = "080f20a722118011a86c2b7f3a32c47a"
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
        "key":"AIzaSyDGs-CyF1VB_8BIHeQ9tE20VBYDV8U8RY4",
        "mode":"walking"
        }
    headers = {
        'cache-control': "no-cache",
        'Postman-Token': "e9e299a8-acd4-47a3-a1c0-a3c1b7cded2d"
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

def can_I_walk_it(event1, event2):
    google_res = get_google_directions(event1["location"],event2["location"])
    time_needed = google_res["minutes"]
    miles_needed = google_res["miles"]
    hour1 = event1["end"]
    hour2 = event2["start"]
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
            "calories": 0,
            "miles": 0,
            "time": 0
        }
    else:
        calories_burnt = get_calories_info_byonlymiles(miles_needed)                #change function here for user needs
        results = {
            "calories": calories_burnt,
            "miles":miles_needed,
            "time":time_needed
        }
    return results

# first = {
#     "location": "700 Commonwealth Avenue, Boston, MA",
#     "start": "02:00",
#     "end": "04:00"
# }
# second = {
#     "location": "10 Harbor Point Boulevard",
#     "start":"06:00",
#     "end": "08:00"
# }

        
