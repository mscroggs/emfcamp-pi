from events import events
from tweet import send_tweet
import pytz
from datetime import datetime

now = datetime.now(pytz.timezone("Europe/London"))

for ev in events:
    if 2016 == now.year and 8 == now.month and 8 == now.hour:
        if now.day == 5:
            send_tweet("Wake up everyone! It's time for the first day of Electromagnetic Field!")
        if now.day == 6:
            send_tweet("Wake up everyone! It's time for the second day of Electromagnetic Field!")
        if now.day == 7:
            send_tweet("Wake up everyone! It's time for the third day of Electromagnetic Field!")
