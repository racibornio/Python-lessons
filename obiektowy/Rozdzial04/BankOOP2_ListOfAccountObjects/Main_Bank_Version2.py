# Program pozwalający na przetestowanie kont bankowych.
# Wersja 2., wykorzystuje listę kont bankowych.

# Pobranie całego kodu z pliku klasy Account.
from Account import *

# Lista kont bankowych jest na początku pusta.
accountsList = [ ]

# Tworzenie dwóch kont bankowych.
oAccount = Account('Janek', 100, 'JoesPassword')
accountsList.append(oAccount)
print("Numer konta Janka to 0")

oAccount = Account('Marysia', 12345, 'MarysPassword')
accountsList.append(oAccount)
print("Numer konta Marysi to 1")

accountsList[0].show()
accountsList[1].show()
print()

# Wywołanie wybranych metod w różnych obiektach kont bankowych.
print('Wywoływanie metod obu obiektów kont bankowych...')
accountsList[0].deposit(50, 'JoesPassword')
accountsList[1].withdraw(345, 'MarysPassword')
accountsList[1].deposit(100, 'MarysPassword')

# Wyświetlenie informacji o kontach bankowych.
accountsList[0].show()
accountsList[1].show()

# Utworzenie kolejnego konta bankowego na podstawie informacji pochodzących od użytkownika.
print()
userName = input('Jakie jest imię klienta nowego konta bankowego? ')
userBalance = input('Jakie jest saldo początkowe dla tego konta bankowego? ')
userBalance = int(userBalance)
userPassword = input('Jakie jest hasło dla tego konta bankowego? ')
oAccount = Account(userName, userBalance, userPassword)
accountsList.append(oAccount)  # Dołączenie obiektu do listy kont.

# Wyświetlenie informacji o nowo utworzonym koncie bankowym.
print('Utworzono nowe konto, jego numer to 2.')
accountsList[2].show()

# Wpłata 100 zł na nowo utworzone konto bankowe.
accountsList[2].deposit(100, userPassword)
usersBalance = accountsList[2].getBalance(userPassword)
print()
print('Po wpłacie 100 zł na konto wysokość jego salda wynosi:', usersBalance)

# Wyświetlenie informacji o nowym koncie bankowym.
accountsList[2].show()
