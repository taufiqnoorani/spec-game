
from cards import create_deck_dataframe
from numberOfPlayers import numberOfPlayers

#  Saving the values.
num_players = numberOfPlayers()
print(f"You've chosen {num_players} players.")

showCards = create_deck_dataframe()
#print(showCards)
for key, value in showCards.items():
    print(f"Key: {key}, Value: {value}")
# Asking players for names.

#name = input("Enter the name")