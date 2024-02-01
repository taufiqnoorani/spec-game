
from cards import createDeckDataframe
from numberOfPlayers import numberOfPlayers

#  Saving the values.
numPlayers = numberOfPlayers()
print(f"You've chosen {numPlayers} players.")

showcards = createDeckDataframe()
#print(showCards)
for key, value in showcards.items():
    print(f"Key: {key}, Value: {value}")
# Asking players for names.