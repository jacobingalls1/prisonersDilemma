import sys
import numpy as np

np.set_printoptions(threshold=sys.maxsize)

weights, biases = np.load(sys.argv[1], allow_pickle=True)

print(weights)
print(biases)




