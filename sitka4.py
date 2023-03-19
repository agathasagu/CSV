# 1. handle error checking using try and except
# 2. change file to use death valley rate


import csv
import matplotlib.pyplot as plt
from datetime import datetime

infile = open("death_valley_2018_simple.csv", "r")
csvfile = csv.reader(infile)

header_row = next(csvfile)


for index, column_header in enumerate(header_row):
    print(index, column_header)

highs = []
lows = []
dates = []

# mydate = datetime.strptime("2018-07-01", "%Y-%m-%d")
# print(mydate)

for row in csvfile:
    try:
        high = int(row[4])
        low = int(row[5])
        thedate = datetime.strptime(row[2], "%Y-%m-%d")

    except ValueError as err:
        print("There is an error in ", row[2])
    else:
        highs.append(high)
        lows.append(low)
        dates.append(thedate)


fig = plt.figure()

plt.plot(dates, highs, c="red", alpha=0.5)
plt.plot(dates, lows, c="blue", alpha=0.5)
plt.fill_between(x=dates, y1=highs, y2=lows, facecolor="blue", alpha=0.1)
plt.title("Daily high and low temperatures - 2018", fontsize=16)
plt.xlabel("")
plt.ylabel("Temperature(F)", fontsize=12)
plt.tick_params(axis="both", which="major", labelsize=12)


fig.autofmt_xdate()
plt.show()
