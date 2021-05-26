import random
import numpy as np

THRESHHOLD = .5

def sigmoid(z):
    return 1/(1+np.exp(-z))

class GeneticAgent:
    def __init__(self, layers=None):
        self.weights = []
        self.biases = []
        self.layers = layers

    def predict(self, X):
        Z = X
        for i in range(len(self.layers)-2):
            Z = np.tanh(np.dot(self.weights[i], Z)+self.biases[i])
        return sigmoid(np.dot(self.weights[-1], Z)+self.biases[-1])

    def decide(self, history):
        IN_LAYER = self.layers[0]
        X=np.zeros((IN_LAYER,1))+.5
        if history.shape[1]<IN_LAYER/2:
            for i in range(history.shape[1]):
                X[i]=history[0][i]
                X[int(i+IN_LAYER/2)]=history[1][i]
        else:
            for i in range(int(IN_LAYER/2)):
                X[i]=history[0][-int(IN_LAYER/2-i)]
                X[int(i+IN_LAYER/2)]=history[1][-int(IN_LAYER/2-i)]
        prediction = self.predict(X)[0,0]
        return prediction>THRESHHOLD

weights = [np.array([[ 1.30990505, -0.06468201, -0.46950911, -2.02245323,  0.42620721,
        -1.37370777,  0.30836363,  0.65407862, -0.9105383 ,  0.09767235],
       [ 0.38871475,  0.79181999, -0.2702231 ,  0.73337662,  0.96175165,
        -0.8550377 , -0.18222975, -0.99995231,  0.64691077,  0.43077896],
       [ 0.25518624,  0.72894703,  1.79299686, -1.50061381,  0.27741656,
        -0.48354261, -1.10852133, -0.39681925,  0.85722985, -0.56128393],
       [-1.65607598, -0.90567922,  0.13574025,  0.76196196, -0.63033259,
         0.73868959, -1.37081178, -0.25442325,  0.01497708, -0.07469577],
       [ 0.1234429 ,  0.55146133, -0.60363845,  0.4972716 ,  0.62092348,
         0.26755567, -0.43505104,  0.40581611,  1.86748107,  0.32704326]]),
 np.array([[ 0.06850804,  0.19885511,  0.74956799,  0.84055963,  0.64902676],
       [-1.50210092,  0.20538305,  1.43107796, -0.49334454,  1.16815121],
       [ 0.06754536,  0.15098483,  1.08040988,  0.79294101,  0.78918854],
       [ 0.56643139,  1.71831393,  0.17554512,  0.28595594, -0.01323947],
       [ 0.03852699,  0.90508678, -2.50633483, -1.10937125, -1.51624776]]),
 np.array([[-0.53504735, -0.75104322,  0.38708203, -1.16713954,  0.68290754]])]
biases=[np.array([[-0.14920893],
       [ 0.69170856],
       [-0.14018873],
       [-0.14134704],
       [-0.04847876]]),
 np.array([[ 1.53266309],
       [ 0.71234386],
       [ 0.2366763 ],
       [-0.87470679],
       [-0.53490642]]),
 np.array([[1.31665168]])]


def strategy(history, memory):
    if not memory:
        memory = GeneticAgent([10,5,5,1])
        memory.weights = weights
        memory.biases = biases
    return memory.decide(history), memory





















