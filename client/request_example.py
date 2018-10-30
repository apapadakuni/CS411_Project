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

def example_fcn():
    return 'hello'


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

def 
a = get_calories_info_byonlymiles(4)
print(a)






