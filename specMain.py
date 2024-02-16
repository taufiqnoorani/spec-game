# from analyseGrid import analyse_grid
# from displayGrid import return_stateful_list
# from validateCallout import validate_callouts
from numberOfPlayers import numberOfPlayers
from playTurn.addingScores import addingScores
from playTurn.guess import guess
from setupRound import getShowcards
from setupRound import populate_playerScoreDict
from setupRound import getScorecards
from displayGrid import displayGridList
from preRound import preRoundPredictions
from analyseGrid import analyse_grid, assign_scorecards, give_scorecards_callout
from playTurn.updatedGrid import updatedGrid
from preRound.preRoundScoring import preRoundScoring
from endRound.endRoundScoring import endRoundScoring
from endRound.endRoundCondition import endRoundCondition
from endRound.endRoundLast import endRoundLast

# GLOBAL VARIABLES
all_player_guesses = {}
#variable for game scores
gameScores = {}

# Asking number of players and their names.
numPlayers, namePlayers = numberOfPlayers()
print(f"You've chosen {numPlayers} players.")

for name in namePlayers:
    gameScores[name] = 0

# Displaying the player order.
print(f"The players, in order of their turns are: {namePlayers}.")

# number of rounds played
# for rounds in numPlayers:

for rounds in namePlayers:

    # save player sccore
    player_scores = populate_playerScoreDict(namePlayers)  # stores player scores
    all_player_guesses = populate_playerScoreDict(namePlayers)  # stores player guesses

    showcards = getShowcards()
    scorecards = getScorecards()
    predictions = preRoundPredictions.preRoundPredictions(namePlayers)

    displayGridList(showcards)

    i = 0
    last_player = ""
    while True:
        # print("showcards before updating \n")
        # print(showcards)
        #print(showcards)
        # Loop until there is only one card left
        if analyse_grid(showcards) is True:
            print("Only One card left")
            break
        # player guess one by one
        print("\nPLAY TURN\nprevious turn player: ")
        print(last_player)
        player_guess, player = guess(namePlayers[i], showcards, all_player_guesses, last_player)

        # checks in case of callout
        # ----------------------------------------------------------------------------------------------------
        if player_guess[0] == "player":
            print("(guess match): award showcards to: ")
            print(player)
            player_scores = give_scorecards_callout(player, last_player, scorecards, player_scores, "player")
            print(f"All Player Scores: \n{player_scores}")
            continue
        elif player_guess[0] == "grid":
            print("(grid match): award showcards to ")
            print(player)
            player_scores = give_scorecards_callout(player, last_player, scorecards, player_scores, "grid")
            print(f"All Player Scores: \n{player_scores}")
            continue
        elif player_guess[0] == "none":
            print("Wrong Callout! \nGame Continues\n")
            continue
        # ----------------------------------------------------------------------------------------------------

        all_player_guesses[namePlayers[i]].append(player_guess)  # storing player guesses after every turn
        print("Player Guesses: \n")
        print(all_player_guesses)

        # player guessed card revealed on grid
        showcards, card_matched_in_grid = updatedGrid(showcards, player_guess)

        displayGridList(showcards)  # displays the main grid
        # print("showcards after updating \n")
        # print(showcards)

        # assign player scorecards with respect to correct guesses

        score, msg = addingScores(card_matched_in_grid, player_guess)
        player_scores = assign_scorecards(player_scores, scorecards, score, namePlayers[i])
        if score > 0:
            lastScorecardWinner = namePlayers[i]

        # print("showcards after updating and pred \n")
        # print(showcards)

        print(f"All Player Scores: \n{player_scores}")

        last_player = namePlayers[i]  # stores the last player who took took the turn

        i += 1
        if i == numPlayers:
            i = 0

    # Check pre round predictions
    for card in showcards:
        if card[3] == "0":
            lastCard = card
            showcards, card_matched_in_grid = updatedGrid(showcards, lastCard)
            break
    displayGridList(showcards)
    bonusPlayer, bonusPoints = preRoundScoring(predictions, lastCard, lastScorecardWinner, scorecards)
    print(f"{bonusPlayer} wins {bonusPoints} bonus points!")

    #Add the scores of the round to total scores of the game
    gameScores = endRoundScoring(player_scores, bonusPlayer, bonusPoints, namePlayers, gameScores)

    #Check if any player/s have reached a score of 173 or more and declare them as winners
    winnerConditional = endRoundCondition(gameScores)
    if winnerConditional is True:
        break
#Declare winners at the end of all rounds
endRoundLast(winnerConditional, gameScores)
print("\nGAME ENDED")