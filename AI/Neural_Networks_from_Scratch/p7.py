
import numpy as np
import math

softmax_output = [0.7, 0.1, 0.2]
target_output = [1, 0, 0]
loss = -(math.log(softmax_output[0])*target_output[0] +
         math.log(softmax_output[1])*target_output[1] +
         math.log(softmax_output[2])*target_output[2])

print(loss)

loss = -math.log(softmax_output[0])

print(loss)

print(-math.log(0.7))
print(-math.log(0.5))

# Logarithm Math
# b = 5.2
# print(np.log(b))
# print(math.e ** 1.6486586255873816)
