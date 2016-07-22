# emfcamp-pi
Code that will run on the Raspberry Pi 3 at
[Electromagnetic Field](http://emfcamp.org) in 
[The Maths Village](https://wiki.emfcamp.org/wiki/Village:The_Maths_Village>).
Before EMF, the Pi will be running in my flat.

I will be setting cron jobs on the Pi to:
- Run `run_minute.py` every minute.
- Run `run_20min.py` every 20 minutes.
- Run `run_hour.py` every hour.

Before EMF starts, I will install all python packages named in
`requirements-pip.txt` (using `pip`), install all the packages in
`requirements-apt-get.txt` (using `apt-get`), and I so all the things
in `requirements-other.txt`.

The Pi will be connected to:
- A recipt printer (see `printer.py`).
- The internet via an ethernet cable.

The Pi will:
- Print out everything on Twitter with [#tweetprinter](https://twitter.com/hashtag/tweetprinter?f=tweets&vertical=default&src=hash).
- Upload the village events calendar to [mscroggs.co.uk/emfcal](http://mscroggs.co.uk/emfcal).
- Tweet as [@emfscroggsbot](https://twitter.com/emfscroggsbot).


## What each file does.
- `config.py` contains login information for Twitter (not shared on GitHub obvs).
- `events.py` contains a list of events in the village.
- `make_calendar.py` converts the list of events into an icalendar file.
- `printer.py` contains functions that allow use of the receipt printer.
- `README.md` is this readme file.
- `requirements-*.txt` are text files telling me what needs installing on the Pi.
- `run_*.py` are files that will be run by cron.
- `tweet_about_days.py` will send tweets reminding people that it is the (n)th day of EMF.
- `tweet_about_events.py` will send tweets reminding people that events are about to start.
- `tweet.py` contains functions that will send tweets.
