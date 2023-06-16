inputs = [1, 2, 3, 2.5]
weights1 = [0.2, 0.8, -0.5, 1.0]
weights1 = [0.5, -0.91, 0.26, -0.5]
weights1 = [-0.26, -0.27, 0.17, 0.87]
bias1 = 2
bias2 = 3
bias3 = 0.5

output = inputs[0]*weights1[0] + inputs[1] * weights1[1] + inputs[2]*weights1[2]  + inputs[3]*weights1[3] + bias1

print(output)
