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

labels = ("Canada", "USA", "Soviet Union")
# sizes are how many and how large the slices of the pie chart will be 
sizes = [CAN_medalCount, USA_medalCount, URS_medalCount]
colors = ['red', 'blue', 'yellow']
explode = (0, 0.1, 0)

plt.pie(sizes, explode=explode, colors=colors, autopct='%.1f%%', shadow=True, startangle=140)
plt.axis('equal')

plt.legend(labels, loc=1)
plt.title("Total Medals Won in Ice Hockey for Top 3 Countries since 1924")
plt.show()