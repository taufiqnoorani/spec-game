from numberOfPlayers import numberOfPlayers
from preRoundPredictions import takePreRoundGuess

if __name__ == "__main__":
    print("Welcome to Spec.")
    players, names = numberOfPlayers()
    predictions = takePreRoundGuess(players, names)
    print("Predictions for Pre-Round:")
    for player, prediction in predictions.items():
        print(f"{player}: {prediction}")
