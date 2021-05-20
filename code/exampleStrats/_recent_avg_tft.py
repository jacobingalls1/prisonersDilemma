import random


def strategy(history, memory):  # defects if opponent has mostly defected recently
    choice = 1  # this is the default/first turn choice
    if history.shape[1] == 0:
        return choice, None
    else:
        choices = [0, 0]
        LOOKBACK = 10  # number of responses to review (about 10 seems best experimentally)
        for i in range(-1, -1 - LOOKBACK, -1):
            if history.shape[1] + i < 0:
                break
            choices[history[1][i]] += 1
        if choices[0] >= choices[1]:
            choice = 0
    return choice, None
