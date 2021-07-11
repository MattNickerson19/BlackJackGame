#!/usr/bin/env python3



FILENAME = "money.txt"

def writeFile(payOutAmount):
    try:
        with open (FILENAME, "w", newline = "") as file:
            file.write(str(payOutAmount))
    except Exception as e:
        print(type(e), e)
        

def readFile():
    try:
        moneyAmount = []
        with open(FILENAME, "r", newline = "") as file:
            money = file.readlines()
            moneyAmount.append(money)
            print("Money:\t",moneyAmount[0][0])
            return float(moneyAmount[0][0])
    except FileNotFoundError:
        print("Cound not find", FILENAME, "file")
        
    except Exception as e:
        print(type(e), e)
        





    
