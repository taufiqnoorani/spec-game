
from cards import createDeckDataframe
from numberOfPlayers import numberOfPlayers

# Asking number of players and their names. 
numPlayers, namePlayers = numberOfPlayers()
print(f"You've chosen {numPlayers} players.")

showcards = createDeckDataframe()
#print(showCards)
for key, value in showcards.items():
    print(f"Key: {key}, Value: {value}")

#Displaying the player order.
print(f"The players, in order of their turns are: {namePlayers}.")