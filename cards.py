import pandas as pd

def createDeckDataframe():
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    jokers = ['Joker', 'Joker', 'Joker']

    # Create a list of tuples representing all cards in the deck
    cards = [(rank, suit) for rank in ranks for suit in suits]
    cards.extend([(joker, 'Joker') for joker in jokers])

    # Create a DataFrame from the list of tuples
    deckDf = pd.DataFrame(cards, columns=['Rank', 'Suit'])

    #TODO: need to assign unique id to each card
    dictCards = {}
    for t in cards:
        key = len(dictCards)
        dictCards[key] = t

    return dictCards