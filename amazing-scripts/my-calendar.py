import icalendar

# Read the ICS file
cal = icalendar.Calendar.from_ical(open('./data/sadiakhouyaya738@gmail.com.ics', 'rb').read())

# Get all the events
events = cal.walk('VEVENT')

if __name__ == '__main__':
    # Print the summary of each event
    print("Events in the calendar:", len(events))
    for event in events:
        print(event['summary'])
