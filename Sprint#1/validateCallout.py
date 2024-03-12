import os
from displayGrid import return_stateful_list

# this checks against all previous player guesses
'''
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

'''


def validate_callouts(latest_grid, all_guess, last_player):
    # checks against previous guesses
    players_dict = all_guess
    player_name = last_player

    # checks in the grid
    _list = latest_grid
    # print(_list)

    counter = 0
    for sub_list in _list:
        if sub_list[1] == players_dict[player_name][-1][1]:
            if sub_list[3] is '1' and (sub_list[1].upper()) == "JOKER":
                counter += 1

    # print(f"count of card {counter}")
    if counter is 5:
        print("All 5 Jokers are Faced up!\n")
    elif counter is 1:
        return "none"

    # Get the list of players
    players = list(players_dict.keys())

    # Find the index of the given player
    player_index = players.index(player_name)

    # Get the index of the previous player
    previous_player_index = (player_index - 1) % len(players)

    # Check if the given player and the previous player have any cards
    if not players_dict[player_name] or not players_dict[players[previous_player_index]]:
        print(f"{player_name} or {players[previous_player_index]} doesn't have any guessed cards yet.")
        return "none"

    # Compare the last cards of the given player and the previous player
    match = players_dict[player_name][-1][1:3] == players_dict[players[previous_player_index]][-1][1:3]

    # If the cards match, print the player name and the rank and suit that matched
    if match:
        _, rank, suit, _ = players_dict[player_name][-1]
        print(f"{player_name}'s last card {rank} of {suit} matches with {players[previous_player_index]}'s last card.")
        return "player"

    for sub_list in _list:
        if sub_list[1:3] == players_dict[player_name][-1][1:3]:
            if sub_list[3] is '1':
                print(f"Valid Callout\nThe card player guessed is already flipped, the card is {sub_list}")
                return "grid"
            else:
                return "none"
