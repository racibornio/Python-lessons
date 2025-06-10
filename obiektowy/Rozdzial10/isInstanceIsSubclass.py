#  Testowanie wywołań isinstance() i issubclass().
class Base():

    def __init__(self):
        print('W metodzie init() klasy Base.')

class Sub(Base):

    def __init__(self):
        print('W metodzie init() podklasy.')

oSub = Sub() # Utworzenie egzemplarza klasy Sub.
oBase = Base()  # Utworzenie egzemplarza klasy Base.

print(isinstance(oSub, Sub))  # Zwraca wartość True.
print(isinstance(oSub, Base))  # Zwraca wartość True.

print(isinstance(oBase, Base))  # Zwraca wartość True.
print(isinstance(oBase, Sub))  # Zwraca wartość False.

print(issubclass(Sub, Base))  # Zwraca wartość True.
print(issubclass(Base, Sub))  # Zwraca wartość False.
