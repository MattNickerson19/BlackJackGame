#!/usr/bin/env python3

import csv
import random

def displayMenu():
    print("BLACKJACK!")
    print("BlackJack payout is 3:2")
    

def dealerHand(deck):
    dealerHand = []
    dealCard = random.randint(0,len(deck)-1)
    dealerCard = deck[dealCard]
    dealerHand.append(dealerCard)
    print("\nDEALER'S SHOW CARD:")
    for card in dealerHand:
            print(card[0],"of", card[1])
    

def playerHand(deck):
    playerHand = []
    
    i = 0
    while i < 2:
        dealCard = random.randint(0,len(deck)-1)
        playerCard = deck[dealCard]
        playerHand.append(playerCard)
        i += 1
    print("\nPLAYER'S CARDS:")
    for card in playerHand:
            print(card[0],"of", card[1])
            
    playerMove = input("\nHit or Stand? (hit/stand):  ")
    while True:
        
        if playerMove.lower() == "hit":
            dealCard = random.randint(0,len(deck)-1)
            playerCard = deck[dealCard]
            playerHand.append(playerCard)
            print("\nPLAYER'S CARDS:")
            for card in playerHand:
                print(card[0],"of", card[1])
            playerMove = input("\nHit or Stand? (hit/stand):  ")

        elif playerMove.lower() == "stand":
            break
        
        else:
            print("Not valid Entry")
            playerMove = input("\nHit or Stand? (hit/stand):  ")


def playGame():
    pass

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


def main():
    deck = [["1","hearts",1],["1","diamonds",1],["1","clubs",1],["1","spades",1],
                  ["2","hearts",2], ["2","diamonds",1],["2","clubs",1],["2","spades",2],
                  ["3","hearts",3], ["3","diamonds",1],["3","clubs",1],["3","spades",3],
                  ["4","hearts",4], ["4","diamonds",1],["4","clubs",1],["4","spades",4],
                  ["5","hearts",5], ["5","diamonds",1],["5","clubs",1],["5","spades",5],
                  ["6","hearts",6], ["6","diamonds",1],["6","clubs",1],["6","spades",6],
                  ["7","hearts",7], ["7","diamonds",1],["7","clubs",1],["7","spades",7],
                  ["8","hearts",8], ["8","diamonds",1],["8","clubs",1],["8","spades",8],
                  ["9","hearts",9], ["9","diamonds",1],["9","clubs",1],["9","spades",9],
                  ["10","hearts",10],["10","diamonds",1],["10","clubs",1],["10","spades",10],
                  ["Jack","hearts",10],["Jack","diamonds",1],["Jack","clubs",1],["Jack","spades",10],
                  ["Queen","hearts",10],["Queen","diamonds",1],["Queen","clubs",1],["Queen","spades",10],
                  ["King","hearts",10],["King","diamonds",1],["King","clubs",1],["King","spades",10],
                  ["Ace","hearts",1,11],["Ace","diamonds",1,11],["Ace","clubs",1,11],["Ace","spades",1,11]]

    displayMenu()
    moneyAmount = readFile()
    dealerHand(deck)
    playerHand(deck)
    
    

if __name__ == "__main__":
    main()
