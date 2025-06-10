# Kod testujący klasę Vector.

from Vector import *

v1 = Vector(3, 4)
v2 = Vector(2, 2)
v3 = Vector(3, 4)

# Te polecenia wyświetlają wartości boolowskie lub liczbowe.
print(v1 == v2) # False
print(v1 == v3) # True
print(abs(v1))  # 5
print(abs(v2))  # 2.8284...
print(v1 < v2)  # False
print(v1 > v2)  # True
print() # Pusty wiersz.

# Te polecenia wyświetlają obiekty Vector (wywołania metody __str__()).
print('Vector 1:', v1) # 3, 4
print('Vector 2:', v2) # 2, 2
print('Vector 1 + Vector 2:', v1 + v2)  # 5, 6
print('Vector 1 - Vector 2:', v1 - v2)  # 1, 2
print('Vector 1 pomnożony przez Vector 2:', v1 * v2)  # 6, 8
print('Vector 2 pomnożony przez 5:', v1 * 5)  # 15, 20
