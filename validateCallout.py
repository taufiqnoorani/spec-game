import os
from displayGrid import return_stateful_list


def validate_callouts(user_input):

    #TODO: check against previous player guesses if any

    print("\n" * 100)
    _list = return_stateful_list()
    print(_list)
    for sub_list in _list:
        if sub_list == user_input:
            if sub_list[2] is '1':
                return f"Valid Callout\nThe card player guessed is already flipped, the card is {sub_list}"
            else:
                return "In-Valid Callout"




#TODO: award showcards