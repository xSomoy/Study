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

norm_base = sum(exp_values)
norm_values = []

for value in exp_values:
    norm_values.append(value / norm_base)

print(norm_values)
print(sum(norm_values))
