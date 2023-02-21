import csv
import matplotlib.pyplot as plt

infile = open("sitka_weather_07-2018_simple.csv", "r")
csvfile = csv.reader(infile)

header_row = next(csvfile)


for index, column_header in enumerate(header_row):
    print(index, column_header)

highs = []

for row in csvfile:
    highs.append(int(row[5]))

plt.plot(highs, c="red")
plt.title("Daily high temp for Sitka Alaska, July 2018", fontsize=16)
plt.xlabel("")
plt.ylabel("Temperature(F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)

plt.show()
