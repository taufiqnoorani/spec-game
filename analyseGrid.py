def analyse_grid(grid):
    flipped, un_flipped = 0,0
    for sub_list in grid:
        if sub_list[3] is '0':
            flipped += 1
        else:
            un_flipped += 1

    if flipped is 1:
        return True
    else:
        return False

#TODO: end of turn logic?  award showcards? check predictions?

def endofturnlogic(player_names,current_player):
    print("")

def updatedGrid():
    return updatedGrid