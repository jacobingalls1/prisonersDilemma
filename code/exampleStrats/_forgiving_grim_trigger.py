def strategy(history, memory):  # grim trigger that will forgive the opponent once
    wronged = False
    FORGIVE_TIME = 5
    if memory is not None:
        if memory == FORGIVE_TIME + 1:
            memory = 0
        elif memory > 0 or (memory == 0 and history[1][-1] == 0):  # 0 indicates has been wronged once, -1 indicates wronged twice
            wronged = True
            memory -= 1
            if memory == 0:
                memory = FORGIVE_TIME + 1
                wronged = False
        elif memory == -1:
            wronged = True
    elif history.shape[1] >= 1:
        if history[1][-1] == 0:
            wronged = True
            memory = FORGIVE_TIME

    if wronged:
        return 0, memory
    else:
        return 1, memory
