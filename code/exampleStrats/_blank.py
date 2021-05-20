import random


def strategy(history, memory):
    choice = 1  # this is the default/first turn choice
    if history.shape[1] == 0:
        return choice, None
    else:
        # history[0] is the list of your choices, history[1] is the list of the opponent's
        # now make your move
        pass
    return choice, None
