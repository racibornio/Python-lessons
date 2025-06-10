# Program główny do kontrolowania obiektu Bank składającego się z obiektów Account.

# Pobranie całego kodu klasy Bank.
from Bank import *

# Tworzenie egzemplarza klasy Bank.
oBank = Bank()

# Kod główny.
# Utworzenie dwóch przykładowych kont bankowych.
joesAccountNumber = oBank.createAccount('Janek', 100, 'JoesPassword')
print("Numer konta Janka to:", joesAccountNumber)

marysAccountNumber = oBank.createAccount('Marysia', 12345, 'MarysPassword')
print("Numer konta Marysi to:", marysAccountNumber)

while True:
    print()
    print('Aby sprawdzić saldo, naciśnij klawisz b')
    print('Aby zamknąć konto, naciśnij klawisz c')
    print('Aby wpłacić środki, naciśnij klawisz d')
    print('Aby wypłacić wyświetlić informacje o banku, naciśnij klawisz i')
    print('Aby otworzyć nowe konto, naciśnij klawisz o')
    print('Aby zakończyć działanie programu, naciśnij klawisz q')
    print('Aby wyświetlić wszystkie konta, naciśnij klawisz s')
    print('Aby wypłacić środki, naciśnij klawisz w')
    print()

    action = input('Co chcesz teraz zrobić? ')
    action = action.lower()
    action = action[0]  # Pobranie pierwszej litery.
    print()

    if action == 'b':
        oBank.balance()

    elif action == 'c':
        oBank.closeAccount()

    elif action == 'd':
        oBank.deposit()

    elif action == 'i':
        oBank.bankInfo()

    elif action == 'o':
        oBank.openAccount()

    elif action == 's':
        oBank.show()

    elif action == 'q':
        break

    elif action == 'w':
        oBank.withdraw()

    else:
        print('Przepraszamy, ale to nie jest prawidłowa opcja. Spróbuj ponownie.')

print('Gotowe')

