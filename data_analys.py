import csv
from tkinter import *
import tkinterdnd2 as tkdnd

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



def csv_dnd():
    def show_text(event):
        textarea.delete("1.0","end")
        textarea.insert("end",f"{event.data}\n")
        return event.data

    root=tkdnd.Tk()
    root.title("CSV DnD")
    root.geometry('400x300')

    frame= Frame(root)
    frame.pack()

    textarea=Text(frame, height=30, width=40)
    textarea.pack(side=LEFT)

    textarea.drop_target_register(tkdnd.DND_FILES)
    textarea.dnd_bind('<<DROP>>', show_text)

    root.mainloop()

csv_dnd()