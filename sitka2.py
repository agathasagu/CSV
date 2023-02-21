# using datetime module
# adding dates to the x- axis
import csv
import matplotlib.pyplot as plt
from datetime import datetime

infile = open("sitka_weather_07-2018_simple.csv", "r")
csvfile = csv.reader(infile)

header_row = next(csvfile)


for index, column_header in enumerate(header_row):
    print(index, column_header)

highs = []
dates = []

mydate = datetime.strptime("2018-07-01", "%Y-%m-%d")
print(mydate)

for row in csvfile:
    highs.append(int(row[5]))
    thedate = datetime.strptime(row[2], "%Y-%m-%d")
    dates.append(thedate)

fig = plt.figure()

plt.plot(dates, highs, c="red")
plt.title("Daily high temp for Sitka Alaska, July 2018", fontsize=16)
plt.xlabel("")
plt.ylabel("Temperature(F)", fontsize=12)
plt.tick_params(axis="both", which="major", labelsize=12)

fig.autofmt_xdate()
plt.show()
