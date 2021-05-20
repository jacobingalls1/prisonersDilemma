import random


def strategy(history, memory):  # makes a weighted random choice from recent responses
    choice = 1  # this is the default/first turn choice
    if history.shape[1] == 0:
        return choice, None
    else:
        # history[0] is the list of your choices, history[1] is the list of the opponent's
        # now make your move
        totals = [0, 0]
        LOOKBACK = 2  # number of responses to review
        i = None
        for i in range(-1, -1 - LOOKBACK, -1):
            if history.shape[1] + i < 0:
                break
            totals[history[1][i]] += 1
        choice = random.choices([0, 1], weights=totals)[0]
    return choice, None
