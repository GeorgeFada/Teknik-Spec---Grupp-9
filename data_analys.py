import csv
import tkinter

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

for item in data:
    sum += item

print("Summan av:", sum / len(data)) #Skriv "Summan av <vad datan är>:", få det ifrån csv

DA = tkinter.Tk()

DA.mainloop()
