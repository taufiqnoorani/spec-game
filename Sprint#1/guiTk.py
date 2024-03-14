import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from setupRound import getScorecards, getShowcards
from cardMap import getCardAsset
import pandas as pd
from analyseGrid import analyse_grid

noOfplayers = 0

predI = 0

filePath = "Sprint#1/"

window = tk.Tk()

window.title("Spec")

window.geometry('1280x800')

frame = ttk.Frame(window)
frame.place(relx=0.5, rely=0.5, anchor='center')

gameScores = {}
nameEntries = []
predictions = {}
predictionEntries = []
preDeck = []
showcards = getShowcards()
scorecards = getScorecards()
previousGuess = {}
currentRound = 0
roundScores = {}


def getOrdererdShowcards():
    showcardList = []
    randomList = range(0,25)
    showcards1 = pd.read_csv(filePath+"showcards.csv")
    i = 1
    for r in randomList:
        sc = [str(showcards1.iloc[r].Rank), str(showcards1.iloc[r].Suite)]
        showcardList.append(sc)
        i+=1
    return showcardList

def clearFrame():
    for widget in frame.winfo_children():
        widget.forget()

def assignScore(guess, card):
    print("Guess: ", guess)
    displayGrid()
    print(gameScores)

def onCardClick(event, card):
    print("Card clicked: ", card)
    showcards[int(card[0])-1][3] = '1'
    #Show a another small window that allows the plyer what the the flipped card might be
    #The player has a drop down menu with all the showcards to select from
    
    selWindow = tk.Tk()
    selWindow.title("Select Card")
    selWindow.geometry('300x200')
    selFrame = ttk.Frame(selWindow)
    selFrame.place(relx=0.5, rely=0.5, anchor='center')
    selLabel = ttk.Label(selFrame, text="Select a card to predict")
    selLabel.pack(side='top', pady=5)
    selCard = ttk.Combobox(selFrame, values=getOrdererdShowcards())
    selCard.pack(side='top', pady=5)
    selCard.current(0)

    def onConfirm():
        assignScore(selCard.get(), card)
        selWindow.destroy()

    confirmButton = ttk.Button(selFrame, text="Confirm", command=lambda: onConfirm())
    confirmButton.pack(side='bottom', pady=5)
    

#From the showcards, display the grid of cards
def displayGrid():
    clearFrame()
    global cardImage
    cardImage = []
    global cardList
    cardList = []
    i = 0

    for row in range(5):
        for column in range(5):
            cardAsset = getCardAsset(showcards[i])
            cardImage.append(tk.PhotoImage(file=cardAsset))
            #image = tk.PhotoImage(file=cardAsset)
            cardList.append(ttk.Label(frame, image=cardImage[i]))
            #label = ttk.Label(frame, image=cardImage[i])
            cardList[i].grid(row=row, column=column)
            if showcards[i][3] == '0' and analyse_grid(showcards) == False:
                cardList[i].bind("<ButtonRelease>", lambda event, card=showcards[i]: onCardClick(event, card))
            i+=1

    currentPlayerLabel = ttk.Label(frame, text = "Current Player: " + nameEntries[0].get())
    currentPlayerLabel.grid(row=5, column=0, columnspan=5)

#Handle all the round states: current player, round scores
def playRound():
    clearFrame()
    if currentRound <= noOfplayers: #Will run as many times as the number of players
        for name in nameEntries:
            roundScores[name.get()] = 0
        displayGrid()

preDeck = getOrdererdShowcards()
#Ask each player in order, what their predictions are for the round
#Each player can select a card from the showcards to predict
def preRoundPredictions():
    clearFrame()
    global predI
    tempCard = []
    for card in preDeck.copy():
        if card[0] == "Joker" or card[1] == "Joker":
            preDeck.remove(card)

    preDeck.append("Joker")
    if len(predictions) < noOfplayers:
        if nameEntries[predI].get() not in predictions:
            preWindow = tk.Tk()
            preWindow.title("Predict last Card")
            preWindow.geometry('300x200')
            preFrame = ttk.Frame(preWindow)
            preFrame.place(relx=0.5, rely=0.5, anchor='center')
            preLabel = ttk.Label(preFrame, text="" + nameEntries[predI].get() + " Predict the last card of the game")
            preLabel.pack(side='top', pady=5)
            preCard = ttk.Combobox(preFrame, values=preDeck)
            preCard.pack(side='top', pady=5)
            preCard.current(0)

            def onPreConfirm():
                predictions[nameEntries[predI].get()] = preCard.get().split(' ')

                tempCard = preCard.get().split(' ')
                for card in preDeck:
                    if card == tempCard:
                        preDeck.remove(card)
                    elif card[0] == tempCard[0]:
                        preDeck.remove(card)
                    elif card[1] == tempCard[1]:
                        preDeck.remove(card)

                preWindow.destroy()
                preRoundPredictions()

            confirmButton = ttk.Button(preFrame, text="Confirm", command=lambda: onPreConfirm())
            confirmButton.pack(side='bottom', pady=5)
        else:
            predI+=1
            preRoundPredictions()
    else:
        #Conitnue with the rest of the game
        print("Predictions: ", predictions)
        playRound()

            


def setNames():
    #nameEntries.shuffle()
    playerNames = []
    for name in nameEntries:
        playerNames.append(name.get())
        gameScores[name.get()] = 0
    #messagebox.showinfo("Player Names", "Player names: " + ', '.join(playerNames))
    global currentRound
    currentRound += 1
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