import pandas as pd
import random
numberOfPlayers = 2

file_path = ""

def preRoundPredictions(name):
    # Displaying the rules.
    print("Rules for Pre-Round Predictions:\nPredictions are made by each player, in turn, nominating the Ace, King, Queen, Jack, or Ten of a specific suit, or by announcing 'Joker' without mentioning a suit.\nNo two players may predict the same suit or the same rank or a Joker.")
    print("Ranks to guess from: ACE(A), KING(K), QUEEN(Q), JACK(J), 10(10), JOKER(JOKER)")
    print("Suites to guess from: HEARTS(H), DIAMONDS(D), CLUBS(C), SPADES(S)")
    print("The guess format is:Q,H (for Queen of Hearts.)")
    # Saving the pre-round predictions.
    predictions = {}
    # Defining sets to keep track of predicted ranks and suits.
    ranksPredicted = set()
    suitsPredicted = set()

    while True:
        prediction = input(f"{name}, make your prediction (e.g., 'Q,H' for Queen of Hearts or 'Joker'): ").strip().upper()

        # Applying all the pre-round prediction rules.
        # The rules are mentioned in this file on line 9.
        if prediction == 'JOKER':
            if 'JOKER' not in predictions.values():
                predictions[name] = prediction
                break
            else:
                print("Another player has already predicted Joker. Please choose another prediction.")
        else:
            rank, suit = prediction.split(',')
            if rank in ['A', 'K', 'Q', 'J', '10'] and suit in ['S', 'H', 'C', 'D']:
                if rank not in ranksPredicted:
                    if suit not in suitsPredicted:
                        predictions[name] = (rank, suit)
                        ranksPredicted.add(rank)
                        suitsPredicted.add(suit)
                        break
                    else:
                        print("Another player has already predicted this suit. Please choose another prediction.")
                else:
                    print("Another player has already predicted this rank. Please choose another prediction.")
            else:
                print("Invalid rank or suit. Please choose from 'A', 'K', 'Q', 'J', '10' for rank and 'S', 'H', 'C', 'D' for suit.")
    return predictions

def aiPredictions(AI, humanPrediction):
    # Defining sets to keep track of predicted ranks and suits.
    ranksPredicted = set()
    suitsPredicted = set()
    predictions = {}
    while True:
        prediction = random.choice(['A', 'K', 'Q', 'J', '10']) + ',' + random.choice(['S', 'H', 'C', 'D']) or "JOKER"
        if prediction == 'JOKER':
            if 'JOKER' not in humanPrediction.values():
                predictions[AI] = prediction
                break
        else:
            rank, suit = prediction.split(',')
            if rank in ['A', 'K', 'Q', 'J', '10'] and suit in ['S', 'H', 'C', 'D']:
                if rank not in ranksPredicted:
                    if suit not in suitsPredicted:
                        predictions[AI] = (rank, suit)
                        ranksPredicted.add(rank)
                        suitsPredicted.add(suit)
                        break
    return predictions