import numpy as np

array_1 = np.array([0, 1, 2, 3, 4])

print("Displaying array 1:")
print(array_1)
print()

array_2 = np.array([0, -1, -2, -3, -4])
print("Displaying array 2:")
print(array_2)
print()

sum = array_1 + array_2
print("Displaying sum:")
print(sum)
print()

subtract = array_1 - array_2
print("Displaying subtract:")
print(subtract)
print()

multipliation = array_1 * array_2
print("Displaying multiplication:")
print(multipliation)
print()

dividing = array_1 / array_2
print("Displaying dividing:")
print(dividing)
print()

added_ten = array_1 + 10
print("Array after adding 10:")
print(added_ten)
print()

random_10_values = np.random.random(10)
print("Random 10 numbers:")
print(random_10_values)
print()

random_10_int = np.random.randint(0, 10, 10)
print("Random 10 integers:")
print(random_10_int)
print()

random_10_normal = np.random.normal(0, 1, 10)
print("Random 10 values from normal distribution:")
print(random_10_normal)
print()