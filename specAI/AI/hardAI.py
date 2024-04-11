import random

def rollDice(cards, position):
    # Perform the first coin toss
    toss1 = random.randint(0, 1)

    # Initialize guess variable
    guess = None

    if toss1 == 1:
        # If toss1 is 1, the computer guesses the correct card (correct rank and suit)
        index = int(position)  # Convert position to an integer for indexing
        card = cards[index]
        guess = [card[0], card[1], card[2], 0]
    else:
        # If toss1 is 0, the computer gets another chance
        # Perform the second coin toss
        toss2 = random.randint(0, 1)
        if toss2 == 1:
            # If toss2 is 1, the computer guesses either the correct rank or suit
            index = int(position)  # Convert position to an integer for indexing
            card = cards[index]
            guess = random.choice(['rank', 'suit'])
            if guess == 'rank':
                guess = [card[0], card[1], random.choice(['H', 'D', 'C', 'S']), 0]
            else:
                guess = [card[0], random.choice(['A', 'K', 'Q', 'J', '10']), card[2], 0]
        else:
            # If toss2 is 0, the computer guesses a random rank and suit
            rank = random.choice(['A', 'K', 'Q', 'J', '10'])
            suit = random.choice(['H', 'D', 'C', 'S'])
            guess = [position, rank, suit, 0]

    return guess

def gameAI(showcards):
    # Filter unflipped cards
    unflippedCards = [card for card in showcards if card[3] == '0']

    # If there are no unflipped cards, return None
    if not unflippedCards:
        return None

    # Choose a random unflipped card
    chosenCard = random.choice(unflippedCards)

    # Create a guess based on the chosen card
    position = chosenCard[0]
    rank = chosenCard[1]
    suit = chosenCard[2]
    guess = [position, rank, suit, 0]
    
    return guess
