from __future__ import print_function
import datetime
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'

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


    first_time = 1
    if not events:
        print('No upcoming events found.')
    event_by_day = {}
    event_by_day['Mon'] = []
    event_by_day['Tue'] = []
    event_by_day['Wed'] = []
    event_by_day['Thu'] = []
    event_by_day['Fri'] = []
    event_by_day['Sat'] = []
    event_by_day['Sun'] = []
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
        event_start_day = datetime.datetime.strptime(start_date, '%Y-%m-%d').strftime('%a')
        
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
            "start_time" : start_time,
            "end_time" : end_time,
            "location" : event_location
        }

        
        event_by_day[event_start_day].append(parsed_event)      #adding event to specific day


        


if __name__ == '__main__':
    a = get_googlecalendar_events()
    print(a)