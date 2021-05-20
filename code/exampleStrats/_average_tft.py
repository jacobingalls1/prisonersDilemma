def strategy(history, memory):  # defect if opponent has mostly defected
    choice = 1
    if history.shape[1] >= 1:
        avg_choice = 0
        for choice in history[1]:
            avg_choice += choice
        avg_choice /= history.shape[1]
        if avg_choice <= 0.5:
            choice = 0
    return choice, None
