# Program pozwalający na przetestowanie kont bankowych.
# Wersja 1., użycie wyraźnie zdefiniowanych zmiennych dla poszczególnych obiektów Account.

# Pobranie całego kodu z pliku klasy Account.
from Account import *

# Tworzenie dwóch kont bankowych.
oJoesAccount = Account('Jan', 100, 'JoesPassword')
print("Utworzono konto dla klienta Janek")

oMarysAccount = Account('Marysia', 12345, 'MarysPassword')
print("Utworzono konto dla klienta Marysia")

oJoesAccount.show()
oMarysAccount.show()
print()

# Wywołanie wybranych metod w różnych obiektach kont bankowych.
print('Wywoływanie metod obu obiektów kont bankowych...')
oJoesAccount.deposit(50, 'JoesPassword')
oMarysAccount.withdraw(345, 'MarysPassword')
oMarysAccount.deposit(100, 'MarysPassword')

# Wyświetlenie informacji o kontach bankowych.
oJoesAccount.show()
oMarysAccount.show()

# Utworzenie kolejnego konta bankowego na podstawie informacji pochodzących od użytkownika.
print()
userName = input('Jakie jest imię klienta nowego konta bankowego? ')
userBalance = input('Jakie jest saldo początkowe dla tego konta bankowego? ')
userBalance = int(userBalance)
userPassword = input('Jakie jest hasło dla tego konta bankowego? ')
oNewAccount = Account(userName, userBalance, userPassword)

# Wyświetlenie informacji o nowo utworzonym koncie bankowym.
oNewAccount.show()

# Wpłata 100 zł na nowo utworzone konto bankowe.
oNewAccount.deposit(100, userPassword)
usersBalance = oNewAccount.getBalance(userPassword)
print()
print('Po wpłacie 100 zł na konto wysokość jego salda wynosi:', usersBalance)

# Wyświetlenie informacji o nowym koncie bankowym.
oNewAccount.show()

