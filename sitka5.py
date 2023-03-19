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

svtmax_index = header_row.index("TMAX")
svtmin_index = header_row.index("TMIN")
svname_index = header_row.index("NAME")
svdate_index = header_row.index("DATE")

dvtmax_index = dvheader_row.index("TMAX")
dvtmin_index = dvheader_row.index("TMIN")
dvname_index = dvheader_row.index("NAME")
dvdate_index = dvheader_row.index("DATE")


highs = []
lows = []
dates = []
dvhigh = []
dvlow = []
dvdate = []


for row in csvfile:
    highs.append(int(row[svtmax_index]))
    lows.append(int(row[svtmin_index]))
    thedate = datetime.strptime(row[svdate_index], "%Y-%m-%d")
    name = row[svname_index]
    dates.append(thedate)


for row in dvcsvfile:
    try:
        high = int(row[dvtmax_index])
        low = int(row[dvtmin_index])
        thedate = datetime.strptime(row[dvdate_index], "%Y-%m-%d")
        dvname = row[dvname_index]

    except ValueError as err:
        print("There is an error in ", row[dvdate_index])
    else:
        dvhigh.append(high)
        dvlow.append(low)
        dvdate.append(thedate)
        dvname = row[dvname_index]

fig = plt.figure()


plt.subplot(2, 1, 1)
plt.plot(dates, highs, c="red")
plt.plot(dates, lows, c="blue")
plt.fill_between(x=dates, y1=highs, y2=lows, facecolor="blue", alpha=0.1)
plt.title(name)

plt.subplot(2, 1, 2)
plt.plot(dvdate, dvlow, c="blue")
plt.plot(dvdate, dvhigh, c="red")
plt.fill_between(x=dvdate, y1=dvhigh, y2=dvlow, facecolor="blue", alpha=0.1)
plt.title(dvname)

fig.autofmt_xdate()
plt.suptitle("Temperature Comparison between " + name + " and " + dvname)

plt.show()
