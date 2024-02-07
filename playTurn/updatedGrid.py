def updatedGrid(grid, guess):
    for card in grid:
        if card[0] == guess[0]:  # If the position matches.
            card[3] = 1  # Flip the card.
            print(f"{card[1]},{card[2]}")# Reveals the actual value of the card.
            break  # Exit the loop as the card has been found.
    return grid  # Return the updated grid. Store this as updatedGrid to add to other functions.