import numpy as np 

inputs = [[1,2,3, 5],
          [4,5,6,7],
          [8,9,10,11]] # this is a matrix

weights= [[3.1, 2.1, -8.7, 2.3],
          [3.2, -1.5, 8.5, -2.2], # this is a matrix
          [2.9, -2.5, 8.1, 2.1]]
biases = [2,3,.5]

#second layer 

weights2= [[3.5, 2.0, -8.1, 2.5],
          [3.1, -1.3, 8.4, -2.1], # this is a matrix
          [2.1, -2.3, 8.5, 2.2]]
biases2 = [1,2,.7]


layer1_outputs = np.dot(weights, np.array(weights).T) + biases
#neurons will be indexed by the weights sets so weights will come to the left 

layer2_outputs = np.dot(weights, np.array(weights2).T) + biases2

print(layer2_outputs)

#batch size is a num of samples of processed before the model is updated. common batch is 32