# from analyseGrid import analyse_grid
# from displayGrid import return_stateful_list
# from validateCallout import validate_callouts
from numberOfPlayers import numberOfPlayers
from setupRound import getShowcards
from setupRound import getScorecards
from displayGrid import displayGridList
from preRound import preRoundPredictions

# Asking number of players and their names. 
numPlayers, namePlayers = numberOfPlayers()
print(f"You've chosen {numPlayers} players.")

showcards = getShowcards()
scorecards = getScorecards()

#Displaying the player order.
print(f"The players, in order of their turns are: {namePlayers}.")

predictions = preRoundPredictions.preRoundPredictions(namePlayers)

displayGridList(showcards)

#validate player callout by sending user input
#check_callout = validate_callouts(['Ace', 'Spade', '0'])
#print(check_callout)

#analyze grid if theres a last card left
#check_grid = analyse_grid(return_stateful_list())  #theres a logic clash in this, DISCUSS over scrum
#print(check_grid)

#TODO: where are playerwise scorecards stored that they won with every correct prediction??
#TODO: the card data syntax doesnt match between taufiq and manan, and wheres the pre_round predictions stored?. please coordinate and use same card storing syntax, mana us using ['ace', 'Hearts', '0'], taufiq is using ['Q','H']

