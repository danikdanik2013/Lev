#!/usr/bin/python3
import csv

x = '7.csv'
word_input2 = input("Do you want to watch all list?(yes/no)")
if word_input2 == "yes":
    with open ( x , 'r' , newline = '' ) as f:
        file = csv.reader(f)
        for row in file:
            a = row[0]
            print("{}".format(a))
        word_input = input("Do you want get more information about this car?(yes/no)")
        if word_input == "yes":
            for row in file:
                car_input = input("Model is: ")
                a = row[0]
                b = row[1]
                if car_input == row[0]:
                    print ("{} - {}".format(a, b))
                    break
        else:
            print("12")



# input_sorted = input("Yes/No?: ")
# if input_sorted == "Yes":
#     sortedlist = sorted(x, key=lambda row: (row[1],row[0],row[2]), reverse=True)
# else:
#     print (" okey...")
# word_input = input("Model is: ")
#         a = row[0]
#         b = row[1]
#         if word_input == row[0]:
#             print ("{} - {}".format(a, b))
#             continue