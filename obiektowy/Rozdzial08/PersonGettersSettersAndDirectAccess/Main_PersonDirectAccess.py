# Przykład programu głównego, w którym dostęp do klasy Person odbywa się bezpośrednio.

from Person import *

oPerson1 = Person('Jan Kowalski', 90000)
oPerson2 = Person('Joanna Nowak', 99000)

# Bezpośrednie pobranie wartości zmiennej egzemplarza salary.
print(oPerson1.salary)
print(oPerson2.salary)

# Bezpośrednia zmiana wartości zmiennej egzemplarza salary.
oPerson1.salary = 100000
oPerson2.salary = 111111

# Pobranie uaktualnionej wartości zmiennej egzemplarza salary i jej ponowne wyświetlenie.
print(oPerson1.salary)
print(oPerson2.salary)

