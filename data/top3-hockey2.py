import matplotlib.pyplot as plt
import csv

CAN_medalCount=0
USA_medalCount=0 
URS_medalCount=0 
categories = []

with open('top-3-hockey.csv', 'r', encoding='utf8', errors='ignore') as csvfile:
	reader= csv.reader(csvfile, delimiter=',')
	line_count = 0 

	for row in reader:

		if line_count is 0: 
			categories.append(row)
			line_count += 1
		else: 
			line_count += 1
			if (row[0] == "CAN"):
				CAN_medalCount += 1
			if (row[0] == "USA"):
				USA_medalCount += 1
			if (row[0] == "URS"):
				URS_medalCount += 1

countries = ['USA', 'Canada', 'Soviet Union']
medals = [CAN_medalCount, USA_medalCount, URS_medalCount]
x_pos = [i for i, _ in enumerate(countries)]

plt.bar(x_pos, medals, color='blue')
plt.xlabel("Countries")
plt.ylabel("Total Medals")
plt.title("Total Numbers of Ice Hockey Medals Won by Top 3 Countries 1924-2014")
plt.xticks(x_pos, countries)

plt.show()