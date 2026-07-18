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

lista_pythonowa_1 = [1, 2, 3, 4, 5]
lista_pythonowa_2 = [5, 4, 3, 2, 1]

suma_list = lista_pythonowa_1 + lista_pythonowa_2
print("Displaying sum of two python lists:")
print(suma_list)
print()

lista_numpy_1 = np.array(lista_pythonowa_1)
lista_numpy_2 = np.array(lista_pythonowa_2)

suma_numpy = lista_numpy_1 + lista_numpy_2
print("Displaying sum of two numpy arrays:")
print(suma_numpy)
print()