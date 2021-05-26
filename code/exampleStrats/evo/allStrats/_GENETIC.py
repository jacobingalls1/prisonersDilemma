import random
import numpy as np

THRESHHOLD = .5
BIAS_SPEED = .01
WEIGHT_SPEED = .01


def sigmoid(z):
    return 1/(1+np.exp(-z))

class GeneticAgent:
    def __init__(self, dna=None, layers=None):
        self.weights = []
        self.biases = []
        self.layers = layers
        if dna:
            self.readIn(dna)
        else:
            self.fillRandom()

    def fillRandom(self):
        layers = self.layers
        for i in range(len(layers)-1):
            self.weights.append(np.random.randn(layers[i+1], layers[i])*.01)
            self.biases.append(np.zeros((layers[i+1], 1)))

    def writeOut(self, outfile):
        self.jitter(0)
        np.save(outfile, (self.weights, self.biases))

    def readIn(self, infile):
        self.weights,self.biases = np.load(infile, allow_pickle=True)

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

    def strategy(self, history, memory):
        return self.decide(history), None

    def jitter(self, gen):
        LWEIGHT_SPEED=WEIGHT_SPEED/(round(gen*.01)+1)
        LBIAS_SPEED=BIAS_SPEED/(round(gen*.01)+1)
        layers = self.layers
        for i in range(len(layers)-1):
            self.weights[i]+=np.random.randn(layers[i+1], layers[i])*LWEIGHT_SPEED*random.choice([1,-1])
            self.biases[i]+=np.random.randn(layers[i+1], 1)*random.choice([1,-1])*LBIAS_SPEED

def populate(numFiles, outDirectory, layers):
    for i in range(numFiles):
        GeneticAgent(None, layers).writeOut(outDirectory+'/'+str(i))



weights = [np.array([[ 1.3156708 , -0.06345499, -0.45226876, -2.03770417,  0.43532086,
        -1.35123679,  0.3097804 ,  0.65780887, -0.88199779,  0.07201888],
       [ 0.38581836,  0.7788426 , -0.23364427,  0.73452076,  0.94285003,
        -0.83382009, -0.16284507, -1.02228062,  0.65043522,  0.44610165],
       [ 0.25030269,  0.73434598,  1.7921289 , -1.51533852,  0.30027864,
        -0.49795393, -1.11081617, -0.3716306 ,  0.83925858, -0.5760265 ],
       [-1.64454069, -0.91833713,  0.13202752,  0.7596618 , -0.61277564,
         0.7607113 , -1.36994016, -0.25651041, -0.006933  , -0.07059727],
       [ 0.15753643,  0.51371984, -0.61335454,  0.47880958,  0.63078044,
         0.27644348, -0.42255398,  0.43533659,  1.83738955,  0.31073763]]),
 np.array([[ 5.60134491e-02,  1.79517488e-01,  7.58876374e-01,
         8.56516910e-01,  6.74704810e-01],
       [-1.48327319e+00,  2.19004283e-01,  1.38277577e+00,
        -5.15301404e-01,  1.16230578e+00],
       [ 8.74659794e-02,  1.36477080e-01,  1.10013048e+00,
         7.77831203e-01,  7.74335708e-01],
       [ 5.67829561e-01,  1.74928644e+00,  2.13967929e-01,
         3.23334340e-01, -3.79142502e-02],
       [ 2.12287660e-04,  8.77904888e-01, -2.52560657e+00,
        -1.07912821e+00, -1.52465904e+00]]),
 np.array([[-0.51794736, -0.73717867,  0.38397342, -1.17758741,  0.70068552]])]
biases = [np.array([[-0.15459512],
       [ 0.70159918],
       [-0.13636501],
       [-0.14483145],
       [-0.04526038]]),
 np.array([[ 1.52124544],
       [ 0.68953162],
       [ 0.23476264],
       [-0.87880705],
       [-0.55054054]]),
 np.array([[1.31722364]])]











def strategy(history, memory):
    if not memory:
        memory = GeneticAgent(None, [10,5,5,1])
        memory.weights = weights
        memory.biases = biases
    return memory.decide(history), memory





















