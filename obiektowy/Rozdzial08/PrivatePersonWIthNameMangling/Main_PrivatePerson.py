# Przykład programu głównego używającego PrivatePerson.

from PrivatePerson import *

oPrivatePerson1 = PrivatePerson('Jan Kowalski', 'Dane dla użytkownika Jan Kowalski')
oPrivatePerson2 = PrivatePerson('Joanna Nowak', 'Dane dla użytkownika Joanna Nowak')

# Użycie metod typu getter i setter - to działa świetnie.
print(oPrivatePerson1.getName())

oPrivatePerson1.setName('Janina Kowalska')
print(oPrivatePerson1.getName())


# Próba bezpośredniego użycia zakończy się niepowodzeniem.
#print(oPrivatePerson1.__privateData)


# Używanie udekorowanych nazw - to działa.
print(oPrivatePerson1._PrivatePerson__privateData)
oPrivatePerson1._PrivatePerson__privateData = 'Zmodyfikowane dane dla użytkownika Janina Kowalska'
print(oPrivatePerson1._PrivatePerson__privateData)


