# Utworzenie przykładowego programu głównego, który używa klasy Club.

from Club import *

# Utworzenie klubu, do którego może należeć maksimum pięciu członków.
oProgrammingClub = Club('Programowanie', 5)

oProgrammingClub.addMember('Jan Kowalski')
oProgrammingClub.addMember('Celina Lutowska')
oProgrammingClub.addMember('Daniel Różański')
oProgrammingClub.addMember('Sara Stankiewicz')
oProgrammingClub.addMember('Franek Frankowski')

oProgrammingClub.report()

# Próba dołączenia kolejnego członka do klubu.

oProgrammingClub.addMember('Iwona Jóźwiak')
