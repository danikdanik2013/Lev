#!/usr/bin/python3
import csv

x = '7.csv'
vvod = input("Model is: ")
with open ( x , 'r' , newline = '' ) as f:
        file = csv.reader(f)
        for row in file:
            if vvod == "Porsche 911":
                print (vvod,'-',row[1])
                break
            elif vvod == "Porsche 918":
                print (row[2])
                break
            elif vvod == "Porsche 906":
                print (row[3])
                break
            else:
                print("UNCORRECTS")
                break
# input_sorted = input("Yes/No?: ")
# if input_sorted == "Yes":
#     sortedlist = sorted(x, key=lambda row: (row[1],row[0],row[2]), reverse=True)
# else:
#     print (" okey...")