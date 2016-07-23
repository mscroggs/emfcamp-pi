import tweet_about_days

import make_calendar

import os

os.system("scp /home/pi/.emf/mathscal.ical mscroggs:/home/mscroggs/public_html/mathscal.ical")
from tweet import send_tweet
send_tweet("Run every hour works!")
