#!/usr/bin/env python3
import csv 


FILENAME = "money.csv"

def writeFile(moneyAmount):
    try:
        with open (FILENAME, "w", newline = "") as file:
            writer = csv.writer(file)
            writer.writerows(moneyAmount)
    except Exception as e:
        print(type(e), e)
        

def readFile():
    try:
        moneyAmount = []
        with open(FILENAME, "r", newline = "") as file:
            reader = csv.reader(file)
            for row in reader:
                moneyAmount.append(row)
            print("Money:\t",moneyAmount[0][0])
            return int(moneyAmount[0][0])
    except FileNotFoundError:
        print("Cound not find", FILENAME, "file")
        
    except Exception as e:
        print(type(e), e)
        





    
