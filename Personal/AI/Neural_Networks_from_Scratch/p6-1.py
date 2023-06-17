# Softmax Activision Function
import math

layer_outputs = [4.8, 1.12, 2.385]

E = math.e

# E = 2.71828182846
# print(E)

exp_values = []
for output in layer_outputs:
    exp_values.append(E**output)

print(exp_values)
