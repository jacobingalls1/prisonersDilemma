import random


def strategy(history, memory):  # joss but frequency of defection depends on opponent's responses to defection

    # choice = 1
    # if random.random() < 0.10 or (history.shape[1] >= 1 and history[1,-1] == 0):
    #     # Choose to defect randomly by 10% chance, OR if and only if the opponent just defected.
    #     choice = 0
    # return choice, None

    choice = 1
    if history.shape[1] == 0:
        return 1, [1, 2, 0]  # memory is [unpunished_defections, unprovoked_defections, just_defected_unprovoked]
    if history[1][-1] == 0 and memory[2] == 0:  # defecting because opponent just defected unprovoked
        choice = 0
    elif random.random() < (memory[0] / memory[1]):  # defecting randomly
        choice = 0
        memory[2] = 2  # cooperate for 2 turns unless I decide to randomly defect again
        memory[1] += 1
        memory[0] += history[1][-1]
    elif memory[2] > 0:
        if not history[1][-2]:
            memory[0] += history[1][-1]
        memory[2] -= 1
    return choice, memory
