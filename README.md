# emfcamp-pi
Code that will run on the Raspberry Pi 3 at
[Electromagnetic Field](http://emfcamp.org) in 
[The Maths Village](https://wiki.emfcamp.org/wiki/Village:The_Maths_Village>).

I will be setting cron jobs on the Pi to:
- Run `run_minute.py` every minute.
- Run `run_20min.py` every 20 minutes.
- Run `run_hour.py` every hour.

Before EMF starts, I will install all python packages named in `requirements.txt`.
