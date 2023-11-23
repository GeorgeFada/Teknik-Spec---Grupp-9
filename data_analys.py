import csv
import matplotlib.pyplot as plt
import numpy as np

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
       sum += i

    print(sum / len(data))

    x = []
    y = []

def heightchart():
    with open('data.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')

        for row in plots:
            x.append(row[0])
            y.append(str(row[0]))

    plt.bar(x, y, color='g', width=0.5, label="Höjd (cm)")
    plt.xlabel('Tid')
    plt.ylabel('Höjd (cm)')
    plt.title('Växt diagram')
    plt.legend()
    plt.show()

heightchart()
