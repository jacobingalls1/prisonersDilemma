def should_exploit(history, memory):  # exploit if it usually works
    should = True
    if memory[0][1] == 0:  # first time trying
        return True, memory
    if memory[0][0] / memory[0][1] < 0.5:
        should = False
    return should, memory


def should_cooperate(history, memory):  # cooperate if it usually works
    should = True
    if memory[1][1] == 0:  # first time trying
        return True, memory
    if memory[1][0] / memory[1][1] < 0.5:
        should = False
    return should, memory


def strategy(history, memory):  # tries to find a stable state, preferably where i exploit my opponent
    choice = 1  # this is the default/first turn choice
    if history.shape[1] == 0:
        # memory = [[successful_exploits, exploit_attempts], [successful_cooperates, cooperate_attempts], previous case]
        return choice, [[0, 0], [0, 0], 0]

    if memory[2] == 1:
        memory[0][1] += 1
        memory[0][0] += history[1][-1]
    elif memory[2] == 3:
        memory[0][1] += 1
        if history[0][-1] == 0:  # i tried to exploit
            memory[1][0] += history[1][-1]
    elif memory[2] == 4:
        memory[2] = -1
        return history[0][-1], memory
    elif memory[2] == -1:
        memory[1][1] += 1
        memory[1][0] += history[1][-1]

    if history[0][-1] == 0 and history[1][-1] == 1:  # case 1: i just exploited opponent
        memory[2] = 1
        return 0, memory
    elif history[0][-1] == 1 and history[1][-1] == 0:  # case 2: opponent just exploited me
        memory[2] = 2
        return 0, memory
    elif history[0][-1] == 1 and history[1][-1] == 1:  # case 3: we both just cooperated
        memory[2] = 3
        choice, memory = should_exploit(history, memory)
        choice = not choice
    elif history[0][-1] == 0 and history[1][-1] == 0:  # case 4: we both just defected
        memory[2] = 4
        choice, memory = should_cooperate(history, memory)
    return choice, memory
