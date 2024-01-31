import pandas as pd

def create_deck_dataframe():
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    jokers = ['Joker', 'Joker', 'Joker']

    # Create a list of tuples representing all cards in the deck
    cards = [(rank, suit) for rank in ranks for suit in suits]
    cards.extend([(joker, 'Joker') for joker in jokers])

    # Create a DataFrame from the list of tuples
    deck_df = pd.DataFrame(cards, columns=['Rank', 'Suit'])

    #TODO: need to assign unique id to each card
    dict_cards = {}
    for t in cards:
        key = len(dict_cards)
        dict_cards[key] = t

    return dict_cards

