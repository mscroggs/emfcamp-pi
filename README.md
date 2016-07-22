# emfcamp-pi
Code that will run on the Raspberry Pi 3 at
[Electromagnetic Field](http://emfcamp.org) in 
[The Maths Village](https://wiki.emfcamp.org/wiki/Village:The_Maths_Village>).

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
