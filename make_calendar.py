from icalendar import Calendar, Event
from datetime import datetime
import pytz

cal = Calendar()
cal.add('prodid', '-//The Maths Village events//mscroggs.co.uk//EN')
cal.add('version', '2.0')

event_n = 0

def add_event(name, desc, s, e):
    global cal
    global event_n
    event_n += 1
    event = Event()
    event.add('summary', name)
    event.add('dtstart', datetime(s[0],s[1],s[2],s[3],s[4],s[5],tzinfo=pytz.timezone("Europe/London")))
    event.add('dtend', datetime(e[0],e[1],e[2],e[3],e[4],e[5],tzinfo=pytz.timezone("Europe/London")))
    event.add('dtstamp', datetime(2016,8,1,0,10,0,tzinfo=pytz.timezone("Europe/London")))
    event.add('description',desc)
    event.add('location',"The Maths Village marquee")
    event['uid'] = 'event-'+str(event_n)+'@mscroggs.co.uk'
    event.add('priority', 5)

    cal.add_component(event)

from events import events

for ev in events:
    if len(ev) >= 4:
        add_event(ev[0],ev[3],ev[1],ev[2])
    else:
        add_event(ev[0],ev[0],ev[1],ev[2])


try:
    with open('/home/pi/.emf/mathscal.ical', 'w') as f:
        f.write(cal.to_ical())
except:
    with open('mathscal.ical', 'w') as f:
        f.write(cal.to_ical())
