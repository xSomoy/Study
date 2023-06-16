import numpy as np

np.random.seed(0)

X = [[1, 2, 3, 2.5],
     [2.0, 5.0, -1.0, 2.0],
     [-1.5, 2.7, 3.3, -0.8]]


class Layer_Dense:
    def __init__(self):
        pass
    def forward(self):
        pass


# ----------------------------------------- #
# # layer 1
# inputs = [[1, 2, 3, 2.5],
#           [2.0, 5.0, -1.0, 2.0],
#           [-1.5,2.7,3.3,-0.8]]

# weights = [[0.2, 0.8, -0.5, 1.0],
#            [0.5, -0.91, 0.26, -0.5],
#            [-0.26, -0.27, 0.17, 0.87]]

# biases = [2, 3, 0.5]

# # layer 2

# weights2 = [[0.1, -0.14, 0.5],
#            [-0.5, 0.12, -0.33],
#            [-0.44, 0.73, -0.13 ]]

# biases2 = [-1, 2, -0.5]


# layer1_outputs = np.dot(inputs, np.array(weights).T) + biases
# layer2_outputs = np.dot(layer1_outputs, np.array(weights2).T) + biases2

# print(layer2_outputs)


# ------------------------------------------------------------------------------- #

# outputs = np.dot(weights, np.array(inputs).T) + biases #does work
# outputs = np.dot(np.array(weights).T, inputs) + biases #doesn't work

# print(layer2_outputs)
