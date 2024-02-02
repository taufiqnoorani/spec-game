def playerTurn(player, players, roundScores):
    print(f"\n{player}'s turn:")
    #display_grid()

    # Take input from the player for their call
    userInput = input("Make your call (e.g., '5,5 Q,H' for row 5, column 5, and guess Queen of Hearts): ")

    # Split the input into row, column, and guess
    try:
        row, col, guess = map(str.strip, userInput.split())
        row, col = int(row), int(col)
    except ValueError:
        print("Invalid input format. Please try again.")
        return

    # Validate the row and column values
    if not (1 <= row <= 5 and 1 <= col <= 5):
        print("Invalid row or column. Please choose values between 1 and 5.")
    return