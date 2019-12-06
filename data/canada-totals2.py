import matplotlib.pyplot as plt
import csv

years = [1928, 1932, 1936, 1948, 1952, 1956, 1960, 1964, 1968, 1972, 1976, 1980, 1984, 1988, 1992, 1994, 1998, 2002, 2006, 2010, 2014]
medalCount=[] 
categories = []

with open('canada-totals.csv', 'r', encoding='utf8', errors='ignore') as csvfile:
	reader= csv.reader(csvfile, delimiter=',')
	line_count = 0 

	for row in reader:

		if line_count is 0: 
			categories.append(row)
			line_count += 1
		else: 
			line_count += 1
			if line_count <= 22:
				medalCount.append(row[2])

x_pos = [i for i, _ in enumerate(years)]

plt.bar(x_pos, medalCount, color='blue')
plt.xlabel("Years")
plt.ylabel("Medals")
plt.title("Total Number of Medals Won by Canada 1924-2014")
plt.xticks(x_pos, years)

plt.show()

