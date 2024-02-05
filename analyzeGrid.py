def analyze_grid(grid):
    flipped, un_flipped = 0,0
    for sub_list in grid:
        if sub_list[2] is '1':
            flipped += 1
        else:
            un_flipped += 1

    if flipped is 1:
        return "There is only 1 card left to predict"
    else:
        return f"There are {un_flipped} cards left un-flipped"

# TODO: end of turn logic?  award showcards? check predictions?
