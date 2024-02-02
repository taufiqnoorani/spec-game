import random

def numberOfPlayers():
    while True:
        try:
            players = int(
                input("Enter the number of players playing (must be between 2 to 4): "))
            if 2 <= players <= 4:
                break  # Break out of the loop if a valid number of players is entered
            else:
                print("Invalid player number. Please choose a value between 2 and 4.")
        except ValueError:
            print("Invalid input. Please enter a valid integer between 2 and 4.")
    # Asking for player names.
    names = []
    for i in range(players):
        name = input(f"Enter name for Player {i + 1}: ")
        names.append(name)

    # Randomize the order of player names
    random.shuffle(names)

    return players, names


playerNumber, playerName = numberOfPlayers()
print(f"The players, in order of their turns are: {playerName}.")