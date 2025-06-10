# Wersja proceduralna.
# Bank — wersja 5.
# Dowolna liczba kont — implementacja wykorzysująca listę słowników.

accountsList = []

def newAccount(aName, aBalance, aPassword):
    global accountsList
    newAccountDict = {'name':aName, 'balance':aBalance, 'password':aPassword}
    accountsList.append(newAccountDict)

def show(accountNumber):
    global accountsList
    print('Konto', accountNumber)
    thisAccountDict = accountsList[accountNumber]
    print('       Imię', thisAccountDict['name'])
    print('       Saldo:', thisAccountDict['balance'])
    print('       Hasło:', thisAccountDict['password'])
    print()

def getBalance(accountNumber, password):
    global accountsList
    thisAccountDict = accountsList[accountNumber]
    if password != thisAccountDict['password']:
        print('Hasło jest nieprawidłowe.')
        return None
    return thisAccountDict['balance']

def deposit(accountNumber, amountToDeposit, password):
    global accountsList
    thisAccountDict = accountsList[accountNumber]
    if amountToDeposit < 0:
        print('Kwota wpłaty musi być wartością dodatnią!')
        return None

    if password != thisAccountDict['password']:
        print('Hasło jest nieprawidłowe.')
        return None

    thisAccountDict['balance'] = thisAccountDict['balance'] + amountToDeposit
    return thisAccountDict['balance']

def withdraw(accountNumber, amountToWithdraw, password):
    global accountsList
    thisAccountDict = accountsList[accountNumber]
    if amountToWithdraw < 0:
        print('Kwota wypłaty musi być wartością dodatnią.')
        return None

    if password != thisAccountDict['password']:
        print('Hasło do tego konta jest nieprawidłowe.')
        return None

    if amountToWithdraw > thisAccountDict['balance']:
        print('Kwota wypłaty nie może być większa od wysokości salda.')
        return None

    thisAccountDict['balance'] = thisAccountDict['balance'] - amountToWithdraw
    return thisAccountDict['balance']

# Utworzenie dwóch przykładowych kont.
print("Numer konta bankowego Janka:", len(accountsList))
newAccount("Jan", 100, 'soup')

print("Numer konta bankowego Marysi:", len(accountsList))
newAccount("Marysia", 12345, 'nuts')

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

        userAccountNumber = len(accountsList)
        newAccount(userName, userStartingAmount, userPassword)
        print('Numer nowego konta:', userAccountNumber)

    elif action == 's':   # Wyświetlenie informacji.
        print('Informacje:')
        nAccounts = len(accountsList)
        for accountNumber in range(0, nAccounts):
            show(accountNumber)

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
