# Importing libraries.
import random
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox


# Framing.
window = tk.Tk()
window.title("Spec")
window.geometry('1280x800')

frame = ttk.Frame(window)
frame.place(relx=0.5, rely=0.5, anchor='center')


#Clearing the frame.
def clearFrame():
   for widget in frame.winfo_children():
      widget.forget()


# Setting up cards and grid.
def scorecards():
   # Create scorecards
   return scorecards
def showcards():
   # Create showcards.
   return showcards
def displayGrid():
   # Generate grid.
   return displayGrid


# Game Logic a.k.a all the modules.

# Get number of players.
def numberOfPlayers():
   clearFrame()

   
   # Will set the value of n to the number of players.
   def setNumber(value):
    global n
    n = value
    return n


   button2 = ttk.Button(frame, text="2 Players", command=lambda: setNumber(2))
   button2.pack(side='left', padx=5)

   button3 = ttk.Button(frame, text="2 Players", command=lambda: setNumber(3))
   button3.pack(side='left', padx=5)

   button4 = ttk.Button(frame, text="2 Players", command=lambda: setNumber(4))
   button4.pack(side='left', padx=5)
   
   numberOfPlayers = n
   rounds = numberOfPlayers
   
   return numberOfPlayers, rounds


# Get names of players.
def nameOfPlayer(numberOfPlayers):
   clearFrame()


   # Will set the names of the players.
   def setNames():
      playerNames = []
      for name in names:
         playerNames.append(name.get())
      messagebox.showinfo("Player Names", "Player names: " + ', '.join(playerNames))
      return playerNames
   
   
   names = []
   for i in range(numberOfPlayers):
      label = ttk.Label(frame, text="Player " + str(i+1) + ": ")
      label.pack(side='top', pady=5)
      entry = ttk.Entry(frame)
      entry.pack(side='top', pady=5)
      names.append(entry)


   confirmButton = ttk.Button(frame, text="Confirm", command=setNames)
   confirmButton.pack(side='bottom', pady=5)
   return names


# Randomize the order of player names.
def randomNames(playerNames):

   random.shuffle(playerNames)
   return playerNames


# Ask for pre-round predictions and save it.
def preRoundPredictions(playerNames):
   clearFrame()
   
   ranksPredicted = set()
   suitsPredicted = set()

   preRule = ttk.Label(frame, text="Rules for Pre-Round Predictions:\n\nNominate the Ace, King, Queen, Jack, or Ten of a specific suit, or by typing ""Joker"" without mentioning a suit.\n\nNo two players may predict the same suit or the same rank or a Joker.\n\nRanks to guess from: ACE(A), KING(K), QUEEN(Q), JACK(J), 10(10), JOKER(JOKER)\nSuites to guess from: HEARTS(H), DIAMONDS(D), CLUBS(C), SPADES(S)\n\nThe guess format is:Q,H (for Queen of Hearts.)")
   preRule.pack(side='top', pady=5)

   # Set the pre-round predictions rules and check them.
   def checkPredictions(predictions):
         rank, suit = predictions.split(',')
         if rank in ['A', 'K', 'Q', 'J', 'T'] and suit in ['S', 'H', 'C', 'D']:
            if rank not in ranksPredicted:
               if suit not in suitsPredicted:
                  predictions[playerNames] = (rank, suit)
                  ranksPredicted.add(rank)
                  suitsPredicted.add(suit)
                  return True, predictions
               else:
                  return messagebox.WARNING("Another player has already predicted this suit. Please choose another prediction.")
            else:
               return messagebox.WARNING("Another player has already predicted this rank. Please choose another prediction.")
         else:
            return messagebox.WARNING("Invalid rank or suit. Please choose from 'A', 'K', 'Q', 'J', '10' for rank and 'S', 'H', 'C', 'D' for suit.")


   # Set the predictions.
   def setPredictions():
      predictions.clear()
      for name, entry in zip(playerNames, predictions):
         if not checkPredictions(predictions):
            return predictions
         else:
            predictions[name.get()] = entry.get().upper()
            return predictions


   global predictions 
   predictions = []
   for name in playerNames:
      label = ttk.Label(frame, text="Make Your Prediction: " + name.get())
      label.pack(side='top', pady=5)
      entry = ttk.Entry(frame)
      entry.pack(side='top', pady=5)
      predictions.append(entry)

   confirmButton = ttk.Button(frame, text="Confirm", command = setPredictions)
   confirmButton.pack(side='bottom', pady=5)

   return predictions


def guess():
   # Guess logic.
   return guess


def updateGrid():
   # Update the grid.
   return updateGrid


def analyzeGrid():
   # Analyze the grid.
   return analyzeGrid


def validateCallout():
   # Validate the callout.
   return validateCallout


def preRoundScoring():
   # Pre-round scoring.
   return preRoundScoring


def endRoundScoring():
   # End-round scoring.
   return endRoundScoring


def endRoundCondition():
   # End-round condition.
   return endRoundCondition   


def endRoundLast():
   # End-round last.
   return endRoundLast


# Initialization of the game a.k.a. the specMain section.
number = numberOfPlayers()
names = nameOfPlayer(number)
playerNames = randomNames(names)
preRoundPredictions(playerNames)



window.mainloop()