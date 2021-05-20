def strategy(history, memory):  # grim trigger that forgets grudge every once in a while
    wronged = False
    MEMORY_TIME = 10  # forgets grudge every this many turns
    if memory is None:
        memory = 0
    if memory > 0:  # Has memory that it was already wronged.
        wronged = True
    elif memory == -1:
        wronged = False
    else:  # Has not been wronged yet, historically.
        if history.shape[1] >= 1 and history[1, -1] == 0:  # Just got wronged.
            wronged = True
            memory = 1
    if memory is not None and memory % MEMORY_TIME == 0 and history.shape[1] != 1:
        return 1, -1

    if wronged:
        return 0, memory + 1
    else:
        return 1, 0
