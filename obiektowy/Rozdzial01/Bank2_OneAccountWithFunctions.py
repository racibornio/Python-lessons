# Wersja proceduralna.
# Bank — wersja 2.
# Tylko jedno konto.

accountName = ''
accountBalance = 0
accountPassword = ''

def newAccount(name, balance, password):
    global accountName, accountBalance, accountPassword
    accountName = name
    accountBalance = balance
    accountPassword = password


def show():
    global accountName, accountBalance, accountPassword
    print('       Imię', accountName)
    print('       Saldo:', accountBalance)
    print('       Hasło:', accountPassword)
    print()

def getBalance(password):
    global accountName, accountBalance, accountPassword
    if password != accountPassword:
        print('Hasło jest nieprawidłowe.')
        return None

    return accountBalance

def deposit(amountToDeposit, password):
    global accountName, accountBalance, accountPassword
    if amountToDeposit < 0:
        print('Kwota wpłaty musi być wartością dodatnią!')
        return None

    if password != accountPassword:
        print('Hasło jest nieprawidłowe.')
        return None

    accountBalance = accountBalance + amountToDeposit
    return accountBalance

def withdraw(amountToWithdraw, password):
    global accountName, accountBalance, accountPassword
    if amountToWithdraw < 0:
        print('Kwota wypłaty musi być wartością dodatnią.')
        return None

    if password != accountPassword:
        print('Hasło do tego konta jest nieprawidłowe.')
        return None

    if amountToWithdraw > accountBalance:
        print('Kwota wypłaty nie może być większa od wysokości salda.')
        return None

    accountBalance = accountBalance - amountToWithdraw
    return accountBalance


newAccount("Jan", 100, 'soup')  # Utworzenie konta.

while True:
    print()
    print('Wybierz opcję b, aby wyświetlić saldo')
    print('Wybierz opcję d, aby dokonać wpłaty')
    print('Wybierz opcję w, aby dokonać wypłaty')
    print('Wybierz opcję s, aby wyświetlić informacje o koncie')
    print('Wybierz opcję q, aby zakończyć działanie programu')
    print()

    action = input('Co chcesz teraz zrobić? ')
    action = action.lower()  # Wymuszenie użycia małych liter.
    action = action[0]  # Użycie po prostu pierwszej litery.
    print()

    if action == 'b':
        print('Wyświetl saldo:')
        userPassword = input('Proszę podać hasło: ')
        theBalance = getBalance(userPassword)
        if theBalance is not None:
            print('Wysokość salda wynosi:', theBalance)

    elif action == 'd':
        print('Wpłata środków:')
        userDepositAmount = input('Proszę podać kwotę wpłaty: ')
        userDepositAmount = int(userDepositAmount)
        userPassword = input('Proszę podać hasło: ')

        newBalance = deposit(userDepositAmount, userPassword)
        if newBalance is not None:
            print('Wysokość salda po operacji wynosi:', newBalance)

    elif action == 's':   # Wyświetlenie informacji o koncie.
        print('Informacje:')
        show()

    elif action == 'q':
        break

    elif action == 'w':
        print('Wypłata środków:')

        userWithdrawAmount = input('Proszę podać kwotę wypłaty: ')
        userWithdrawAmount = int(userWithdrawAmount)
        userPassword = input('Proszę podać hasło: ')

        newBalance = withdraw(userWithdrawAmount, userPassword)
        if newBalance is not None:
            print('Wysokość salda po operacji wynosi:', newBalance)

print('Gotowe')
