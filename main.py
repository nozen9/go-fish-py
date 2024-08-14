"""
Digital Ready Summer 2024
Card Game Project

Write your card game here!
"""
from card import Card
from rank import Rank
from suit import Suit
import random

def main():
    print("Write your card game here!")

deck = Card.new_deck()

# hand_size = int(5)

def playerHand():
    hand_size = 5
    playerList = []
    for i in range(hand_size):
        playerRan = random.choice(deck) #deck.pop()
        playerList.append(playerRan)
    
    print("Starter Player Hand: ", str(playerList))
    return playerList


def computerHand():
        hand_size = 5
        computerList = []
        for i in range(hand_size): 
            computerRan = random.choice(deck)
            computerList.append(computerRan)
        #checking length of computerList
        print("Length of Computer Hand: ", str(len(computerList)))
        return computerList

# Deal random set of 5 cards to player and computer 
playerList = playerHand()
computerList = computerHand()


def playGoFish():

    #calling player and computer functions
    global playerList
    global computerList

    newCard = random.choice(deck)

    print("Comp List: " + str(computerList))


    while len(deck) != 0 or len(computerList) != 0 or len(playerList) != 0:

        playerRank = int(input("Enter a card rank: "))

    # PLAYER TURN
    #if playerCard in computerList:
        cardsToBeAdded = []
        for card in computerList: 
            if playerRank == card.rank: 
                 #print(True)
                computerList.remove(card)
                # playerList.append(card)
                cardsToBeAdded.append(card)

        if len(cardsToBeAdded) == 0:
             print("Go Fish")
             playerList.append(newCard)
             print(newCard)
             print("Player Hand: ", str(playerList))
        else:
             for card in cardsToBeAdded:
                playerList.append(card)
             
        print(playerList)
        print(computerList)


    # COMPUTER TURN   
    #computer asks for a card in its list:
        computerRank = random.choice(computerList).rank
        print("Computer Rank: " + str(computerRank))
        print("Do you have a ", str(computerRank), "?")

        cardsToBeAdded = []
        for card in playerList: 
            if computerRank == card.rank: 
                 #print(True)
                playerList.remove(card)
                # playerList.append(card)
                cardsToBeAdded.append(card)

        if len(cardsToBeAdded) == 0:
             print("Go Fish")
             computerList.append(newCard)
             print(newCard)
             print("Computer Hand: ", str(computerList))
        else:
             for card in cardsToBeAdded:
                computerList.append(card)
             
        print("PlayerHand: ", str(playerList))
        print("ComputerHand: ", str(computerList))


def setsForWins():
   
    global playerHand
    global computerHand 

    computerSets = 0
    playerSets = 0
    computerListRanks = []
    playerListRanks = []

    for card in computerList:
        computerListRanks.append(card.rank)

    
    for card in playerList:
        playerListRanks.append(card.rank)


    for num in range(13):
     if playerListRanks.count(num) == 4:
        playerSets += 1
        
    for num in range(13):
        if computerListRanks.count(num) == 4:
            computerSets += 1 
           
    if playerSets > computerSets:
        print("Player Wins!")

    elif playerSets < computerSets:
        print("Computer Wins!")

    elif playerSets == computerSets:
        print("Tie.")
    
        
playGoFish()
setsForWins()


if __name__ == "__main__":
    main()
