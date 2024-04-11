# from endRoundScoring import gameScores

def endRoundCondition(gameScores):
    if not gameScores or any(score >= 173 for score in gameScores.values()):
        winners = {player: score for player, score in gameScores.items() if score >= 173}
        if winners:
            print("\nThe following players have reached a score of 173 or more and are winners:")
            for player, score in winners.items():
                print(f"Player {player} with a score of {score}")
                # Print the total scores
                print("\nTotal Scores:")
                for key, value in gameScores.items():
                    print(f"Player {key}: {value}")
            return True
    return False

    