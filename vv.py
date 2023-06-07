import calendar
import datetime

now = datetime.datetime.now()
dotw = calendar.day_name[now.weekday()]

y = int(now.strftime("%Y"))
m = int(now.strftime("%m"))
d = int(now.strftime("%d"))

if datetime.datetime(year=2023, month=6, day=2, hour=00, minute=00) <= now < datetime.datetime(year=2023, month=9, day=1, hour=00, minute=00):
    am_open = datetime.datetime(year=y, month=m, day=d, hour=12, minute=00)

# -----------------------------------------------------------------
# AM CLOSE TIMES
if dotw != "Saturday":
  am_close = datetime.datetime(year=y, month=m, day=d, hour=17, minute=30)

if dotw == "Saturday":
  am_close = datetime.datetime(year=y, month=m, day=d, hour=18, minute=00)

# -----------------------------------------------------------------
# PM TIMES
if dotw != "Saturday":
# ADULT SWIM TIMES
  adult_swim_open = datetime.datetime(year=y, month=m, day=d, hour=17, minute=30)
  adult_swim_close = datetime.datetime(year=y, month=m, day=d, hour=18, minute=30)
# PM OPEN SWIM TIMES
  pm_open = datetime.datetime(year=y, month=m, day=d, hour=18, minute=30)
  pm_close = datetime.datetime(year=y, month=m, day=d, hour=20, minute=30)

# -----------------------------------------------------------------
# OPEN OR CLOSED DETECTOR
# OPEN SWIM
if am_open <= now < am_close:
  print(f"OPEN:")
  print(f"Open Swim (ALL AGES)")
  print(f'{am_open.strftime("%I")}:{am_open.strftime("%M")} {am_open.strftime("%p")} - {am_close.strftime("%I")}:{am_close.strftime("%M")} {am_close.strftime("%p")}')

# -----------------------------------------------------------------
# CLOSED SATURDAYS
if dotw == "Saturday":
  if am_close <= now:
    print("CLOSED")

# -----------------------------------------------------------------
# ADULT SWIM
if dotw != "Saturday":
  if adult_swim_open <= now < adult_swim_close:
    print("OPEN:")
    print("Current Walking and Adult Lap Swim (18+ ONLY)")
    print(f'{adult_swim_open.strftime("%I")}:{adult_swim_open.strftime("%M")} {adult_swim_open.strftime("%p")} - {adult_swim_close.strftime("%I")}:{adult_swim_close.strftime("%M")} {adult_swim_close.strftime("%p")}')

# -----------------------------------------------------------------
# PM
if dotw != "Saturday":
  if pm_open <= now < pm_close:
    # FAMILY NIGHT
    if (dotw == "Sunday") or (dotw == "Wednesday"):
      print("OPEN:")
      print("Family Night - $15 per family (ALL AGES)")
      print(f'{pm_open.strftime("%I")}:{pm_open.strftime("%M")} {pm_open.strftime("%p")} - {pm_close.strftime("%I")}:{pm_close.strftime("%M")} {pm_close.strftime("%p")}')
    else:
      # OPEN SWIM
      print("OPEN:")
      print("Open Swim - Half Price! (ALL AGES)")
      print(f'{pm_open.strftime("%I")}:{pm_open.strftime("%M")} {pm_open.strftime("%p")} - {pm_close.strftime("%I")}:{pm_close.strftime("%M")} {pm_close.strftime("%p")}')

# -----------------------------------------------------------------
# CLOSED
if dotw != "Saturday":
  if pm_close <= now:
    print("CLOSED")