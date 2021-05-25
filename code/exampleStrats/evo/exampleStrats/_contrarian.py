def strategy(history, memory):  # does the opposite of what the opponent just did
    choice = 1
    if history.shape[1] >= 1 and history[1][-1] == 1:
        choice = 0
    return choice, None
