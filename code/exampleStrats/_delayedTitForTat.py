def strategy(history, memory):
    LOOKBACK = 1
    choice = 1
    if history.shape[1] >= LOOKBACK and history[1,-LOOKBACK] == 0: # Choose to defect if and only if the opponent just defected.
        choice = 0
    return choice, None
