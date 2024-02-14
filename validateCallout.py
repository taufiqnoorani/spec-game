import os
from displayGrid import return_stateful_list


def validate_callouts(latest_grid, all_guess, last_player):
    # checks against previous guesses
    players_dict = all_guess
    player_name = last_player

    _, player_last_card_rank, player_last_card_suit, _ = players_dict[player_name][-1]
    user_input = ['0', player_last_card_rank, player_last_card_suit, '0']
    # Iterate over all players in the dictionary
    for player, cards in players_dict.items():
        # Skip the player we are comparing
        if player == player_name:
            continue

        # Check each card's rank and suit of the current player
        for _, rank, suit, _ in cards:
            # If the rank and suit are the same as the specific player's last card's rank and suit, print the player, rank and suit
            if rank == player_last_card_rank and suit == player_last_card_suit:
                print(f"{player} has the same card: {rank} of {suit}")
                return "player"

    # checks in the grid
    _list = latest_grid
    #print(_list)
    for sub_list in _list:
        if sub_list[1:3] == user_input[1:3]:
            if sub_list[3] is '1':
                print(f"Valid Callout\nThe card player guessed is already flipped, the card is {sub_list}")
                return "grid"
            else:
                return False

