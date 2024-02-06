# Description: This file contains the function that will be called when it is the player's turn to play.
from numberOfPlayers import numberOfPlayers
from analyseGrid import updatedGrid

def guess(player,roundscore, updatedGrid):
    while True:
    # Taking input from the player for their call
        userInput = input("Make your call (e.g., '25 Q,H' for the 25th card and guess Queen of Hearts): ")

        # Spliting the input into row, column, and guess
        try:
            position, guess = map(str.strip, userInput.split())
            position = int(position)
            guess = list(map(str.strip, guess.split(',')))  # Convert to list and split by comma
            row = guess[0].upper()
            col = guess[1].upper()
            
            if not (1 <= position <= 25):
                print("Invalid position. Please choose values between 1 and 25.")
                continue

            # Check if the input is valid
            if row not in ["JOKER", "K", "Q", "J", "A", "10"]:
                print("Invalid rank. Please choose a valid rank.")
                continue

            if col not in ["C","D","H","S"]:
                print("Invalid suit. Please choose a valid suit.")
                continue

            #if checkCard == "flipped":
                #print("Card already flipped. Please choose another card.")
                #continue

        except ValueError:
            print("Invalid input format. Please try again.")
            continue
        break

    guess = [position, row, col]
    return guess

#Need to check this logic to make sure it works.
def checkCard(updatedGrid, guess):
    for card in updatedGrid:
        if card[0] == guess[0]:  # If the position matches
            if card[3] == 0:  # If the card is unflipped
                return "Unflipped"
            else:  # If the card is flipped
                return "Flipped"
    return "Position not found"  # If no matching position is found


def checkGuess(updatedGrid, guess):
    score = 0
    for card in updatedGrid:
        if card[0] == guess[0]:  # If the position matches
            if card[1] == guess[1] and card[2] == guess[2]:  # If the suit and rank match
                score = 4  # Exact card guessed
            elif card[1] == guess[1]:  # If only the suit matches
                score = 1  # Card of the same suit
                if card[2] == "JOKER":  # If the card is a Joker of the suit called
                    score = 2  # Joker of the suit called
            elif card[2] == guess[2]:  # If only the rank matches
                score = 2  # Card of the same rank
            if card[2] == "JOKER" and card[1] == "JOKER":  # If the card is the real Joker
                score = 4  # Real Joker guessed
            break  # Exit the loop as the card has been found
    return score  # Return the score

#Incomplete code. please dont change anything here.


# Test the playerTurn function
# player = "John"
# roundscore = 0
# inp = guess(player, roundscore)
# print(inp)
