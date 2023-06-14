import calendar
import datetime

now = datetime.datetime.now()
dotw = calendar.day_name[now.weekday()]

y = int(now.strftime("%Y"))
m = int(now.strftime("%m"))
d = int(now.strftime("%d"))

def amTimes(am_open, am_close):
  print(f"OPEN:")
  print(f"Open Swim (ALL AGES)")
  print(am_open.strftime("%I") + ":" + am_open.strftime("%M"), am_open.strftime("%p"), "-", am_close.strftime("%I") + ":" + am_close.strftime("%M"), am_close.strftime("%p"))

def familyNight(family_night_open, family_night_close):
  print("OPEN:")
  print("Family Night - $15 per family (ALL AGES)")
  print(family_night_open.strftime("%I") + ":" + family_night_open.strftime("%M"), family_night_open.strftime("%p"), "-", family_night_close.strftime("%I") + ":" + family_night_close.strftime("%M"), family_night_close.strftime("%p"))

def halfOff(half_off_open, half_off_close):
  print("OPEN:")
  print("Open Swim - Half Price! (ALL AGES)")
  print(half_off_open.strftime("%I") + ":" + half_off_open.strftime("%M"), half_off_open.strftime("%p"), "-", half_off_close.strftime("%I") + ":" + half_off_close.strftime("%M"), half_off_close.strftime("%p"))

if datetime.datetime(year=2023, month=6, day=2, hour=00, minute=00) <= now < datetime.datetime(year=2023, month=9, day=1, hour=00, minute=00):
    am_open = datetime.datetime(year=y, month=m, day=d, hour=12, minute=00)
    if dotw == "Saturday":
       am_close = datetime.datetime(year=y, month=m, day=d, hour=18, minute=00)
       if am_open <= now < am_close:
          amTimes(am_open, am_close)
       elif am_close <= now:
          print("CLOSED")
    else:
        am_close = datetime.datetime(year=y, month=m, day=d, hour=17, minute=30)
        adult_swim_open = datetime.datetime(year=y, month=m, day=d, hour=17, minute=30)
        adult_swim_close = datetime.datetime(year=y, month=m, day=d, hour=18, minute=30)
        pm_open = datetime.datetime(year=y, month=m, day=d, hour=18, minute=30)
        pm_close = datetime.datetime(year=y, month=m, day=d, hour=20, minute=30)
        if am_open <= now < am_close:
            amTimes(am_open, am_close)
        elif adult_swim_open <= now < adult_swim_close:
           print("OPEN:")
           print("Current Walking and Adult Lap Swim (18+ ONLY)")
           print(f'{adult_swim_open.strftime("%I")}:{adult_swim_open.strftime("%M")} {adult_swim_open.strftime("%p")} - {adult_swim_close.strftime("%I")}:{adult_swim_close.strftime("%M")} {adult_swim_close.strftime("%p")}')
        elif pm_open <= now < pm_close:
           if (dotw == "Wednesday") or (dotw == "Sunday"):
              familyNight(pm_open, pm_close)
           else:
              halfOff(pm_open, pm_close)
        elif pm_close <= now:
           print("CLOSED")