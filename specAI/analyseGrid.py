def analyseGrid(grid):
    flipped, un_flipped = 0, 0
    for sub_list in grid:
        if sub_list[3] is '0':
            flipped += 1
        else:
            un_flipped += 1

    if flipped is 1:
        return True
    else:
        return False
    


def updatedGrid(grid, guess):
    global card
    for i, card in enumerate(grid):
        if card[0] == guess[0]:  # If the position matches.
            print(f"{card[1]},{card[2]}")# Reveals the actual value of the card.
            grid[i][3] = '1'
            print(grid[i])
            break  # Exit the loop as the card has been found.
    #print(grid)
    return grid, card  # Return the updated grid. Store this as updatedGrid to add to other functions.



def assignScorecards(playerScores, scorecards, score, playerName):
    # print(score)
    for x in range(0, score):
        s = scorecards.pop(-1)
        playerScores[playerName].append(s)

    return playerScores
