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



def strategy(history, memory):
    if type(memory) == str:
        memory = GeneticAgent(memory)
    return memory.decide(history), memory


#populate(10, 'genepool')
'''
g = GeneticAgent('genepool/0.npy')
print(strategy(np.zeros((2,1), dtype=float), g))
'''



















