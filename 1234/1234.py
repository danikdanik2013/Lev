#!/usr/bin/python3
import csv

x = '7.csv'

vvod = input("Model is: ")
with open ( x , 'r' , newline = '' ) as f:
        file = csv.reader(f)
        for row in file:
            if vvod == "Porsche 911":
                print ( row[0])
            elif vvod == "Porsher 918":
                print (row[1])
            elif vvod == "Porsche 906":
                print (row[2])
            else:
                print("UNCORRECT")
# input_sorted = input("Yes/No?: ")
# if input_sorted == "Yes":
#     sortedlist = sorted(x, key=lambda row: (row[1],row[0],row[2]), reverse=True)
# else:
#     print (" okey...")
# def aaa():
#     with open ( x , 'r' , newline = '' ) as f:
#         file = csv.reader(f)
#         for row in file:
#             print ( row[0])
#             return (row[0])
# def bbb():
#     with open ( x , 'r' , newline = '' ) as f:
#         file = csv.reader(f)
#         for row in file:
#             print ( row[1])
#             return (row[1])
# def ccc():
#     with open ( x , 'r' , newline = '' ) as f:
#         file = csv.reader(f)
#         for row in file:
#             print ( row[2])
#   ..          return ( row [2])
