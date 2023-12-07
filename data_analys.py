import csv
import matplotlib.pyplot as plt

fields = []
rows = []

data = []
sum = 0

with open('data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    fields = next(csvreader)
    fields = next(csvreader)


    for row in csvreader:
        rows.append(row)

        data.append(int(row[0]))

    for i in data:
       sum += i

    x = []
    y = []


def sunhourchartheight():
    with open('data.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')

        for row in plots:
            x.append(row[0])
            y.append(str(row[0]))

    plt.bar(x, y, color='g', width=0.5, label="Höjd (cm)")
    plt.xlabel('Soltimmar (h)')
    plt.ylabel('Höjd (cm)')
    plt.title('Växt diagram')
    plt.legend()
    plt.show()

def sunhourchartmass():
    with open('data.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')

        for row in plots:
            x.append(row[0])
            y.append(str(row[3]))

    plt.bar(x, y, color='g', width=0.5, label="Massa (g)")
    plt.title('Växt diagram')
    plt.legend()
    plt.show()

graph_input = str(input('soltimmarhöjd\nsoltimmarmassa\nVilken typ av data vii du se? '))
if graph_input == 'soltimmarhöjd':
    sunhourchartheight()
elif graph_input == 'soltimmarmassa':
    sunhourchartmass()

