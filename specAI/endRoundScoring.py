def endRoundScoring(playerScores, bonusPlayer, bonusPoints, nameOfPlayers, gameScores):
        for player in nameOfPlayers:
            gameScores[player].append(playerScores[player])
        gameScores[bonusPlayer] .append(playerScores[player])
        return gameScores
