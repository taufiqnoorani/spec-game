def guess(names, updatedGrid):
    rankMap = {"A": "ACE", "K": "KING", "Q": "QUEEN", "J": "JACK", "10": "10", "JOKER": "JOKER"}
    suitMap = {"H": "HEARTS", "D": "DIAMONDS", "C": "CLUBS", "S": "SPADES", "JOKER": "JOKER"}

    currentPlayer = names

    while True:
        userInput = input(f"Make your call: Player -> {currentPlayer}: ")
        try:
            position, guess = map(str.strip, userInput.split())
            position = int(position)
            guess = list(map(str.strip, guess.split(',')))  # Convert to list and split by comma
            rank = guess[0].upper()

            if rank == "JOKER":
                suit = "JOKER"
            else:
                suit = guess[1].upper()

            if rank not in rankMap or suit not in suitMap:
                raise ValueError("Invalid rank or suit.")

            # If we've reached this point, the input is valid and we can break the loop
            break
        except ValueError as e:
            print(f"Invalid input: {e}")
        except IndexError:
            print("Invalid input: not enough values provided.")


    n = str(position)
    guess = [n, rank, suit, '0']
    return guess, currentPlayer  # Return the guess and the last player.
