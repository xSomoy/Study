# Softmax Activision Function = Exponentiate > Normalize > Output
import math
import numpy as np
import nnfs
nnfs.init()

layer_outputs = [[4.8, 1.12, 2.385],
                 [8.9, -1.81, 0.2],
                 [1.41, 1.051, 0.026]]

E = math.e

exp_values = np.exp(layer_outputs)

norm_values = exp_values / np.sum(exp_values)

print(norm_values)
print(sum(norm_values))
