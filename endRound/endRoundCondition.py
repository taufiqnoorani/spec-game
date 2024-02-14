# from endRoundScoring import gameScores

def endRoundCondition(gameScores):   

    #Check the score list and declare players winner if they reach score of atleast 173
    global winnerConditional
    winnerConditional = {player: score for player, score in gameScores.items() if score >= 173}
    if winnerConditional:
        print("\nThe following players have reached a score of 173 or more and are winners:")
        for player, score in winnerConditional.items():
            print(f"Player {player} with a score of {score}")
            # Print the total scores
            print("\nTotal Scores:")
            for key, value in gameScores.items():
                print(f"Player {key}: {value}")     
            return True       
    else:       
        return winnerConditional
    