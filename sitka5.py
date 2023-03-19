# using datetime module
# 1. Changing the file to include all the data for the year of 2018
# 2. change the title to -Daily and low high temperatures - 2018
# 3. extract low temps from the file and add to the chart
# 4. shade in the area between high and low

import csv
import matplotlib.pyplot as plt
from datetime import datetime

infile = open("sitka_weather_2018_simple.csv", "r")
csvfile = csv.reader(infile)
header_row = next(csvfile)

dvinfile = open("death_valley_2018_simple.csv", "r")
dvcsvfile = csv.reader(dvinfile)
dvheader_row = next(dvcsvfile)


highs = []
lows = []
dates = []
dvhigh = []
dvlow = []
dvdate = []


for row in csvfile:
    highs.append(int(row[5]))
    lows.append(int(row[6]))
    thedate = datetime.strptime(row[2], "%Y-%m-%d")
    dates.append(thedate)


for row in dvcsvfile:
    try:
        high = int(row[4])
        low = int(row[5])
        thedate = datetime.strptime(row[2], "%Y-%m-%d")

    except ValueError as err:
        print("There is an error in ", row[2])
    else:
        dvhigh.append(high)
        dvlow.append(low)
        dvdate.append(thedate)

fig = plt.figure()


fig.autofmt_xdate()

plt.subplot(2, 1, 1)
plt.plot(dates, highs, c="red")
plt.plot(dates, lows, c="blue")
plt.fill_between(x=dates, y1=highs, y2=lows, facecolor="blue", alpha=0.1)
plt.title("SITKA AIRPORT, AK US")

plt.subplot(2, 1, 2)
plt.plot(dvdate, dvlow, c="blue")
plt.plot(dvdate, dvhigh, c="red")
plt.fill_between(x=dvdate, y1=dvhigh, y2=dvlow, facecolor="blue", alpha=0.1)
plt.title("DEATH VALLEY, CA US")

plt.suptitle(
    "Temperature Comparison between SITKA AIRPORT, AK US and DEATH VALLEY, CA US"
)

plt.show()
