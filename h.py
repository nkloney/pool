import calendar
import datetime

now = datetime.datetime.now()
dotw = calendar.day_name[now.weekday()]

y = int(now.strftime("%Y"))
m = int(now.strftime("%m"))
d = int(now.strftime("%d"))

def swimLessons():
  sl1 = datetime.datetime(year=2023, month=6, day=5, hour=00, minute=00) <= now < datetime.datetime(year=2023, month=6, day=9, hour=00, minute=00)

  sl2 = datetime.datetime(year=2023, month=6, day=12, hour=00, minute=00) <= now < datetime.datetime(year=2023, month=6, day=16, hour=00, minute=00)
  
  sl3 = datetime.datetime(year=2023, month=6, day=19, hour=00, minute=00) <= now < datetime.datetime(year=2023, month=6, day=23, hour=00, minute=00)
  
  sl4 = datetime.datetime(year=2023, month=6, day=26, hour=00, minute=00) <= now < datetime.datetime(year=2023, month=6, day=30, hour=00, minute=00)
  
  sl5 = datetime.datetime(year=2023, month=7, day=10, hour=00, minute=00) <= now < datetime.datetime(year=2023, month=7, day=14, hour=00, minute=00)
  
  sl6 = datetime.datetime(year=2023, month=7, day=17, hour=00, minute=00) <= now < datetime.datetime(year=2023, month=7, day=21, hour=00, minute=00)
  
  sl7 = datetime.datetime(year=2023, month=7, day=24, hour=00, minute=00) <= now < datetime.datetime(year=2023, month=7, day=28, hour=00, minute=00)
  
  sl8 = datetime.datetime(year=2023, month=7, day=31, hour=00, minute=00) <= now < datetime.datetime(year=2023, month=8, day=4, hour=00, minute=00)

  if (sl1 == True) or (sl2 == True) or (sl3 == True) or (sl4 == True) or (sl5 == True) or (sl6 == True) or (sl7 == True) or (sl8 == True):
    return True

swimLessons()

if datetime.datetime(year=2023, month=6, day=2, hour=00, minute=00) <= now < datetime.datetime(year=2023, month=9, day=1, hour=00, minute=00):
  if dotw == "Sunday":
    am_open = datetime.datetime(year=y, month=m, day=d, hour=12, minute=00)
  else:
    am_open = datetime.datetime(year=y, month=m, day=d, hour=11, minute=30)

# AM CLOSE TIMES
if swimLessons() != True:
  if (dotw == "Wednesday") or (dotw == "Sunday"):
    am_close = datetime.datetime(year=y, month=m, day=d, hour=17, minute=45)
  elif dotw == "Saturday":
    am_close = datetime.datetime(year=y, month=m, day=d, hour=18, minute=00)
  else:
    am_close = datetime.datetime(year=y, month=m, day=d, hour=19, minute=00)
elif swimLessons() == True:
  am_close = datetime.datetime(year=y, month=m, day=d, hour=17, minute=30)

# -----------------------------------------------------------------
# PM TIMES
if swimLessons() != True:
  if dotw != "Saturday":
    if (dotw == "Sunday") or (dotw == "Wednesday"):
      # FAMILY NIGHT
      family_night_open = datetime.datetime(year=y, month=m, day=d, hour=18, minute=30)
      family_night_close = datetime.datetime(year=y, month=m, day=d, hour=20, minute=30)
    else:
      # HALF OFF
      half_off_open = datetime.datetime(year=y, month=m, day=d, hour=17, minute=00)
      half_off_close = datetime.datetime(year=y, month=m, day=d, hour=19, minute=00)

# -----------------------------------------------------------------
# OPEN OR CLOSED DETECTOR
# OPEN SWIM
if am_open <= now < am_close:
  print(f"OPEN:")
  print(f"Open Swim (ALL AGES)")
  print(am_open.strftime("%I") + ":" + am_open.strftime("%M"), am_open.strftime("%p"), "-", am_close.strftime("%I") + ":" + am_close.strftime("%M"), am_close.strftime("%p"))

# -----------------------------------------------------------------
# CLOSED SATURDAYS
if dotw == "Saturday":
  if am_close <= now:
    print("CLOSED")
    
# SWIM LESSONS CLOSED
if swimLessons() == True:
  if am_close <= now:
    print("CLOSED")

# FAMILY NIGHT BREAK
if swimLessons() != True:
  if (dotw == "Sunday") or (dotw == "Wednesday"):
    if am_close <= now < family_night_open:
      print("CLOSED:")
      print("Family Night starts at 6:30 PM")

# -----------------------------------------------------------------
# PM
if swimLessons() != True:
  if dotw != "Saturday":
    # FAMILY NIGHT
    if (dotw == "Sunday") or (dotw == "Wednesday"):
      if family_night_open <= now < family_night_close:
        print("OPEN:")
        print("Family Night - $15 per family (ALL AGES)")
        print(family_night_open.strftime("%I") + ":" + family_night_open.strftime("%M"), family_night_open.strftime("%p"), "-", family_night_close.strftime("%I") + ":" + family_night_close.strftime("%M"), family_night_close.strftime("%p"))
    else:
      # HALF OFF
      if half_off_open <= now < half_off_close:
        print("OPEN:")
        print("Open Swim - Half Price! (ALL AGES)")
        print(half_off_open.strftime("%I") + ":" + half_off_open.strftime("%M"), half_off_open.strftime("%p"), "-", half_off_close.strftime("%I") + ":" + half_off_close.strftime("%M"), half_off_close.strftime("%p"))

# -----------------------------------------------------------------
# CLOSED
if swimLessons() != True:
  if dotw != "Saturday":
    if (dotw == "Sunday") or (dotw == "Wednesday"):
      if family_night_close <= now:
        print("CLOSED")
    else:
      if half_off_close <= now:
        print("CLOSED")