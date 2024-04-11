from analyseGrid import analyseGrid, updatedGrid
import random

filepath = ""


# The AI will choose a card at random
def gameAI(showcards):
    unflippedCards = [card[0] for card in showcards if card[3] == '0']

    # If there are no unflipped cards, return None
    if not unflippedCards:
        return None

    position = random.choice(unflippedCards)
   
    def rollDice(cards, position):
        result = random.randint(1, 6)

        # Initialize guess variable
        guess = None

        if result == 6:
            index = int(position)  # Convert position to an integer for indexing
            card = cards[index]
            guess = [card[0], card[1], card[2], 0]
        elif result == 1:
            index = int(position)  # Convert position to an integer for indexing
            card = cards[index]
            guess = random.choice(['rank', 'suit'])
            if guess == 'rank':
                guess = [card[0], card[1], random.choice(['H', 'D', 'C', 'S']), 0]
            else:
                guess = [card[0], random.choice(['A', 'K', 'Q', 'J', '10']), card[2], 0]
        else:
            # Handle the case where result is not 1 or 6
            # For example, you can choose a random rank and suit
            # as a fallback option
            rank = random.choice(['A', 'K', 'Q', 'J', '10'])
            suit = random.choice(['H', 'D', 'C', 'S'])
            guess = [position, rank, suit, 0]

        return guess
   
    # Call the rollDice function and assign the returned guess to the guess variable
    guess = rollDice(showcards, position)
    return guess