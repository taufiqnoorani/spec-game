from numberOfPlayers import numberOfPlayers
from preRoundPredictions import preRoundPredictions

if __name__ == "__main__":
    print("Welcome to Spec.")
    players, names = numberOfPlayers()
    predictions = preRoundPredictions(players, names)
    print("Predictions for Pre-Round:")
    for player, prediction in predictions.items():
        print(f"{player}: {prediction}")
