def endRoundScoring(player_scores, bonusPlayer, bonusPoints, namePlayers, gameScores): 

    #add scores of players after every round
    for key, value in player_scores.items():
        totalSum = sum(int(item[0]) for item in value)
        
        #add pre-round scores to final gameScore after every round
        if key == bonusPlayer:
            totalSum += bonusPoints
        gameScores[key] += totalSum

    #Display game scores after the round
    print(f"\nThe scores at the end of this round is: {gameScores}")   
    
    # Update player order from namePlayers
    namePlayers.append(namePlayers.pop(0))    
    return gameScores