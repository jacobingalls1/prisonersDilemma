import random
import numpy as np


def strategy(history, memory):  # defects until opponent cooperates, then cooperates forever
    righted = False
    if memory is not None and memory:  # Has memory that it was already righted.
        righted = True
    else:  # Has not been wronged yet, historically.
        if history.shape[1] >= 1 and history[1][-1] == 1:  # Just got righted.
            righted = True

    if righted:
        return 1, True
    else:
        return 0, False
