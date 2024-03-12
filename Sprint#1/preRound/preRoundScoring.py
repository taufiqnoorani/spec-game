#lastcard: list
#lastScorecardWinner: str
#scorecards: list
def preRoundScoring(predictions, lastCard, lastScorecardWinner, scorecards):
    # Initializing variables to keep track of bonus points and the player who receives them.
    bonusPoints = 0
    bonusPlayer = None

    # Checks if any player predicted the correct card.
    if lastCard in predictions.values():
        # The player that correctly predicted the last card wins all the remaining scorecards.
        bonusPlayer = list(predictions.keys())[list(predictions.values()).index(lastCard)]
        print(f"Congratulations! The correct card {lastCard} was predicted!")
        print(f"{bonusPlayer} wins all remaining scorecards!")
    else:
        correctRank = lastCard[1]
        correctSuit = lastCard[2]

    #Converting socrecards to int
    scorelist = []
    for card in scorecards:
        scorelist.append(int(card[0]))

        #If no player predicted the correct card, this bonus goes to the player who predicted the correct rank.
    for player, prediction in predictions.items():
        if prediction[0] == correctRank:
            bonusPlayer = player
            bonusPoints = sum(scorelist) if scorelist else 10
            print(f"Although the correct card was not predicted, {player} predicted the correct rank {correctRank}!")
            print(f"{player} wins all remaining scorecards!")
            break
        #If no player predicted the correct card and the correct rank, this bonus goes to the player who predicted the correct suit.
        elif prediction[1] == correctSuit:
            bonusPlayer = player
            bonusPoints = sum(scorelist) if scorelist else 10
            print(f"Although the correct card or rank was not predicted, {player} predicted the correct suit {correctSuit}!")
            print(f"{player} wins all remaining scorecards!")
            break

    # If no player predicted the correct card, rank or suit, this bonus goes to the player who won the last scorecard.
    if lastScorecardWinner:
        if not bonusPlayer:
            if lastScorecardWinner:
                bonusPlayer = lastScorecardWinner
                bonusPoints = sum(scorelist) if scorelist else 10
                print(f"No player predicted the correct card, rank, or suit.")
                print(f"The last scorecard winner {lastScorecardWinner} wins all remaining scorecards!")
            else:
                print("No player predicted the correct card, rank, or suit, and there are no previous scorecard winners.")
                print("No one gets any bonus points.")

    return bonusPlayer, bonusPoints