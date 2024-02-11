def addingScores(card, guess):
    score = 0
    message = ""

    guess[3] = '1'

    card[1] = card[1].upper()
    card[2] = card[2].upper()

    print(card)
    print(guess)

    if card[0] == guess[0]:  # If the position matches
        if card[1] == guess[1] and card[2] == guess[2]:  # If the rank and suit match
            score = 4  # Exact card guessed
            message = "Exact card guessed."
        elif card[1] == guess[1]:  # If only the rank matches
            score = 2  # Card of the same rank
            message = "Rank matches."
        elif card[2] == guess[2]:  # If only the suit matches
            score = 1  # Card of the same suit
            message = "Suit matches."
            if card[1] == "JOKER":  # If the card is a Joker of the suit called
                score = 2  # Joker of the suit called
                message = "Joker found as deuce."
        if card[1] == "JOKER" and card[2] == "JOKER":  # If the card is the real Joker
            score = 4  # Real Joker guessed
            message = "Real Joker found."

    return score, message  # Return the score
