# Kod główny pokazujący przykład użycia właściwości klasy Student.

from Student import *

oStudent1 = Student('Jan Kowalski')
oStudent2 = Student('Joanna Nowak')

# Pobranie wartości grade obiektów za pomocą właściwości 'grade' i wyświetlenie ich wartości.
print(oStudent1.grade)
print(oStudent2.grade)
print()

# Przypisanie nowych wartości za pomocą właściwości 'grade'.
oStudent1.grade = 85
oStudent2.grade = 92

oStudent1.grade = 'abc'


print(oStudent1.grade)
print(oStudent2.grade)
