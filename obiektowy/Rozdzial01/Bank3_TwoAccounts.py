# Wersja proceduralna.
# Bank — wersja 3.
# Dwa konta.

account0Name = ''
account0Balance = 0
account0Password = ''
account1Name = ''
account1Balance = 0
account1Password = ''
nAccounts = 0

def newAccount(accountNumber, name, balance, password):
    global account0Name, account0Balance, account0Password
    global account1Name, account1Balance, account1Password

    if accountNumber == 0:
        account0Name = name
        account0Balance = balance
        account0Password = password
    if accountNumber == 1:
        account1Name = name
        account1Balance = balance
        account1Password = password

def show():
    global account0Name, account0Balance, account0Password
    global account1Name, account1Balance, account1Password

    if account0Name != '':
        print('Konto 0')
        print('       Imię', account0Name)
        print('       Saldo:', account0Balance)
        print('       Hasło:', account0Password)
        print()
    if account1Name != '':
        print('Konto 1')
        print('       Imię', account1Name)
        print('       Saldo:', account1Balance)
        print('       Hasło:', account1Password)
        print()

def getBalance(accountNumber, password):
    global account0Name, account0Balance, account0Password
    global account1Name, account1Balance, account1Password

    if accountNumber == 0:
        if password != account0Password:
            print('Hasło jest nieprawidłowe.')
            return None
        return account0Balance
    if accountNumber == 1:
        if password != account1Password:
            print('Hasło jest nieprawidłowe.')
            return None
        return account1Balance

def deposit(accountNumber, amountToDeposit, password):
    global account0Name, account0Balance, account0Password
    global account1Name, account1Balance, account1Password

    if accountNumber == 0:
        if amountToDeposit < 0:
            print('Kwota wpłaty musi być wartością dodatnią!')
            return None

        if password != account0Password:
            print('Hasło jest nieprawidłowe.')
            return None

        account0Balance = account0Balance + amountToDeposit
        return account0Balance

    if accountNumber == 1:
        if amountToDeposit < 0:
            print('Kwota wpłaty musi być wartością dodatnią!')
            return None

        if password != account1Password:
            print('Hasło jest nieprawidłowe.')
            return None

        account1Balance = account1Balance + amountToDeposit
        return account1Balance

def withdraw(accountNumber, amountToWithdraw, password):
    global account0Name, account0Balance, account0Password
    global account1Name, account1Balance, account1Password

    if accountNumber == 0:
        if amountToWithdraw < 0:
            print('Kwota wypłaty musi być wartością dodatnią.')
            return None

        if password != account0Password:
            print('Hasło do tego konta jest nieprawidłowe.')
            return None

        if amountToWithdraw > account0Balance:
            print('Kwota wypłaty nie może być większa od wysokości salda.')
            return None

        account0Balance = account0Balance - amountToWithdraw
        return account0Balance

    if accountNumber == 1:
        if amountToWithdraw < 0:
            print('Kwota wypłaty musi być wartością dodatnią.')
            return None

        if password != account1Password:
            print('Hasło do tego konta jest nieprawidłowe.')
            return None

        if amountToWithdraw > account1Balance:
            print('Kwota wypłaty nie może być większa od wysokości salda.')
            return None

        account1Balance = account1Balance - amountToWithdraw
        return account1Balance


# Utworzenie konta testowego.
newAccount(nAccounts, "Jan", 100, 'soup')
nAccounts = 1

while True:
    print()
    print('Wybierz opcję b, aby wyświetlić saldo')
    print('Wybierz opcję d, aby dokonać wpłaty')
    print('Wybierz opcję n, aby utworzyć nowe konto')
    print('Wybierz opcję w, aby dokonać wypłaty')
    print('Wybierz opcję n, aby wyświetlić informacje o kontach')
    print('Wybierz opcję q, aby zakończyć działanie programu')
    print()

    action = input('Co chcesz teraz zrobić? ')
    action = action.lower()  # Wymuszenie użycia małych liter.
    action = action[0]  # Użycie po prostu pierwszej litery.
    print()

    if action == 'b':
        print('Wyświetl saldo:')
        userAccountNumber = input('Proszę podać numer konta: ')
        userAccountNumber = int(userAccountNumber)
        userPassword = input('Proszę podać hasło: ')
        theBalance = getBalance(userAccountNumber, userPassword)
        if theBalance is not None:
            print('Wysokość salda wynosi:', theBalance)

    elif action == 'd':
        print('Wpłata środków:')
        userAccountNumber= input('Proszę podać numer konta: ')
        userAccountNumber = int(userAccountNumber)
        userDepositAmount = input('Proszę podać kwotę wpłaty: ')
        userDepositAmount = int(userDepositAmount)
        userPassword = input('Proszę podać hasło: ')
        newBalance = deposit(userAccountNumber, userDepositAmount, userPassword)
        if newBalance is not None:
            print('Wysokość salda po operacji wynosi:', newBalance)

    elif action == 'n':
        print('Nowe konto:')
        userName = input('Jak masz na imię? ')
        userStartingAmount = input('Jakie jest saldo początkowe? ')
        userStartingAmount = int(userStartingAmount)
        userPassword = input('Podaj hasło do tego konta? ')

        newAccount(nAccounts, userName, userStartingAmount, userPassword)
        print('Numer nowego konta:', nAccounts)
        nAccounts = nAccounts + 1

    elif action == 's':   # Wyświetlenie informacji.
        print('Informacje:')
        show()

    elif action == 'q':
        break

    elif action == 'w':
        print('Wypłata środków:')
        userAccountNumber = input('Proszę podać numer konta: ')
        userAccountNumber = int(userAccountNumber)
        userWithdrawAmount = input('Proszę podać kwotę wypłaty: ')
        userWithdrawAmount = int(userWithdrawAmount)
        userPassword = input('Proszę podać hasło: ')

        newBalance = withdraw(userAccountNumber, userWithdrawAmount, userPassword)
        if newBalance is not None:
            print('Wysokość salda po operacji wynosi:', newBalance)

print('Gotowe')
