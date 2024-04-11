
from setupRound import getScorecards
from analyseGrid import assignScorecards

scorecards = getScorecards()
name = input("Enter your name: ")
playerScores = {}
nameOfPlayers = [name, "AI"]
playerName = nameOfPlayers[0]  # Assuming it's the human player's turn
score = 10  # Example score earned by the player
playerScores = assignScorecards(playerScores, scorecards, score, playerName)

# After updating scores for all players, you can print or inspect playerScores
print(playerScores)