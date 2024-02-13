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
from analyseGrid import analyse_grid, assign_scorecards
from playTurn.updatedGrid import updatedGrid
from preRound.preRoundScoring import preRoundScoring

#GLOBAL VARIABLES
all_player_guesses = []

# Asking number of players and their names.
numPlayers, namePlayers = numberOfPlayers()
print(f"You've chosen {numPlayers} players.")

# Displaying the player order.
print(f"The players, in order of their turns are: {namePlayers}.")

# number of rounds played
# for rounds in numPlayers:

for rounds in namePlayers:

    # save player sccore
    global player_scores
    player_scores = populate_playerScoreDict(namePlayers)

    showcards = getShowcards()
    scorecards = getScorecards()
    predictions = preRoundPredictions.preRoundPredictions(namePlayers)

    displayGridList(showcards)

    i = 0
    while True:
        #print("showcards before updating \n")
        #print(showcards)

        #Loop until there is only one card left
        if analyse_grid(showcards) is True:
            print("Only One card left")
            break
        # player guess one by one
        player_guess, player = guess(namePlayers[i], showcards, all_player_guesses) #takes the previous player guess aswell for callout

        all_player_guesses.append(player_guess)

        print(all_player_guesses)

        #player guessed card revealed on grid
        showcards, card_matched_in_grid = updatedGrid(showcards, player_guess)

        displayGridList(showcards) #displays the main grid
        #print("showcards after updating \n")
        #print(showcards)

        #assign player scorecards with respect to correct guesses

        score, msg = addingScores(card_matched_in_grid , player_guess)
        player_scores = assign_scorecards(player_scores, scorecards, score, namePlayers[i])
        if score > 0:
            lastScorecardWinner = namePlayers[i]

        #print("showcards after updating and pred \n")
        #print(showcards)

        print("Score: ")
        print(player_scores)

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

    #Update player order
    namePlayers.append(namePlayers.pop(0))

print("game ended")

