import pandas as pd
from numberOfPlayers import numberOfPlayers

file_path = ""

def takePreRoundGuess(players, names):
   # Displaying the rules.
   print("Rules for Pre-Round Predictions:\nPredictions are made by each player, in turn, nominating the Ace, King, Queen, Jack, or Ten of a specific suit, or by announcing ""Joker"" without mentioning a suit.\n No two players may predict the same suit or the same rank or a Joker.")
   print("You can choose ranks from Ace(A), King(K), Queen(Q), Jack(J),Ten(T)")
   print("You can choose suits from Spade(S), Heart(H), Club(C), Diamond(D)")
   
   # Saving the pre-round predictions.
   predictions = {}
   # Defining sets to keep track of predicted ranks and suits.
   ranksPredicted = set()
   suitsPredicted = set()

   for player in names:
        while True:
            prediction = input(f"{player}, make your prediction (e.g., 'Q,H' for Queen of Hearts or 'Joker'): ").strip().upper()

            # Applying all the pre-round prediction rules.
            # The rules are mentioned in this file on line 9.
            if prediction == 'JOKER':
                if 'JOKER' not in predictions.values():
                    predictions[player] = prediction
                    break
                else:
                    print("Another player has already predicted Joker. Please choose another prediction.")
            else:
                rank, suit = prediction.split(',')
                if rank in ['A', 'K', 'Q', 'J', 'T'] and suit in ['S', 'H', 'C', 'D']:
                    if rank not in ranksPredicted:
                        if suit not in suitsPredicted:
                            predictions[player] = (rank, suit)
                            ranksPredicted.add(rank)
                            suitsPredicted.add(suit)
                            break
                        else:
                            print("Another player has already predicted this suit. Please choose another prediction.")
                    else:
                        print("Another player has already predicted this rank. Please choose another prediction.")
                else:
                    print("Invalid rank or suit. Please choose from 'A', 'K', 'Q', 'J', 'T' for rank and 'S', 'H', 'C', 'D' for suit.")
   
   return predictions