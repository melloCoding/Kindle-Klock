# file: clock.py
# purpose: use ntp to get local time, then set the kindle's system clock to that
# time value retrieved from ntp, and provide tools to resync the ntp when needed

import datetime
import subprocess

# Returns the current timn from the system clock and removes 0 from the begining
# to make it more readable
def getTime():
    return datetime.datetime.now().strftime("%I:%M").lstrip("0")

def amOrPm():
    return datetime.datetime.now().strftime("%p")

# Get the month and date from the system clock in the format of:
# [day of week], [month name] [date]
def getMonthAndDate():
    return datetime.datetime.now().strftime("%A, %B %d")

# Use the ntpupdate command from the kindle in order to sync the system clock
# as the kindle's clock is very inacurate
def syncSystemClock():
    subprocess.run("ntpdate -u pool.ntp.org")
