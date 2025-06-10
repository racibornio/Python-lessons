# Program główny do kontrolowania obiektu Bank składającego się z obiektów Account.
from Bank import *

# Tworzenie egzemplarza klasy Bank.
oBank = Bank('od 9 do 5', '123 Main Street, Anytown, USA', '(650) 555-1212')

#Kod główny.
while True:
    print()
    print('Aby sprawdzić saldo, naciśnij klawisz b')
    print('Aby zamknąć konto, naciśnij klawisz c')
    print('Aby wpłacić środki, naciśnij klawisz d')
    print('Aby wypłacić wyświetlić informacje o banku, naciśnij klawisz i')
    print('Aby otworzyć nowe konto, naciśnij klawisz o')
    print('Aby zakończyć działanie programu, naciśnij klawisz q')
    print('Aby wyświetlić wszystkie konta, naciśnij klawisz s')
    print('Aby wypłacić środki, naciśnij klawisz w  ')
    print()

    action = input('Co chcesz teraz zrobić? ')
    action = action.lower()
    action = action[0]  # Pobranie pierwszej litery.
    print()

    try:
        if action == 'b':
            oBank.balance()
        elif action == 'c':
            oBank.closeAccount()
        elif action == 'd':
            oBank.deposit()
        elif action == 'i':
            oBank.getInfo()
        elif action == 'o':
            oBank.openAccount()
        elif action == 'q':
            break
        elif action == 's':
            oBank.show()
        elif action == 'w':
            oBank.withdraw()
    except AbortTransaction as error:
        # Wyświetlenie komunikatu błędu.
        print(error)

print('Gotowe')
