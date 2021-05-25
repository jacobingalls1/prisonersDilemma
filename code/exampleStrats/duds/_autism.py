import random


def tftVaccine(history):
    for i in range(history.shape[1]-1):#check if opponent is tftlike
        if history[0][i]!=history[1][i+1]:
            return None
    return 1

def simpletonVaccine(history):
    for i in range(history.shape[1]-1):#check if opponent is simpletonlike
        if history[0][i] and history[0][i]!=history[1][i+1]:
            return None
        elif history[0][i]==history[1][i+1]:
            return None
    return history[1][-1]

def defectVaccine(history):
    if len([i for i in history[1] if i == 0])==len(history[1]):
        return 0
    return None

def spiteVaccine(history):
    LOOKBACK=10
    SPITE_FACTOR=.9
    if history.shape[1]<LOOKBACK:
        return None
    if len([i for i in history[1][-LOOKBACK:] if i == 0]) > SPITE_FACTOR*len([i for i in history[0][-LOOKBACK:] if i == 0]):
        return 1
    return 0

vaccines = [tftVaccine, simpletonVaccine, defectVaccine, spiteVaccine]



def goodDeal(history):
    return len([i for i in history[1] if i == 1])==len(history[1])



def strategy(history, memory):
    choice = 1  # this is the default/first turn choice
    if history.shape[1] == 0:
        return choice, None
    else:
        votes = []
        for v in vaccines:
            v = v(history)
            if v is not None:
                votes.append(v)
        if votes:
            choice = round(sum(votes)/len(votes))
        if goodDeal(history):
            choice = 1
    return choice, None
