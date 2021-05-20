def strategy(history, memory):
    choice = 0 #this is the default/first turn choice
    if history.shape[1]== 0:
        return choice, None
    #history[0] is the list of your choices, history[1] is the list of the opponent's
    #now make your move
    return choice, None
