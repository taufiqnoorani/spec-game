def analyse_grid(grid):
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


# TODO: end of turn logic?  award showcards? check predictions?

def endofturnlogic(player_names, current_player):
    print("")


def updatedGrid():
    return updatedGrid


def assign_scorecards(player_scores, scorecards, score, playerName):

    print(score)

    for x in range (0,score):
        s = scorecards.pop(-1)
        player_scores[playerName].append(s)

    return player_scores
