# Description: This file contains the function that will be called when it is the player's turn to guess.
from validateCallout import validate_callouts


def guess(names, updatedGrid):
    print("Rules for guessing:")  # Add the playing rules.
    print("Ranks to guess from: ACE(A), KING(K), QUEEN(Q), JACK(J), 10(10), JOKER(JOKER)")
    print("Suites to guess from: HEARTS(H), DIAMONDS(D), CLUBS(C), SPADES(S)")
    print(f"The guess format is: 25 Q,H (for card no. 25, Queen of Hearts.\n)")
    print(f"The invalid callout format is: Callout\n)")

    rankMap = {"A": "ACE", "K": "KING", "Q": "QUEEN", "J": "JACK", "10": "10", "JOKER": "JOKER"}
    suitMap = {"H": "HEARTS", "D": "DIAMONDS", "C": "CLUBS", "S": "SPADES", "JOKER": "JOKER"}

    # names is the current player
    currentPlayer = names

    # while True:
    # Taking input from the player for their call
    userInput = input(f"Make your call {currentPlayer}: ")

    # Check if the user input is "Callout"
    if userInput.upper() == "CALLOUT":
        validate_callouts()
    else:
        # Spliting the input into row, column, and guess
        try:
            position, guess = map(str.strip, userInput.split())
            position = int(position)
            guess = list(map(str.strip, guess.split(',')))  # Convert to list and split by comma
            rank = guess[0].upper()

            if rank == "JOKER":
                suit = "JOKER"
            else:
                suit = guess[1].upper()

            if not (1 <= position <= 25):
                print("Invalid position. Please choose values between 1 and 25.")

            # Check if the rank is valid
            rank = rankMap.get(rank)  # Convert user input to full rank
            if rank not in rankMap.values():
                print("Invalid rank. Please choose a valid rank.")

            # Check if the rank is valid
            suit = suitMap.get(suit)  # Convert user input to full suit
            if suit not in suitMap.values():
                print("Invalid suit. Please choose a valid suit.")

            for card in updatedGrid:
                if card[0] == guess[0]:  # If the position matches
                    if card[3] == 0:  # If the card is unflipped
                        print("Card already flipped. Please choose another card.")

        except ValueError:
            print("Invalid input format. Please try again.")

    n = str(position)
    guess = [n, rank, suit, '0']
    return guess, currentPlayer  # Return the guess and the last player.
