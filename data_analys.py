import csv
import argparse
import os.path

parser = argparse.ArgumentParser()
parser.add_argument("filename", nargs='?', help="the source csv file containing the data")
args = parser.parse_args()

def check_extension(filename):
    filename_extension = os.path.splitext(filename)[1]
    if filename_extension != ".csv":
        print("The file", "\"" + filename + "\"", "is not a csv file.")
        parser.print_help()
        exit()

if args.filename:
    #todo kolla om extension är .csv
    if not os.path.exists(args.filename): #Om inte hittar fil:
        print("Could not open", "\"" + os.path.basename(args.filename) + "\"" + ", no such file or directory.")
        parser.print_help()
        exit()
    else:
        check_extension(os.path.basename(args.filename))
        csv_file = args.filename
else:
    pass
    exit("Drag")
    #HÄR KÖRS DRAG AND DROP
    #csv_file = file

with open(csv_file, 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    indata_index = 0 
    utdata_index = 0 

    #Spara indexer för var indatan respektive utdatan börjar
    # print(csvreader)
    # exit()
    for row in csvreader:
        #ksk ta bort extra kolumner emellan Indata och utdata som inte behövs.
        #Anta inte att det heter indata eller utdata ska kunna vara vad som ksk.
        indata_index = row.index("Indata")
        utdata_index = row.index("Utdata")
        break

    data_titles = next(csvreader)
    
    data_dict = dict(Indata = [], Utdata = []) #Spara allt i en dictionary

    #Lägg in data titlarna först
    for i in range(indata_index, utdata_index-1):
        array = []
        array.append(data_titles[i])
        array.append([])
        data_dict["Indata"].append(array)
    for i in range(utdata_index, len(data_titles)):
        array = []
        array.append(data_titles[i])
        array.append([])
        data_dict["Utdata"].append(array)

    for row in csvreader:
        for i in range(indata_index, utdata_index-1):
            data_dict["Indata"][i][1].append(row[i])
        num = 0
        for i in range(utdata_index, len(data_titles)):
            data_dict["Utdata"][num][1].append(row[i])
            num += 1
    # print(data_dict)
    # exit()

    #Printa ut för varje rad i csv filen de olika kolumnernas värde, vad för typ av värde, samt om det är indata/utdata
    # <radnummer> Indata: Titel: <värde> (osv), Utdata: Titel:
    # for i in range(len(data_dict["Utdata"][0][1])):
    dict_indata = data_dict["Indata"]
    dict_utdata = data_dict["Utdata"]
    for i in range(len(data_dict["Utdata"][0][1])):
        print(str(i + 1) + ".")
        print("Indata:")
        for item in dict_indata:
            print(item[0] + ":", item[1][i])
        print("Utdata:")
        for item in dict_utdata:
            print(item[0] + ":", item[1][i])
        print("") #Nyrad
