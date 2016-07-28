from events import events
from tweet import send_tweet
import pytz
from datetime import datetime

now = datetime.now(pytz.timezone("Europe/London"))

for ev in events:
    if ev[1][0] == now.year and ev[1][1] == now.month and ev[1][2] == now.day and ev[1][3] == now.hour and ev[1][4] == now.minute+5:
         send_tweet("Head to The Maths Village now for "+ev[0]+", starting at "+str(ev[1][3])+":"+str(ev[1][4])+" #emfcamp #tweetprinter")
