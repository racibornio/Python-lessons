import numpy as np

#zad.: utwórz wektor

#utw. wektor przedstawiający wiersz
vector_row = np.array([1, 2, 3])

#utw. wektora przedstawiającego kolumnę
vector_column = np.array([[1],
                          [2],
                          [3]])

print('Row shape', vector_row.shape)
print('Column shape', vector_column.shape)

vector_mixed = np.array([
    [0, 1, 1],
    [1, 2, 3],
    [2, 3, 4]
])
print('Mixed vector', vector_mixed.shape)