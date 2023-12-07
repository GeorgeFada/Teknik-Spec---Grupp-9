import csv

fields = []
rows = []
data = []
sum = 0
title = ""
indata_index = 0 
utdata_index = 0 

with open('data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    # title = csvreader[0]
    # fields = next(csvreader)
    for row in csvreader:
        #Visa indexen för vilken som är utdata
        #Använd array.pop för att ta bort extra kolumner emellan Indata och utdata som inte behövs.
        #Anta inte att det heter indata eller utdata ska kunna vara vad som ksk.
        indata_index = row.index("Indata")
        utdata_index = row.index("Utdata")
        # print(indata_index)
        # print(utdata_index)
        break

    # for row in csvreader:
        # title = row[0]
        # break
    # title = csvreader

    # fields = next(csvreader)
    data_titlar = next(csvreader)
    # print(data_titlar[0])
    
    # max_index = len(data_titlar) - 1
    line = 1
    for row in csvreader:
        # Hitta skillnad i index, 2 emellan betyder att det är slut
        # if utdata_index - indata_index == 2:
            # print(line, "Indata:", )
        # elif utdata_index - indata_index > 2:
        index_skillnad = utdata_index - indata_index - 1
        # for i in range(indata_index, utdata_index+1):
            # print(data_titlar)
        print(str(line) + ".", "\n" + "Indata:",)
        for i in range(indata_index, utdata_index-1):
            print(data_titlar[i] + ":", row[i])
        print("Utdata:")
        for i in range(utdata_index, len(data_titlar)):
            print(data_titlar[i] + ":", row[i])
        print("\n")
        # print("Summan av", title + ":", sum / len(data)) #Skriv "Summan av <vad datan är>:", få det ifrån csv
        line += 1

    # for row in csvreader:
        # if csvreader.in
            # title = row[0]
        # rows.append(row)
        # data.append(int(row[0]))

# for item in data:
    # sum += item

# Gör en enkel grej där printar varje rad först indatan, varje kolumn printar titeln för datan och vad den är, sedan utdatan för den raden
# <radnummer> Indata: Titel: <värde> (osv), Utdata: Titel:
# print("Summan av", title + ":", sum / len(data)) #Skriv "Summan av <vad datan är>:", få det ifrån csv
