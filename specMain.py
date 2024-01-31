
from cards import createDeckDataframe
from numberOfPlayers import numberOfPlayers

#  Saving the values.
num_players = numberOfPlayers()
print(f"You've chosen {num_players} players.")

showCards = createDeckDataframe()
#print(showCards)
for key, value in showCards.items():
    print(f"Key: {key}, Value: {value}")
# Asking players for names.