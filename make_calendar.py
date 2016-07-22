from icalendar import Calendar, Event
from datetime import datetime
import pytz

cal = Calendar()
cal.add('prodid', '-//The Maths Village events//mscroggs.co.uk//EN')
cal.add('version', '2.0')

event_n = 0

def add_event(name, s, e):
    global cal
    global event_n
    event_n += 1
    event = Event()
    event.add('summary', name)
    event.add('dtstart', datetime(s[0],s[1],s[2],s[3],s[4],s[5],tzinfo=pytz.timezone("Europe/London")))
    event.add('dtend', datetime(e[0],e[1],e[2],e[3],e[4],e[5],tzinfo=pytz.timezone("Europe/London")))
    event.add('dtstamp', datetime(2016,8,1,0,10,0,tzinfo=pytz.timezone("Europe/London")))
    event['uid'] = 'event-'+str(event_n)+'@mscroggs.co.uk'
    event.add('priority', 5)

    cal.add_component(event)

add_event('Maths puzzle evening',(2016,8,5,20,0,0),(2016,8,5,23,59,0))



with open('/home/pi/.emf/mathscal.ics', 'w') as f:
    f.write(cal.to_ical())
