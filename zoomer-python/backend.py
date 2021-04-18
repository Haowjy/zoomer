from __future__ import print_function
import datetime
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


# BACKEND FUNCTION authenticate(): either let user log in, or continue if already logged in
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

def getNextTenEventsFromCal(service, calendarID):  # exactly what it says on the tin
	now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
	#print('Getting the upcoming 10 events')
	events_result = service.events().list(calendarId=calendarID, timeMin=now,
										maxResults=10, singleEvents=True,
										orderBy='startTime').execute()
	events = events_result.get('items', [])

	if not events:
		print('No upcoming events found.')
	for event in events:
		start = event['start'].get('dateTime', event['start'].get('date'))
		print(start, event['summary'])	

zoomerCalList = set()
def addCalToZoomerCalList(cal):
	zoomerCalList.add(cal)

def getCalList(service):  # return a set containing all the calendars the user has access to
	return service.calendarList().list().execute()
	
def main():
	creds = authenticate();
	service = build('calendar', 'v3', credentials=creds)  # seems like a command for run time

	for calID in zoomerCalList:
		getNextTenEventsFromCal(service, calID)
	
if __name__ == '__main__':
	main()
