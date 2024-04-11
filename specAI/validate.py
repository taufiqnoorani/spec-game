def validateCallouts(latestGrid, allGuesses, lastPlayer):
    playersDict = allGuesses
    playerName = lastPlayer
    currentCard = playersDict[playerName][-1]

    # Check if the current player guessed a Joker when all Jokers are flipped
    if currentCard[1].upper() == "JOKER":
        jokerCounter = sum(1 for card in latestGrid if card[1].upper() == "JOKER" and card[3] == '1')
        if jokerCounter >= 5:
            return "jokerAllFlipped"

    # Check if the current player's guess matches the previous player's guess
    previousPlayerGuess = playersDict[list(playersDict.keys())[1 - list(playersDict.keys()).index(playerName)]][-1]
    if currentCard[1:] == previousPlayerGuess[1:]:
        return "sameGuess"

    # Check if the current player's guess matches any flipped card in the grid
    for card in latestGrid:
        if card[1:] == currentCard[1:]:
            if card[3] == '1':
                return "flippedCardMatch"

    return "valid"