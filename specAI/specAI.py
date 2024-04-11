#Importing modules
import random
from preRound.makePredictions import preRoundPredictions, aiPredictions
from preRound.preRoundScoring import preRoundScoring
from specAI.setupRound import getShowcards, getScorecards, populatePlayerScoreDict
from specAI.displayGrid import displayGridList
from specAI.analyseGrid import analyseGrid, updatedGrid, assignScorecards
from specAI.guess import guess
from specAI.validate import validateCallouts
from specAI.addingScores import addingScores
from specAI.endRoundScoring import endRoundScoring
from specAI.endRoundCondition import endRoundCondition
from specAI.endRoundLast import endRoundLast


filepath = ""

# GLOBAL VARIABLES
allPlayerGuesses = {}

# Symbols for the suits
suiteDict = {"Spade": "♠",
          "Heart": "♥",
          "Club": "♣",
          "Diamond": "♦",
          "Joker": "🃏"}


def specAI(difficulty):
    numberOfPlayers = 2
   
    name = input("Enter your name: ")
    nameOfPlayers = [name, "AI"]
    
    # Initialize an empty gameScores dictionary
    gameScores = {}
    
    # Choose AI difficulty level
    if difficulty == '1':
        from AI.easyAI import gameAI as AI
    elif difficulty == '2':
        from AI.mediumAI import gameAI as AI
    elif difficulty == '3':
        from AI.hardAI import gameAI as AI

    # Display player order
    print(f"The players, in order of their turns are: {nameOfPlayers}.")

    rounds = numberOfPlayers
    i = 0

    for pre in range(2):
        # Initialize playerScores and allPlayerGuesses dictionaries
        playerScores = populatePlayerScoreDict(nameOfPlayers)
        allPlayerGuesses = populatePlayerScoreDict(nameOfPlayers)

        humanPrediction = preRoundPredictions(nameOfPlayers[0])
        aiPrediction = aiPredictions(nameOfPlayers[1], humanPrediction)
        print(f"The AI has predicted: {aiPrediction}")
        print(f"The predictions for this round are: {humanPrediction} and {aiPrediction}")
        predictions = {**humanPrediction, **aiPrediction}

        showcards = getShowcards()
        scorecards = getScorecards()
        displayGridList(showcards)

        lastPlayer = ""

        while True:
            # Loop until there is only one card left
            if analyseGrid(showcards):
                print("Only one card left.")
                break

            print(f"{nameOfPlayers[0]}'s turn:")
            playerGuess, player = guess(nameOfPlayers[0], showcards)
            allPlayerGuesses[nameOfPlayers[0]].append(playerGuess)
            showcards, cardMatchedInGrid = updatedGrid(showcards, playerGuess)
            score, msg = addingScores(cardMatchedInGrid, playerGuess)
            playerScores = assignScorecards(playerScores, scorecards, score, nameOfPlayers[0])

            print(f"{nameOfPlayers[1]}'s turn:")
            aiGuess = AI(showcards)
            allPlayerGuesses[nameOfPlayers[1]].append(aiGuess)
            showcards, cardMatchedInGrid = updatedGrid(showcards, aiGuess)
            aiScore, msg = addingScores(cardMatchedInGrid, aiGuess)
            playerScores = assignScorecards(playerScores, scorecards, aiScore, nameOfPlayers[1])

            displayGridList(showcards)

        lastPlayer = nameOfPlayers[i]  # Store the last player who took the turn
        i = (i + 1) % numberOfPlayers

        lastCard = next(card for card in showcards if card[3] == "0")
        showcards, cardMatchedInGrid = updatedGrid(showcards, lastCard)
        displayGridList(showcards)
        
        bonusPlayer, bonusPoints = preRoundScoring(predictions, lastCard, lastPlayer, scorecards)
        print(f"{bonusPlayer} wins {bonusPoints} bonus points!")

        # Update gameScores with playerScores for the current round
        for player in nameOfPlayers:
            if player not in gameScores:
                gameScores[player] = 0
            gameScores[player] += sum(playerScores[player])

        # Check if any player/s have reached a score of 173 or more and declare them as winners
        if endRoundCondition(gameScores):
            break

    # Declare winners at the end of all rounds
    endRoundLast(endRoundCondition(gameScores), gameScores)
    print("\nGAME ENDED")