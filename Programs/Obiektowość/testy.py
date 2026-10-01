class Klasa_1:
    atrybut_klasy = None

    def __init__(self, a_parametru):
        self.atrybut_instancji_wspolny = None
        self.a_atrybutu_klasy = a_parametru
        print("Konstruktor obiektu klasy Klasa_1 z __init__() zadziałał.")

    def mnozenie(self):
        return self.a_atrybutu_klasy * 2


class Klasa_2:
    def __init__(self, a_parametru):
        self.a_atrybutu_klasy = a_parametru
        print("Konstruktor obiektu klasy Klasa_2 z __init__() zadziałał.")

print(f'Tworzymy 1. obiekt klasy Klasa_1 ...')
first_obj_class_1 = Klasa_1(13)
print(f'Atrybut instancji wspólny to: {first_obj_class_1.atrybut_instancji_wspolny}')
print(f'Klasa widzie "swoje" a_atrybutu_klasy z parametru: {first_obj_class_1.a_atrybutu_klasy}')
print(f'Obiekt ma dostęp do atrybutu klasy poprzez wywołanie na rzecz obiektu "Klasa_1.atrybut_klasy": {Klasa_1.atrybut_klasy}\n')

print(f'Obiekt "first_obj_class_1" inicjuje atrybut klasy wartością 100 wywołując go na rzecz obiektu "Klasa_1.atrybut_klasy = 100".')
Klasa_1.atrybut_klasy = 100
print(f'Pole zostało zaktualizowane: {Klasa_1.atrybut_klasy}')
print(f'Można też na rzecz tego obiektu stworzyć atrybut instancji jako kopię atrybutu klasy wywołując "first_obj_class_1.atrybut_klasy = 111".')
first_obj_class_1.atrybut_klasy = 111
print(f'I oto mamy: {first_obj_class_1.atrybut_klasy}\n')


print(f'Tworzymy 2. obiekt klasy Klasa_1 ...')
second_obj_class_1 = Klasa_1(9)
print(f'Atrybut instancji wspólny to: {second_obj_class_1.atrybut_instancji_wspolny}')
print(f'a_atrybutu_klasy z parametru to: {second_obj_class_1.a_atrybutu_klasy}')
print(f'Obiekt am dostęp do atrybutu klasy: {second_obj_class_1.atrybut_klasy}\n')

print(f'Teraz "second_obj_class_1" aktualizje atrybut klasy wartością 200.')
Klasa_1.atrybut_klasy = 200
print(f'Pole zostało zaktualizowane: {Klasa_1.atrybut_klasy}\n')

print(f'Tu także można na rzecz tego obiektu stworzyć atrybut instancji jako kopię atrybutu klasy wywołując "second_obj_class_1.atrybut_klasy = 222".')
second_obj_class_1.atrybut_klasy = 222
print(f'I oto mamy: {second_obj_class_1.atrybut_klasy}\n')

print(f'Tworzymy 1. obiekt klasy Klasa_2 ...')
first_obj_class_2 = Klasa_2(90)
print(f'Klasa widzie "swoje" a_atrybutu_klasy z parametru to {first_obj_class_2.a_atrybutu_klasy}\n')

print(f'A teraz słownik klasy: {Klasa_1.__dict__}\n')
print(f'Słownik 1-go obiektu: {first_obj_class_1.__dict__}\n')
print(f'Słownik 2-go obiektu: {first_obj_class_2.__dict__}\n')
print(f'I słownik 3-go obiektu: {second_obj_class_1.__dict__}\n')



class objects_creator:

    object_counter = 0
    object_list = []
    
    def __init__(self):
        print(f'New object created.')
        objects_creator.object_counter += 1
        objects_creator.object_list.append(self)
        print(f'Objects list: {objects_creator.object_list}')
        pass

    # class variant
    @classmethod
    def count_objects(cls):
        print(f'There are {cls.object_counter} objects.')

    # static variant
    @staticmethod
    def count_objects_static():
        print(f'STATIC: There are {objects_creator.object_counter} objects.\n')

    @classmethod
    def remove_object(cls, obj):
        print(f'The object {obj} is to be removed.')
        cls.object_list.remove(obj)
        del obj
        objects_creator.object_counter -= 1
        print(f'The object has been removed.')

obj_1 = objects_creator()
objects_creator.count_objects()
objects_creator.count_objects_static()
obj_2 = objects_creator()
objects_creator.count_objects()
objects_creator.count_objects_static()
obj_3 = objects_creator()
objects_creator.count_objects()
objects_creator.count_objects_static()

objects_creator.remove_object(obj_1)
objects_creator.count_objects()