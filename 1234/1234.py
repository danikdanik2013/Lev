#!/usr/bin/python3
import csv

x = '7.csv'
word_input2 = input( "Do you want to watch all list?(yes/no) - " )
if word_input2 == "yes":
    with open ( x , 'r', newline = '' ) as f:
        file = csv.reader(f)
        a = []
        for row in file:
            b = row[0]
            print( "{}".format(b) )
            a.append(b)
        sort_input = input( "Do you want to sorted list?(yes/no) " )
        if sort_input == "yes":
            newList = sorted(a)
            print("{}".format(newList))
            f.close()
        else:
            print("OOOPS")
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

else:
    print("OOOPS")
