import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from setupRound import getScorecards, getShowcards
from cardMap import getCardAsset

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
showcards = getShowcards()
scorecards = getScorecards()


def clearFrame():
    for widget in frame.winfo_children():
        widget.forget()

def displayCard():
    clearFrame()
    card = showcards[0]
    cardAsset = getCardAsset(card)
    global image
    image = tk.PhotoImage(file=cardAsset)
    button = ttk.Button(frame, image=image, text="Card", compound='top')
    button.pack(side='top', pady=5)


def onCardClick(event, card):
    print("Card clicked: ", card)
    showcards[int(card[0])-1][3] = '1'
    displayGrid()

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
            if showcards[i][3] == '0':
                cardList[i].bind("<ButtonRelease>", lambda event, card=showcards[i]: onCardClick(event, card))
            i+=1


#Ask each player in order, what their predictions are for the round
#Each player can select a card from the showcards to predict
#The players can select the cards from a 5x5 grid
def preRoundPredictions():
    clearFrame()
    

    

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

displayGrid()
#displayCard()
window.mainloop()