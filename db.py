#!/usr/bin/env python3
import csv as file
import sys

FILENAME = "money.csv"

def writeFile(moneyAmount):
    try:
        with open ("money.csv", "w", newline = "") as file:
            writer = csv.writer(file)
            writer.writerows(moneyAmount)
    except Exception as e:
        print(type(e), e)
        exitProgram()

def readFile():
        try:
            with open("money.csv", "r", newline = "") as file:
            moneyAmount = []
            reader = csv.reader(file)
            for row in reader:
                moneyAmount.append(row)
            return moneyAmount
        except FileNotFoundError:
            print("Cound not find", FILENAME, "file")
            exitProgram()
        except Exception as e:
            print(type(e), e)
            exitProgram()

def exitProgram ():
    print("Terminating program.")
    eye.exit()

    
