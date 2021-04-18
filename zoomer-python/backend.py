from __future__ import print_function
import datetime
import sched
import time
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# If modifying these scopes, go delete the token.json file (needs to generate a new one).
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


# BACKEND FUNCTION
# (from quickstart.py; don't touch this, it makes oauth work)
# either let user log in, or continue if already logged in
# returns creds (auth obj from json)
def authenticate():  
	creds = None
	# The file token.json stores the user's access and refresh tokens, and is
	# created automatically when the authorization flow completes for the first
	# time.
	if os.path.exists('token.json'):
		creds = Credentials.from_authorized_user_file('token.json', SCOPES)
	# If there are no (valid) credentials available, let the user log in.
	if not creds or not creds.valid:
		if creds and creds.expired and creds.refresh_token:
			creds.refresh(Request())
		else:
			flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
			creds = flow.run_local_server(port=0)
		# Save the credentials for the next run
		with open('token.json', 'w') as token:
			token.write(creds.to_json())
	return creds

# FRONTEND FUNCTION
# (from quickstart.py; probably won't keep this but for now it's useful for reference)
# prints out the next ten events from a specified calendar
def getNextTenEventsFromCal(service, calendarID):
	now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
	#print('Getting the upcoming 10 events')
	events_result = service.events().list(calendarId=calendarID, timeMin=now, maxResults=10, singleEvents=True, orderBy='startTime').execute()
	events = events_result.get('items', [])
	if not events:
		print('No upcoming events found.')
	for event in events:
		start = event['start'].get('dateTime', event['start'].get('date'))
		print(start, event['summary'])

# BACKEND FUNCTION
# get next event from specified calendar
# (potentially temporary) helper function
def getNextEvent(service, calendarID):
	now = datetime.datetime.utcnow().isoformat() + 'Z'
	temp_result = service.events().list(calendarId=calendarID, timeMin=now, maxResults=1, singleEvents=True, orderBy='startTime').execute()
	temp_events = temp_result.get('items', [])
	return temp_events


# TODO: make this method (way) more robust (might be a future task)
# (currently it assumes that if event location contains "zoom.us", the entire field is a valid zoom URL)
# BACKEND FUNCTION
# input event (assume "event" is an actual gcal event resource)
# returns boolean depending on whether inputted event is on zoom
# (i.e. check if location field is a zoom link)
def isZoomEvent(event):
	return event['location'].find("zoom.us")

# BACKEND FUNCTION
# TODO: return the next ten events from all calendars
# important - these are the ten events that will be scheduled to launch
def nextTenEvents(service):
	counter = 0
	#initialize list with next event from primary calendar:
	nextTenList = getNextEvent(service, 'primary')
	for calID in activeCals:
		getNextTenEventsFromCal(service, calID)

# FRONTEND FUNCTION
# set activeCals contains available calendars the user wishes to include
# TODO: update activeCals when user selects/deselects calendars
# (Jimmy this is pretty frontend so you should prob write this one)
# (feel free to change what I put here, it's mostly placeholder)
activeCals = set()
def updateActiveCals(cal):
	activeCals.add(cal)
	#stuff goes here

# BACKEND FUNCTION
# returns a set containing all the calendars the user has access to
# (use this to provide the list of possible calendars to the user)
def getCalList(service):
	return service.calendarList().list().execute()
	




# We'll use this as the master schedule; keep it updated, etc.
# TODO: Probably needs some kind of arguments passed in 
eventQueue = sched.scheduler()

# BACKEND FUNCTION
# input zoom url and start time
# TODO: schedule upcoming events
# (Barış, replace this with your scheduling function with zoom call once you finish it)
def scheduleEvent(eventUrl,eventStart):
	#do stuff
	return True

# FRONTEND FUNCTION
# see upcoming scheduled events
# TODO: we likely will want to present the data more nicely for the user;
# could be a front-end task
def getQueue():
	return eventQueue.queue

# BACKEND FUNCTION
# update every ~3 minutes while app is open
def refresh(service):
	#every 3-ish minutes, get next ten events from active calendars
	nextTenEvents(service)
	return True



# BACKEND FUNCTION
# I mean, it's main(); the user shouldn't be poking at this interactively
def main():
	creds = authenticate();
	service = build('calendar', 'v3', credentials=creds)  # seems like a command for run time
	
	#probably something involving the connecting the backend to the frontend/interface goes here, idk

	#scheduler object to check for updates every 3 minutes or so; not the same as the main event queue
	refresher = sched.scheduler(time.time,time.sleep) #idk if the arguments are right
	refresher.enter(180,3,refresh(service))
	while True:  #infinite loop to keep it updating in the background; might want to find a better way though
		refresher.run()



if __name__ == '__main__':
	main()
