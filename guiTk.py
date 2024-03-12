import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox

noOfplayers = 0

window = tk.Tk()

window.title("Spec")

window.geometry('1280x800')

frame = ttk.Frame(window)
frame.place(relx=0.5, rely=0.5, anchor='center')

gameScores = {}
nameEntries = []
predictions = {}
predictionEntries = []


def clearFrame():
    for widget in frame.winfo_children():
        widget.forget()

def validatePredictions(prediction):
    validRanks = ['A', 'K', 'Q', 'J', '10']
    validSuites = ['H', 'D', 'C', 'S']
    if prediction.upper() == 'JOKER':
        return True
    
    parts = prediction.split(',')
    if len(parts) != 2:
        return False
    
    rank, suit = parts
    if rank.upper() not in validRanks or suit.upper() not in validSuites:
        return False
    
    if prediction.upper() in predictions.values():
        return False

    if any(pred.split(',')[0].upper() == rank.upper() and pred.split(',')[1].upper() == suit.upper() for pred in predictions.values()):
        return False

    return True


def setPredictions():
    predictions.clear()
    for name, entry in zip(nameEntries, predictionEntries):
        if not validatePredictions(entry.get().upper()):
            messagebox.showerror("Invalid Prediction", "Invalid Prediction: " + entry.get() + " by " + name.get() + ". Please try again.")
            return
        predictions[name.get()] = entry.get().upper()
    print(predictions)

def preRoundPredictions():
    clearFrame()
    for name in nameEntries:
        label = ttk.Label(frame, text="Make Your Prediction: " + name.get())
        label.pack(side='top', pady=5)
        entry = ttk.Entry(frame)
        entry.pack(side='top', pady=5)
        predictionEntries.append(entry)
    
    preRule = ttk.Label(frame, text="Rules for Pre-Round Predictions:\n\nNominate the Ace, King, Queen, Jack, or Ten of a specific suit, or by typing ""Joker"" without mentioning a suit.\n\nNo two players may predict the same suit or the same rank or a Joker.\n\nRanks to guess from: ACE(A), KING(K), QUEEN(Q), JACK(J), 10(10), JOKER(JOKER)\nSuites to guess from: HEARTS(H), DIAMONDS(D), CLUBS(C), SPADES(S)\n\nThe guess format is:Q,H (for Queen of Hearts.)")
    preRule.pack(side='top', pady=5)
    confirmButton = ttk.Button(frame, text="Confirm", command = setPredictions)
    confirmButton.pack(side='bottom', pady=5)

def setNames():
    #nameEntries.shuffle()
    playerNames = []
    for name in nameEntries:
        playerNames.append(name.get())
        gameScores[name.get()] = 0
    #messagebox.showinfo("Player Names", "Player names: " + ', '.join(playerNames))
    preRoundPredictions()

def setPlayers(num):
    global noOfplayers
    noOfplayers = num
    clearFrame()

    for i in range(noOfplayers):
        label = ttk.Label(frame, text="Player " + str(i+1) + " Name:")
        label.pack(side='top', pady=5)
        entry = ttk.Entry(frame)
        entry.pack(side='top', pady=5)
        nameEntries.append(entry)

    confirmButton = ttk.Button(frame, text="Confirm", command=setNames)
    confirmButton.pack(side='bottom', pady=5)

def setNoOfPlayers():
    clearFrame()
    button1 = ttk.Button(frame, text="2 Players", command = lambda: setPlayers(2))
    button1.pack(side='left', padx=5)

    button2 = ttk.Button(frame, text="3 Players", command = lambda: setPlayers(3))
    button2.pack(side='left', padx=5)

    button3 = ttk.Button(frame, text="4 Players", command = lambda: setPlayers(4))
    button3.pack(side='left', padx=5)

setNoOfPlayers()
window.mainloop()