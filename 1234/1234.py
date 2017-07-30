#!/usr/bin/python3
import csv

x = '7.csv'
word_input = input("Model is: ")
with open ( x , 'r' , newline = '' ) as f:
    file = csv.reader(f)
    for row in file:
        a = row[0]
        b = row[1]
        if word_input == row[0]:
            print ("{} - {}".format(a, b))

# input_sorted = input("Yes/No?: ")
# if input_sorted == "Yes":
#     sortedlist = sorted(x, key=lambda row: (row[1],row[0],row[2]), reverse=True)
# else:
#     print (" okey...")