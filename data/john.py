import matplotlib.pyplot as plt
import csv

countries = ['USA', 'Canada', 'Great Britain']
USA_johns = 0
CAN_johns = 0
GBR_johns = 0
categories = []
x_pos = [i for i, _ in enumerate(countries)]


with open('john.csv', 'r', encoding='utf8', errors='ignore') as csvfile:
	reader= csv.reader(csvfile, delimiter=',')
	line_count = 0 

	for row in reader:

		if line_count is 0: 
			categories.append(row)
			line_count += 1
		else: 
			line_count += 1
			if (row[1] == "USA"):
				USA_johns += 1
			elif (row[1] == "CAN"):
				CAN_johns += 1
			elif (row[1] == "GBR"):
				GBR_johns += 1

johns = [USA_johns, CAN_johns, GBR_johns]

plt.bar(x_pos, johns, color='blue')
plt.xlabel("Countries")
plt.ylabel("Johns")
plt.title("Number of Athletes named John winning medals 1924-2014")

plt.xticks(x_pos, countries)

plt.show()