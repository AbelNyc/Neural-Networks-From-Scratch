inputs = [1.2,5.1,2.1,3.5]
# evey input has a weights
weights1 = [3.1, 2.1, -8.7, 2.3]
weights2 = [3.2, -1.5, 8.5, -2.2]
weights3 = [2.9, -2.5, 8.1, 2.1]

# every neuroan has a bias
bias1, bias2, bias3 = 2,3,.5


# inputs layer: input * weight + bias 
output = [inputs[0] * weights1[0] + inputs[1] * weights1[1] + inputs[2] * weights1[2] + inputs[3] * weights1[3] + bias1,
          inputs[0] * weights2[0] + inputs[1] * weights2[1] + inputs[2] * weights2[2] + inputs[3] * weights2[3] + bias2,
          inputs[0] * weights1[0] + inputs[1] * weights2[1] + inputs[2] * weights3[2] + inputs[3] * weights3[3] + bias3,
]
print("Three neurons:",output)