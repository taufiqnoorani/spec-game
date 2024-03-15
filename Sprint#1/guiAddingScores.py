#card = ["position, "rank", "suite", "flip"]
#guess = ["rank", "suite"]
#retrun the number of scorecards to assign to the player
def addingScoresGUI(card, guess):
    score = 0

    if guess[0] == 'Joker' and card[1] == 'Joker': #Real joker found
        score = 4
    if guess[0] == 'Joker' and card[1] == '2': #False joker found
        score = 2
    if guess[0] == card[1] and guess[1] == card[2]: #Correct rank and suit
        score = 4
    if guess[0] == card[1] and guess[1] != card[2]: #Correct rank incorrect suit
        score = 2
    if guess[0] != card[1] and guess[1] == card[2]: #Incorrect rank correct suit
        score = 1
    return score
