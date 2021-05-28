# DutyScheduleMaker.py
# Arpan Das

import pandas as pd
import re

# read in file as df (made this a variable so it's easier to read/understand)

# had to make an edit to original doc
# changed the A1 cell to "Name" from blank so it's easier to manipulate

filename = "Spring Summer 2021 PRO Leader availability.csv"
df = pd.read_csv(filename, encoding='UTF-8')

# fill in blanks with 0 (unavailable)
df = df.fillna(value = 0)

# document with PRO Leader info
df2 = pd.read_csv("PROLinfo.csv", encoding='UTF-8')

# print(df.head(), '\n', df.info())

# store in all the event dates in a list
dates = []
counter = 0
for date in df:
  if (date not in dates) and (counter > 2):
    dates.append(date)
  counter += 1

# store in all the PRO Leader names in a list
names = []
for name in df['Name']:
  x = re.search("([A-Z])\w+", name)
  if x:
    names.append(name)

# print(dates, names)

availability = []

# store available PRO Leaders with event day/time, name, and their availablity in a tuple
# this doesn't account for people saying "no"
for date in dates:
  for i in range(len(df[date]) - 2):
    if df[date][i+2]:
      availability.append([date, names[i], df[date][i+2]])

pot_time_conflicts = []

# clean data:
# change yes's to 1 and no's to 0

# shallow copy to remove the 0s on
temp = availability.copy()

for i in availability:
  # store time conflicts in a separate tuple
  # idk what to do with these rn but that's a later problem (:
  x = re.search("\d", i[2])
  if x:
    pot_time_conflicts.append(i)

  a = re.search("^(y|Y)", i[2]) # (y|Y) to get Yes/yes/Yuh/yep, etc.
  # if a:
  #   print(i[2])
  b = re.search("\d", i[2]) # \d to get any times
  c = re.search("^:\W", i[2]) # to get :)
  d = re.search("(x|X)", i[2]) # to get x
  e = re.search("^\W", i[2]) # to get checkmarks
  f = re.search("(OK|ok)", i[2]) # to get OK

  if(a or b or c or d or e or f):
    i[2] = "1"

  # right now i say that if it's not a yes then it's a no, but there's also maybes
  # i may move that to yes? idk ask Mike lol
  if i[2] != "1":
    temp.remove(i)

availability = temp

# for i in pot_time_conflicts:
#   print(i)

# for regex cleaning
# get the times for stuff (later)
