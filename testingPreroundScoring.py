from preRoundScoring import preRoundScoring

if __name__ == "__main__":
   print("Scoring for Pre-Round:")
   predictions = {
    "Player1": ("Q", "H"),
    "Player2": ("K", "S"),
    "Player3": ("J", "C")}
   lastCard = ("Q", "S")
   lastScorecardWinner = "Player2"
   scorecards = [2, 3, 4]
   bonusPlayer, bonusPoints = preRoundScoring(predictions, lastCard, lastScorecardWinner, scorecards)
   print(f"Remaining points: {bonusPoints} for player: {bonusPlayer}")