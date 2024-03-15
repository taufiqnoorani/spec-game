import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from cardMap import getCardAsset
from setupRound import getShowcards, getScorecards
import pandas as pd
from analyseGrid import analyse_grid
from analyseGrid import assign_scorecards
from guiAddingScores import addingScoresGUI
from preRound.preRoundScoring import preRoundScoring
from endRound.endRoundScoring import endRoundScoring

filePath = "Sprint#1/"

window = tk.Tk()
window.title("Spec")
window.geometry('1280x800')


frame = ttk.Frame(window)
frame.place(relx=0.5, rely=0.5, anchor='center')



noOfPlayers = 0

#Player Names, this list will be used to store the names of the players
#Will be updated at the end of every round: Shift position of players by 1
playerNames = []

#Round Scores, this dict will be used to store the scores of the players at the end of every round
#Will be updated at the end of every round: Scorecards will be converted to scores and added to this dict
roundScores = {}

#game scores
gameScores = {}

#Scorecards for each player, this dict will be used to store the scorecards of the players
#Will be reset to empty at the start of every round
playerScorecards = {}

#A global list of all showcardsLabels
#Appending all showcard labels to this list will prevent the garbage collector from deleting them
cardList = []

#A global list of all the PhotoImages
#Appending all PhotoImages to this list will prevent the garbage collector from deleting them
cardImage = []

#A global variable for scorecard deck
scoreCardDeck = tk.PhotoImage(file=filePath+"images/cards/card-back2.png")

#A global variable for player scorecard deck
playerScoreCardDeck = tk.PhotoImage(file=filePath+"images/cards/card-back3.png")

#The player who makes the callout

predictions = {}

#[['player', 'rank', 'suite']]
previousGuess = []

lastPlayerScored = ""

showcards = getShowcards()  #Get a random set of showcards. Called after every round
scorecards = getScorecards()  #Get an ordered set of scorecards. Called after every round


#Method to clear the elements in the frame:frame
def clearFrame():
    for widget in frame.winfo_children():
        widget.forget()

#A method to a ordered list of showcards with all but one joker removed
def getOrdererdShowcards():
    showcardList = []
    randomList = range(0,25)
    showcards1 = pd.read_csv(filePath+"showcards.csv")
    i = 1
    for r in randomList:
        sc = [str(showcards1.iloc[r].Rank), str(showcards1.iloc[r].Suite)]
        if sc[0] == "Joker" or sc[1] == "Joker":
            continue
        showcardList.append(sc)
        i+=1
    showcardList.append(["Joker", "."])
    return showcardList

#This method will run the round loop
#Number of loops = number of players
def runRound():
    global playerScorecards
    global showcards
    global scorecards
    showcards = getShowcards()
    scorecards = getScorecards()
    for x in playerNames:
        playerScorecards[x] = [] #Set the scorecards for each player to an empty list
    #Show Card grid - Step 2
    #This will allow the players in order, to select a card to flip, and guss what is will be
    def displayGrid(i):
        clearFrame()
        global cardList
        cardList = []
        global cardImage
        cardImage = []
        currentPlayer = playerNames[i]

        #display the fully flipped grid
        def displayLastGrid():
            clearFrame()
            global cardList
            cardList = []
            global cardImage
            cardImage = []
            for row in range(5):
                for column in range(5):
                    showcards[cardI][3] = '1'
                    cardAsset = getCardAsset(showcards[cardI])
                    cardImage.append(tk.PhotoImage(file=cardAsset))
                    #image = tk.PhotoImage(file=cardAsset)
                    cardList.append(ttk.Label(frame, image=cardImage[cardI]))
                    #label = ttk.Label(frame, image=cardImage[i])
                    cardList[cardI].grid(row=row, column=column)
                    cardI+=1
            scoreLabel = ttk.Label(frame, text = "Final scores")
            scoreLabel.grid(row=5, column=1, columnspan=5)
            

        #Callout button
        def onClickCallout():
            callee = ""

            if len(previousGuess) <= 1:
                print("Callout not possible")
                messagebox.showinfo("Wrong Callout", "Callout not possible")
            elif previousGuess[-1][1] == previousGuess[-2][1] and previousGuess[-1][2] == previousGuess[-2][2]:

                calloutWindow = tk.Tk()
                calloutWindow.title("Callout")
                calloutWindow.geometry('300x200')
                calloutFrame = ttk.Frame(calloutWindow)
                calloutFrame.place(relx=0.5, rely=0.5, anchor='center')
                label1 = ttk.Label(calloutFrame, text= previousGuess[-1][0] + " has been called out")
                label1.pack(side = "top", pady=5)
                label2 = ttk.Label(calloutFrame, text= "for their guess: "+previousGuess[-1][1]+","+previousGuess[-1][2])
                label2.pack(side = "top", pady=5)
                label3 = ttk.Label(calloutFrame, text= "Who made the callout?")
                label3.pack(side = "top", pady=5)
                global calloutList
                calloutList = []
                for names in playerNames:
                    if names != previousGuess[-1][0]:
                        calloutList.append(names)
            
                calloutCombo = ttk.Combobox(calloutFrame, values=calloutList)
                calloutCombo.pack(side = "top", pady=5)
                calloutCombo.current(0)

                def setCalleeDel(callee1):
                    callee = callee1
                    if playerScorecards[previousGuess[-1][0]] != []:
                        playerScorecards[callee].append(playerScorecards[previousGuess[-1][0]].pop(-1))
                        messagebox.showinfo("Correct Callout", ""+callee+" was awarded the top scorecard of "+previousGuess[-1][0])
                    elif scorecards != []:
                        playerScorecards[callee].append(scorecards.pop(-1))
                        messagebox.showinfo("Correct Callout", ""+callee+" was awarded the top scorecard from the pile")
                    calloutWindow.destroy()

                calloutConfirmButton = ttk.Button(calloutFrame, text="Confirm", command=lambda: setCalleeDel(calloutCombo.get()))
                calloutConfirmButton.pack(side = "top", pady=5)

                print("Player: " + callee + " called out player: " + previousGuess[-1][0])
                print("Guess: ", previousGuess[-1][1]+"," +previousGuess[-1][2])
                
                
            else:
                print("Wrong callout")
                messagebox.showinfo("Invalid Callout", "Nothing to callout")
                

        #Assign scores to the players
        def assignScoreCard(guess, card):
            global playerScorecards

            previousGuess.append([currentPlayer, guess.split(' ')[0], guess.split(' ')[1]])
            #tempScore is how many scorecards the player will get
            #print(guess.split(" "))
            #print("Card: ", card)
            tempScore = addingScoresGUI(card, guess.split(" "))
            #print(tempScore)
            playerScorecards = assign_scorecards(playerScorecards, scorecards, tempScore, currentPlayer)
            if tempScore > 0:
                lastPlayerScored = currentPlayer
            #print(playerScorecards)
            showcards[int(card[0])-1][3] = '1' #Flip the card
            if i < noOfPlayers-1:
                displayGrid(i+1)
            else:
                displayGrid(0)


        #This method will handle the click event for the score card and provide the player with a drop down menu to select the card
        def onCardClick(event, card):
            if event == "last":
                c = []
                c[0] =""
                c[1] = card[0]
                c[2] = card[1]
                bonusplayer, bonuspoints = preRoundScoring(predictions,c,lastPlayerScored,scorecards)
                messagebox.showinfo("Last card winner", ""+bonusplayer+" was awarded "+bonuspoints+" bonus points")

                gameScores = endRoundScoring(playerScorecards, bonusplayer, bonuspoints, playerNames, gameScores)

                print(gameScores)
                displayLastGrid()
                return
            #print("Card clicked: ", card)
            #Show a another small window that allows the plyer what the the flipped card might be
            #The player has a drop down menu with all the showcards to select from
            selWindow = tk.Tk()
            selWindow.title("Guess Card")
            selWindow.geometry('300x200')
            selFrame = ttk.Frame(selWindow)
            selFrame.place(relx=0.5, rely=0.5, anchor='center')
            label = ttk.Label(selFrame, text= playerNames[i] + " choose the card you think it is")
            label.pack(side = "top", pady=5)
            selCombo = ttk.Combobox(selFrame, values=getOrdererdShowcards())
            selCombo.pack(side = "top", pady=5)
            selCombo.current(0)

            def onClickAssign():
                assignScoreCard(selCombo.get(), card)
                selWindow.destroy()

            confirmButton = ttk.Button(selFrame, text="Confirm", command=onClickAssign)
            confirmButton.pack(side = "top", pady=5)
            selWindow.wm_attributes("-topmost", 1)
            selWindow.focus_force()
            selWindow.mainloop()
        

        cardI = 0
        for row in range(5):
            for column in range(5):
                cardAsset = getCardAsset(showcards[cardI])
                cardImage.append(tk.PhotoImage(file=cardAsset))
                #image = tk.PhotoImage(file=cardAsset)
                cardList.append(ttk.Label(frame, image=cardImage[cardI]))
                #label = ttk.Label(frame, image=cardImage[i])
                cardList[cardI].grid(row=row, column=column)
                if str(showcards[cardI][3]) == '0' and analyse_grid(showcards) == False:
                    cardList[cardI].bind("<ButtonRelease>", lambda event, card=showcards[cardI]: onCardClick(event, card))

                #Last card left
                if(analyse_grid(showcards) == True):
                    print("Last card left")
                    messagebox.showinfo("Last Card Left", "Click to reveal last card")
                    onCardClick("last", showcards[cardI])
                cardI+=1
        
        scDeckLabel = ttk.Label(frame, text = "Scorecards in Deck "+ str(len(scorecards)))
        scDeckLabel.grid(row=0, column=5, rowspan=1, padx=2, pady=2)

        scoreCardDecklabel = ttk.Label(frame, image=scoreCardDeck)
        scoreCardDecklabel.grid(row=1, column=5, rowspan=1, padx=2, pady=2)

        playerScoreCardImageLabel = ttk.Label(frame, image=playerScoreCardDeck)
        playerScoreCardImageLabel.grid(row=3, column=5, rowspan=1, padx=2, pady=2)

        playerScoreCardLabel = ttk.Label(frame, text = "Scorecards in "+currentPlayer+"'s deck "+ str(len(playerScorecards[currentPlayer])))
        playerScoreCardLabel.grid(row=4, column=5, rowspan=1, padx=2, pady=2)

        turnLabel = ttk.Label(frame, text = "Current Player: " + currentPlayer)
        turnLabel.grid(row=5, column=0, columnspan=5)
        calloutButton = ttk.Button(frame, text="Callout", command = onClickCallout)
        calloutButton.grid(row=6, column=0, columnspan=5)


    #Start by accepting pre round predictions - Step 1
    def getPreRoundPredictions(i):
        clearFrame()
        global preDeck
        global playerNames
        global predictions
        if i == 0:
            preDeck = getOrdererdShowcards() #this is an initial list of cards, as the cards predicted, they will removed acc. to rules
            predictions.clear()

        #Set the predictions
        def setPredictions(comboElement):
            global predictions
            global playerNames
            predictions[playerNames[i]] = comboElement.split(" ")

            #Remove the predicted card from the preDeck
            preDeck.remove(comboElement.split(" "))
            for card in preDeck.copy():
                if card[0] == comboElement.split(" ")[0] or card[1] == comboElement.split(" ")[1]:
                    preDeck.remove(card)

            getPreRoundPredictions(i+1)

        if i < noOfPlayers:
            label = ttk.Label(frame, text= playerNames[i] + " make your prediction for the last card")
            label.pack(side = "top", pady=5)
            preCombo = ttk.Combobox(frame, values=preDeck)
            preCombo.pack(side = "top", pady=5)
            preCombo.current(0)
            confirmButton = ttk.Button(frame, text="Confirm", command=lambda: setPredictions(preCombo.get()))
            confirmButton.pack(side = "top", pady=5)
        else:
            displayGrid(0)  
        
    getPreRoundPredictions(0)


#This method will setup the main game
#It will ask for the number of players and their names
def setupGame():
    clearFrame()
    global roundScores
    global playerScorecards

    #Sets the scores for all players for a ROUND to 0
    def readyRound():
        for name in playerNames:
            playerScorecards[name] = []
            roundScores[name] = 0
        runRound()

    #Set the names of players
    def setNames():
        global playerNames
        for entry in nameEntries:
            playerNames.append(entry.get())
        readyRound()

    #Ask for the names of all players
    def getNames():
        clearFrame()

        #A temporary variable to store all the entries for the names of the players
        global nameEntries
        nameEntries = []

        for i in range(noOfPlayers):
            label = ttk.Label(frame, text="Enter name of Player "+str(i+1))
            label.pack(side = "top", pady=5)
            nameEntry = ttk.Entry(frame)
            nameEntry.pack(side = "top", pady=5)
            nameEntries.append(nameEntry)
        
        confirmButton = ttk.Button(frame, text="Confirm", command=setNames)
        confirmButton.pack(side = "top", pady=5)


    #Set Number of players
    def setNoOfPlayers(no):
        global noOfPlayers
        noOfPlayers = no
        getNames() #Once we have the number of players we can ask for their names

    #Ask for the number of players in a game
    def getNoOfPlayers():

        clearFrame()
        twoButton = ttk.Button(frame, text="2 Players", command=lambda: setNoOfPlayers(2))
        twoButton.pack(side="left", padx=5)
        threeButton = ttk.Button(frame, text="3 Players", command=lambda: setNoOfPlayers(3))
        threeButton.pack(side="left", padx=5)
        fourButton = ttk.Button(frame, text="4 Players", command=lambda: setNoOfPlayers(4))
        fourButton.pack(side="left", padx=5)
    
    getNoOfPlayers()
    #print(noOfPlayers)
setupGame()

window.mainloop()