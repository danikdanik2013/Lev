#!/usr/bin/python3
import csv
import pandas as pd

x = '7.csv'
word_input2 = input("Do you want to watch all list?(yes/no) - ")
if word_input2 == "yes":
    with open ( x , 'r' , newline = '' ) as f:
        file = csv.reader(f)
        for row in file:
            a = row[0]
            print("{}".format(a))
        f.close()
    sort_input = input("Do you want to sorted list?(yes/no) ")
    if sort_input == "yes":
        with open(x, 'r', newline='') as f:
            file = csv.reader(f)
            df = pd.DataFrame(f)
            for row in file:
                print(df.sort_values('Alphabet'))
                # break
    else:
        print("NOPE")
    f.close()
    word_input = input("Do you want get more information about this car?(yes/no) - ")
    if word_input == "yes":
            with open(x, 'r', newline='') as f:
                file = csv.reader(f)
                car_input = input("Model is: ")
                for row in file:
                    a = row[0]
                    b = row[1]
                    if car_input == row[0]:
                        print ("{} - {}".format(a, b))
                        break
    else:
            print("OOOPS")
def sortByAlphabet(inputStr):
                return inputStr[0]

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