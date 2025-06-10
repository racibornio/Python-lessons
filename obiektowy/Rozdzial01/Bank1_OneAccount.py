# Wersja proceduralna.
# Bank — wersja 1.
# Tylko jedno konto.

accountName = 'Jan'
accountBalance = 100
accountPassword = 'soup'

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
        if userPassword != accountPassword:
            print('Hasło jest nieprawidłowe.')
        else:
            print('Wysokość salda wynosi:', accountBalance)

    elif action == 'd':
        print('Wpłata środków:')
        userDepositAmount = input('Proszę podać kwotę wpłaty: ')
        userDepositAmount = int(userDepositAmount)
        userPassword = input('Proszę podać hasło: ')

        if userDepositAmount < 0:
            print('Kwota wpłaty musi być wartością dodatnią!')

        elif userPassword != accountPassword:
            print('Hasło jest nieprawidłowe.')

        else:  # OK.
            accountBalance = accountBalance + userDepositAmount
            print('Wysokość salda po operacji wynosi:', accountBalance)

    elif action == 's':  # Wyświetlenie informacji o koncie.
        print('Informacje:')
        print('       Imię', accountName)
        print('       Saldo:', accountBalance)
        print('       Hasło:', accountPassword)
        print()

    elif action == 'q':
        break

    elif action == 'w':
        print('Wypłata środków:')

        userWithdrawAmount = input('Proszę podać kwotę wypłaty: ')
        userWithdrawAmount = int(userWithdrawAmount)
        userPassword = input('Proszę podać hasło: ')

        if userWithdrawAmount < 0:
            print('Kwota wypłaty musi być wartością dodatnią.')

        elif userPassword != accountPassword:
            print('Hasło do tego konta jest nieprawidłowe.')

        elif userWithdrawAmount > accountBalance:
            print('Kwota wypłaty nie może być większa od wysokości salda.')

        else:  #OK
            accountBalance = accountBalance - userWithdrawAmount
            print('Wysokość salda po operacji wynosi:', accountBalance)

print('Gotowe')
