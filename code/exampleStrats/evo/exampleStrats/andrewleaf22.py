import random
import numpy as np
# Reminder: For the history array, "cooperate" = 1, "defect" = 0

def predict(them, me, gl):
    if np.count_nonzero(them-1) == 0:
        #if they always defect
        return 0
    elif np.count_nonzero(them-1) == gl:
        #print("All cooperate")
        return 1
    elif np.count_nonzero(them-1)*3 <= gl:
        #print("Less defects than not, with 33%")
        return 0
    elif np.count_nonzero(them-1)*1.5 >= gl:
        #print("More defects than not, with 33%")
        return 1
    else:
        #print("Unsure")
        return 2 #unsure

def strategy(history, memory):
    gameLength = history.shape[1]
    actions = ["defect", "cooperate"]
    if(type(memory) is list):
        mymoves = memory
    else:
        mymoves = []
    #testorder length is 5
    choice = random.randint(0,1)
    opponentActions = history[1]
    if gameLength > 0:
        lastMove = history[1,-1]

    if gameLength > 0:
        theirmoves = history[1]
        prediction = predict(theirmoves, mymoves, gameLength) #predicts next move
        if prediction == 1: #if i predict the other person cooperates, i won't cooperate
            choice = 0
        elif prediction == 0:
            choice = 0
        else: #unsure, so cooperates to be safe
            choice = 1

    mymoves.append(choice)

    return actions[choice], mymoves
