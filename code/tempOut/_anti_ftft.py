def strategy(history, memory):  # alternates defecting and cooperating
    choice = 0
    if (history.shape[1] + 1) % 2:
        choice = 1
    return choice, None