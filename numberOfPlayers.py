def numberOfPlayers():
    while True:
        try:
            players = int(input("Enter the number of players playing (must be between 2 to 4): "))
            if 2 <= players <= 4:
                break  # Break out of the loop if a valid number of players is entered
            else:
                print("Invalid player number. Please choose a value between 2 and 4.")
        except ValueError:
            print("Invalid input. Please enter a valid integer between 2 and 4.")

    return players

#  Saving the values.
num_players = numberOfPlayers()
print(f"You've chosen {num_players} players.")

# Asking players for names.

name = input("Enter the name")