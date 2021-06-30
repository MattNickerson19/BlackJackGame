#!/usr/bin/env python3


def writeFile(moneyAmount):
    with open ("money.csv", "w", newline = "") as file:
            writer = csv.writer(file)
            writer.writerows(moneyAmount)

def readFile():
        with open("money.csv", "r", newline = "") as file:
            moneyAmount = []
            reader = csv.reader(file)
            for row in reader:
                moneyAmount.append(row)
            return moneyAmount
