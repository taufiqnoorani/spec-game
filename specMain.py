# from analyseGrid import analyse_grid
# from displayGrid import return_stateful_list
# from validateCallout import validate_callouts
from numberOfPlayers import numberOfPlayers
from playTurn.guess import guess
from setupRound import getShowcards
from setupRound import getScorecards
from displayGrid import displayGridList
from preRound import preRoundPredictions
from analyseGrid import analyse_grid
from playTurn.updatedGrid import updatedGrid

# Asking number of players and their names.
numPlayers, namePlayers = numberOfPlayers()
print(f"You've chosen {numPlayers} players.")

# Displaying the player order.
print(f"The players, in order of their turns are: {namePlayers}.")

# number of rounds played
# for rounds in numPlayers:

for rounds in namePlayers:

    showcards = getShowcards()
    scorecards = getScorecards()
    predictions = preRoundPredictions.preRoundPredictions(namePlayers)

    displayGridList(showcards)
    # print(predictions)
    print(namePlayers)
    i = 0
    while True:
        #print(showcards)
        #Loop until there is only one card left
        if analyse_grid(showcards) is True:
            print("Only One card left")
            break

        print(i)
        print(namePlayers[i])
        player_guess, player = guess(namePlayers[i], showcards)
        i += 1
        if i == numPlayers:
            i = 0

        print(player_guess)
        print(player)
        showcards =updatedGrid(showcards, player_guess)
        print(showcards)
        displayGridList(showcards)


# validate player callout by sending user input
# check_callout = validate_callouts(['Ace', 'Spade', '0'])
# print(check_callout)

# analyze grid if theres a last card left
# check_grid = analyse_grid(return_stateful_list())  #theres a logic clash in this, DISCUSS over scrum
# print(check_grid)
