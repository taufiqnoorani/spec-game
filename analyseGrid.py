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

def give_scorecards_callout(to_player, from_player, scorecards, players_dict, mode):

    if mode is "grid":
        print(f"Scorecards will be assigned from the Scorecard pile to: {to_player}")
        players_dict(to_player).append(scorecards.pop(-1))
        return players_dict
    else:
        # Check if the specific player has any cards
        if not players_dict[from_player]:
            print(f"{from_player} does not have any Scorecards yet, \nScorecards will be assigned from the Scorecard pile to: {to_player}")
            players_dict[to_player].append(scorecards.pop(-1))
            return players_dict

        print(f"Highest scorecard will be given from {from_player} -> {to_player}")
        # Get the card with the highest value in the first index from the specific player
        highest_card = max(players_dict[from_player], key=lambda card: card[0])

        # Remove the highest card from the specific player's cards
        players_dict[from_player].remove(highest_card)

        # Add the highest card to the other player's cards
        players_dict[to_player].append(highest_card)

        return players_dict

def assign_scorecards(player_scores, scorecards, score, playerName):

    #print(score)
    for x in range (0,score):
        s = scorecards.pop(-1)
        player_scores[playerName].append(s)

    return player_scores
