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


weights = [np.array([[ 1.17747033, -0.02975157, -0.43122277, -2.14886702,  0.37617273,
        -1.3652631 ,  0.30573938,  0.67046473, -0.89104837, -0.0233649 ],
       [ 0.32378875,  0.74747823, -0.29064687,  0.69743181,  0.95384753,
        -0.8463167 , -0.24267846, -0.98810972,  0.70059448,  0.48076793],
       [ 0.35079622,  0.74001408,  1.82623748, -1.50404513,  0.27257944,
        -0.39780433, -1.17527589, -0.46569927,  0.94633632, -0.68873327],
       [-1.52065809, -0.85719279,  0.17887938,  0.73897582, -0.68224516,
         0.77677957, -1.48720582, -0.32362612,  0.03868756, -0.09812734],
       [ 0.14226789,  0.42854605, -0.6680759 ,  0.45539046,  0.53649179,
         0.23670054, -0.49102137,  0.40713694,  1.94046364,  0.25647686]]),
 np.array([[ 0.03282814,  0.0976162 ,  0.6734484 ,  0.90335391,  0.69558285],
       [-1.35429266,  0.19753559,  1.44986424, -0.55965636,  1.15782934],
       [ 0.17727426,  0.14433189,  1.02449439,  0.63689206,  0.77046233],
       [ 0.48414121,  1.73979494,  0.32922986,  0.36504384, -0.00405219],
       [ 0.01637543,  1.02393696, -2.51604262, -1.06862891, -1.3813841 ]]),
 np.array([[-0.58327681, -0.6370742 ,  0.24670029, -1.13617521,  0.71288481]])]

biases = [np.array([[-0.11563371],
       [ 0.72803716],
       [-0.18837729],
       [-0.2188207 ],
       [-0.08173032]]),
 np.array([[ 1.6186246 ],
       [ 0.69675001],
       [ 0.3240026 ],
       [-0.8625214 ],
       [-0.60192149]]),
 np.array([[1.37181065]])]


def strategy(history, memory):
    if not memory:
        memory = GeneticAgent(None, [10,5,5,1])
    return memory.decide(history), memory





















