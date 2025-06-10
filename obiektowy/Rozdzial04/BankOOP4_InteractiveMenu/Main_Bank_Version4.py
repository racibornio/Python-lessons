# Program interaktywny tworzący słownik kont bankowych.
# Wersja 4., zawiera interaktywne menu.

from Account import *

accountsDict = {}
nextAccountNumber = 0

# Utworzenie kont początkowych na potrzeby testowania.
oAccount = Account('Janek', 100, 'JoesPassword')
accountsDict[nextAccountNumber] = oAccount
print('Numer konta klienta Janek to:', nextAccountNumber)
# Inkrementacja numeru konta po przypisaniu.
nextAccountNumber = nextAccountNumber + 1

oAccount = Account('Marysia', 12345, 'MarysPassword')
accountsDict[nextAccountNumber] = oAccount
print('Numer konta klienta Marysia to:', nextAccountNumber)
nextAccountNumber = nextAccountNumber + 1

while True:
    print()
    print('Wybierz opcję b, aby wyświetlić saldo')
    print('Wybierz opcję d, aby dokonać wpłaty')
    print('Naciśnij klawisz o, aby otworzyć nowe konto')
    print('Wybierz opcję w, aby dokonać wypłaty')
    print('Wybierz opcję n, aby wyświetlić informacje o kontach')
    print('Wybierz opcję q, aby zakończyć działanie programu')
    print()

    action = input('Co chcesz teraz zrobić? ')
    action = action.lower()
    action = action[0]  # Pobranie pierwszej litery.
    print()

    if action == 'b':
        print('*** Wyświetl saldo ***')
        userAccountNumber = input('Proszę podać numer konta: ')
        userAccountNumber = int(userAccountNumber)
        userAccountPassword = input('Proszę podać hasło: ')
        oAccount = accountsDict[userAccountNumber]
        theBalance = oAccount.getBalance(userAccountPassword)
        if theBalance is not None:
            print('Wysokość salda wynosi:', theBalance)

    elif action == 'd':
        print('*** Wpłata środków ***')
        userAccountNumber = input('Proszę podać numer konta: ')
        userAccountNumber = int(userAccountNumber)
        userDepositAmount = input('Proszę podać kwotę wpłaty: ')
        userDepositAmount = int(userDepositAmount)
        userPassword = input('Proszę podać hasło: ')
        oAccount = accountsDict[userAccountNumber]
        theBalance = oAccount.deposit(userDepositAmount, userPassword)
        if theBalance is not None:
            print('Wysokość salda po operacji wynosi:', theBalance)

    elif action == 'o':
        print('*** Otworzenie konta bankowego ***')
        userName = input('Jakie jest imię klienta nowego konta bankowego? ')
        userStartingAmount = input('Jakie jest saldo początkowe dla tego konta bankowego? ')
        userStartingAmount = int(userStartingAmount)
        userPassword = input('Jakie jest hasło dla tego konta bankowego? ')
        oAccount = Account(userName, userStartingAmount, userPassword)
        accountsDict[nextAccountNumber] = oAccount
        print('Numer nowego konta:', nextAccountNumber)
        nextAccountNumber = nextAccountNumber + 1
        print()

    elif action == 's':
        print('Informacje:')
        for userAccountNumber in accountsDict:
            oAccount = accountsDict[userAccountNumber]
            print('   Numer konta bankowego:', userAccountNumber)
            oAccount.show()#userAccountNumber)

    elif action == 'q':
        break

    elif action == 'w':
        print('*** Wypłata środków ***')
        userAccountNumber = input('Proszę podać numer konta: ')
        userAccountNumber = int(userAccountNumber)
        userWithdrawalAmount = input('Proszę podać kwotę wpłaty: ')
        userWithdrawalAmount = int(userWithdrawalAmount)
        userPassword = input('Proszę podać hasło: ')
        oAccount = accountsDict[userAccountNumber]
        theBalance = oAccount.withdraw(userWithdrawalAmount, userPassword)
        if theBalance is not None:
            print('Wypłata:', userWithdrawalAmount)
            print('Wysokość salda po operacji wynosi:', theBalance)

    else:
        print('Przepraszamy, ale to nie jest prawidłowa opcja. Spróbuj ponownie.')

print('Gotowe')
