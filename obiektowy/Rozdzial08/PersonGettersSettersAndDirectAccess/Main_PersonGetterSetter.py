# Przykładowy kod główny używający metod typu getter i setter.

from Person import *

oPerson1 = Person('Jan Kowalski', 90000)
oPerson2 = Person('Joanna Nowak', 99000)

# Pobranie za pomocą metody typu getter wartości zmiennych egzemplarza salary i ich wyświetlenie.
print(oPerson1.getSalary())
print(oPerson2.getSalary())

# Zmiana za pomocą metody typu setter wartości zmiennych egzemplarza salary.
oPerson1.setSalary(100000)
oPerson2.setSalary(111111)

# Ponowne pobranie wartości zmiennych egzemplarza salary i ich wyświetlenie.
print(oPerson1.getSalary())
print(oPerson2.getSalary())
