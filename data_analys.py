import csv

fields = []
rows = []

data = []
sum = 0

with open('data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    fields = next(csvreader)

    for row in csvreader:
        rows.append(row)

        data.append(int(row[0]))

for i in data:
   sum += data[i]

#print(sum / len(data))