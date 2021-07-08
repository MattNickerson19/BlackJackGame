#!/usr/bin/env python3

import csv
import random
import db

def displayMenu():
    print("BLACKJACK!")
    print("BlackJack payout is 3:2")

def playGame(deck):
#DEALER HAND
    dealerHand = []

    dealerValue = 0
    while True:
        if dealerValue < 17:
            dealCard = random.randint(0,len(deck)-1)
            dealerCard = deck[dealCard]
            dealerHand.append(dealerCard)
            dealerValue = 0
            for card in dealerHand:
                dealerValue += int(card[2])
        elif dealerValue >= 17:
            break
               
        
    print("\nDEALER'S SHOW CARD:")
    print(dealerHand[0][0], "of", dealerHand[0][1])

    
#PLAYER HAND
    playerHand = []

    playerValue = 0
    i = 0
    while i < 2:
        dealCard = random.randint(0,len(deck)-1)
        playerCard = deck[dealCard]
        playerHand.append(playerCard)
        i += 1
    print("\nPLAYER'S CARDS:")
    for card in playerHand:
            print(card[0],"of", card[1])
            playerValue += int(card[2])
    playerMove = input("\nHit or Stand? (hit/stand):  ")

    while True:
        try:
            if playerMove.lower() == "hit":
                dealCard = random.randint(0,len(deck)-1)
                playerCard = deck[dealCard]
                playerHand.append(playerCard)
                
                print("\nPLAYER'S CARDS:")
                playerValue = 0
                for card in playerHand:
                    print(card[0],"of", card[1])
                    playerValue += int(card[2])
                if playerValue > 21:
                    break
                else:
                    playerMove = input("\nHit or Stand? (hit/stand):  ")
                    

            elif playerMove.lower() == "stand":
                break
            
            else:
                print("Not valid Entry")
                playerMove = input("\nHit or Stand? (hit/stand):  ")
        except ValueError:
            print("Invalid Entry")


#SHOW DEALER HAND AND POINTS
    print("\nDEALER'S CARDS")
    for card in dealerHand:
            print(card[0],"of", card[1])

    print("\nYOUR POINTS:\t", playerValue)
    print("DEALER'S POINTS:\t", dealerValue)

#DETERMINE WINNER
    playerWins = False
    if playerValue > 21:
        print("\nYOU BUSTED.")
        moneyAmount = db.readFile()
        return playerWins

    elif dealerValue > 21 and playerValue <= 21:
        print("\nDealer busts. You win,")
        playerWins = True
        moneyAmount = db.readFile()
        return playerWins

    elif playerValue <= 21 and playerValue > dealerValue:
        print("\nCongrats. You win")
        playerWins = True
        moneyAmount = db.readFile()
        return playerWins

    elif dealerValue <= 21 and dealerValue > playerValue:
        print("\nSorry. You lose")
        moneyAmount = db.readFile()
        return playerWins

    elif playerValue <= 21 and playerValue == dealerValue:
        print("\nTie. Bets returned")


def main():
    deck = [["2","hearts",2], ["2","diamonds",2],["2","clubs",2],["2","spades",2],
                  ["3","hearts",3], ["3","diamonds",3],["3","clubs",3],["3","spades",3],
                  ["4","hearts",4], ["4","diamonds",4],["4","clubs",4],["4","spades",4],
                  ["5","hearts",5], ["5","diamonds",5],["5","clubs",5],["5","spades",5],
                  ["6","hearts",6], ["6","diamonds",6],["6","clubs",6],["6","spades",6],
                  ["7","hearts",7], ["7","diamonds",7],["7","clubs",7],["7","spades",7],
                  ["8","hearts",8], ["8","diamonds",8],["8","clubs",8],["8","spades",8],
                  ["9","hearts",9], ["9","diamonds",9],["9","clubs",9],["9","spades",9],
                  ["10","hearts",10],["10","diamonds",10],["10","clubs",10],["10","spades",10],
                  ["Jack","hearts",10],["Jack","diamonds",10],["Jack","clubs",10],["Jack","spades",10],
                  ["Queen","hearts",10],["Queen","diamonds",10],["Queen","clubs",10],["Queen","spades",10],
                  ["King","hearts",10],["King","diamonds",10],["King","clubs",10],["King","spades",10],
                  ["Ace","hearts",1,11],["Ace","diamonds",1,11],["Ace","clubs",1,11],["Ace","spades",1,11]]

    displayMenu()
    print()
    
    playAgain = "y"
    while playAgain.lower() == "y":
        moneyAmount = db.readFile()
        betAmount = float(input("Bet:\t"))
        playerWins = playGame(deck)
        if playerWins == True:
            payOutAmount = round((betAmount *1.5) + moneyAmount,2)
            print(payOutAmount)
        else:
            payOutAmount = round(betAmount - (2 * betAmount) + moneyAmount,2)
            print(payOutAmount)

        bankAccount = str(payOutAmount)
        db.writeFile(bankAccount)
        playAgain = input("\nPlay again? (y/n):  ")
    print("Come back soon")
    
   



if __name__ == "__main__":
    main()
