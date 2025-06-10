# Program pozwalający na przetestowanie kont bankowych.
# Wersja 3., użycie słownika kont bankowych.

# Pobranie całego kodu z pliku klasy Account.
from Account import *

accountsDict = {}
nextAccountNumber = 0

# Tworzenie dwóch kont bankowych.:
oAccount = Account('Janek', 100, 'JoesPassword')
joesAccountNumber = nextAccountNumber
accountsDict[joesAccountNumber] = oAccount
print('Numer konta klienta Janek to:', joesAccountNumber)
nextAccountNumber = nextAccountNumber + 1

oAccount = Account('Marysia', 12345, 'MarysPassword')
marysAccountNumber = nextAccountNumber
accountsDict[marysAccountNumber] = oAccount
print('Numer konta klienta Marysia to:', marysAccountNumber)
nextAccountNumber = nextAccountNumber + 1

accountsDict[joesAccountNumber].show()
accountsDict[marysAccountNumber].show()
print()

# Wywołanie wybranych metod w różnych obiektach kont bankowych.
print('Wywoływanie metod obu obiektów kont bankowych...')
accountsDict[joesAccountNumber].deposit(50, 'JoesPassword')
accountsDict[marysAccountNumber].withdraw(345, 'MarysPassword')
accountsDict[marysAccountNumber].deposit(100, 'MarysPassword')

# Wyświetlenie informacji o kontach bankowych.
accountsDict[joesAccountNumber].show()
accountsDict[marysAccountNumber].show()

# Utworzenie kolejnego konta bankowego na podstawie informacji pochodzących od użytkownika.
print()
userName = input('Jakie jest imię klienta nowego konta bankowego? ')
userBalance = input('Jakie jest saldo początkowe dla tego konta bankowego? ')
userBalance = int(userBalance)
userPassword = input('Jakie jest hasło dla tego konta bankowego? ')
oAccount = Account(userName, userBalance, userPassword)
newAccountNumber = nextAccountNumber
accountsDict[newAccountNumber] = oAccount
print('Numer nowego konta to:', newAccountNumber)
nextAccountNumber = nextAccountNumber + 1

# Wyświetlenie informacji o nowo utworzonym koncie bankowym.
accountsDict[newAccountNumber].show()

# Wpłata 100 zł na nowo utworzone konto bankowe.
accountsDict[newAccountNumber].deposit(100, userPassword)
usersBalance = accountsDict[newAccountNumber].getBalance(userPassword)
print()
print('Po wpłacie 100 zł na konto wysokość jego salda wynosi:', usersBalance)

# Wyświetlenie informacji o nowym koncie bankowym.
accountsDict[newAccountNumber].show()
