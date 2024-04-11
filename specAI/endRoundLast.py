# from endRoundScoring import gameScores
# from endRoundCondition import winnerConditional

def endRoundLast(winnerConditional, gameScores):
        if not winnerConditional:
        
            #Find the maximum score
            maxScore = max(gameScores.values())

            #display the top scorer as a winner and if there is a tie, display them as a tie
            winners = [player for player, score in gameScores.items() if score == maxScore]

            if len(winners) == 1:
                print(f"\nThe top scorer and the winner is Player {winners[0]} with a score of {maxScore}.")
                # Print the total scores
                print("\nTotal Scores:")
                for key, value in gameScores.items():
                    print(f"Player {key}: {value}") 
            else:
                print("\nThere is a tie between the following players:")
                for winner in winners:
                    print(f"Player {winner} with a score of {maxScore}.")
                # Print the total scores
                print("\nTotal Scores:")
                for key, value in gameScores.items():
                    print(f"Player {key}: {value}")           
        else:
             return True