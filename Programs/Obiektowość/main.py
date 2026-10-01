class Main():
    def __init__(self):
        print("Object created!")
        self.y = 1
        print(f'y = {self.y}')
        pass


    x = 0.00


first_obj = Main()
print(f'x = {first_obj.x}')
first_obj.x = 15.0
print(f'x = {first_obj.x}')
print(f'y = {first_obj.y}')

print()

class DrugaKlasa:
    def __init__(self, a):
        self.a = a
        print("Klasa 2-ga działa.")

    def f1(self):
        print('Mamy atrybut klasy:', self.a)
        pass

obj_1 = DrugaKlasa(1)
print(obj_1.a)
obj_1.f1()