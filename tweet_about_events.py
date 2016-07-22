from events import events
from tweet import send_tweet
import ptyz

now = datetime.now(pytz.timezone("Europe/London"))

for ev in events:
    if ev[1][0] == now.year and ev[1][1] == now.month and ev[1][2] == now.day and ev[1][3] == now.hour and ev[1][4] <= now.minute < ev[1][4] + 20:
         send_tweet("Head to The Maths village now for "+ev[0]+", starting at "+str(ev[1][3])+":"+str(ev[1][4])+" #emf2016 #tweetprinter")
