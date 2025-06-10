# Klasa Student.
class Student():
    def __init__(self, name):
        self.name = name
        print('Tworzenie obiektu klasy Student:', self.name)

    def __del__(self):
        print('W metodzie __del__() obiektu klasy Student:', self.name)

# Klasa Teacher.
class Teacher():
    def __init__(self):
       print('Tworzenie obiektu klasy Teacher')
       self.oStudent1 = Student('Jan')
       self.oStudent2 = Student('Sara')
       self.oStudent3 = Student('Cezary')

    def __del__(self):
        print('W metodzie __del__() obiektu klasy Teacher')

# Utworzenie egzemplarza klasy Teacher (który tworzy obiekty klasy Student).
oTeacher = Teacher()

# Usunięcie obiektu klasy Teacher.
del oTeacher
