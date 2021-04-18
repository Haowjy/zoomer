# borderline pseudocode
page_token = None
while True:
    events = service.events().list(calendarId = 'primary', pageToken = page_token).execute()
    for event in events['items']:
        print event['summary']
    page_token = events.get('nextPageToken')
    if not page_token:
        break