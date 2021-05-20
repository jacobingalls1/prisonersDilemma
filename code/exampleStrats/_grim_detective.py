import random
import numpy as np


def strategy(history, memory):  # detective that turns into grim trigger instead of tft
    testingSchedule = [1, 0, 1, 1]
    gameLength = history.shape[1]
    shallIExploit = None
    if memory is not None:
        shallIExploit = memory[0]
    choice = None

    if gameLength < 4:  # We're still in that initial testing stage.
        choice = testingSchedule[gameLength]
    elif gameLength == 4:  # Time to analyze the testing stage and decide what to do based on what the opponent did in that time!
        opponentsActions = history[1]
        if np.count_nonzero(opponentsActions - 1) == 0:  # The opponent cooperated all 4 turns! Never defected!
            shallIExploit = True  # Let's exploit forever.
        else:
            shallIExploit = False  # Let's switch to Grim Trigger

    if gameLength >= 4:
        if shallIExploit:
            choice = 0
        else:
            # Do Grim Trigger
            wronged = False
            if memory is not None and memory[1]:  # Has memory that it was already wronged.
                wronged = True
            else: # Has not been wronged yet, historically.
                if history.shape[1] >= 1 and history[1,-1] == 0:  # Just got wronged.
                    wronged = True

            if wronged:
                return 0, [False, True]
            else:
                return 1, [False, False]

    return choice, [shallIExploit, False]
