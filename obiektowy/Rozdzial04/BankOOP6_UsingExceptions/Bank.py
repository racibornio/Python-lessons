# Klasa Bank zarządzająca słownikiem obiektów Account.

from Account import *

class Bank():
    def __init__(self, hours, address, phone):
        self.accountsDict = {}
        self.nextAccountNumber = 0
        self.hours = hours
        self.address = address
        self.phone = phone

    def askForValidAccountNumber(self):
        accountNumber = input('Proszę podać numer konta bankowego? ')
        try:
            accountNumber = int(accountNumber)
        except ValueError:
            raise AbortTransaction('Numer konta powinien być liczbą całkowitą.')
        if accountNumber not in self.accountsDict:
            raise AbortTransaction('Nie istnieje konto o numerze ' + str(accountNumber))
        return accountNumber

    def getUsersAccount(self):
        accountNumber = self.askForValidAccountNumber()
        oAccount = self.accountsDict[accountNumber]
        self.askForValidPassword(oAccount)
        return oAccount

    def askForValidPassword(self, oAccount):
        password = input('Proszę podać hasło: ')
        oAccount.checkPasswordMatch(password)

    def createAccount(self, theName, theStartingAmount, thePassword):
        oAccount = Account(theName, theStartingAmount, thePassword)
        newAccountNumber = self.nextAccountNumber
        self.accountsDict[newAccountNumber] = oAccount
        # Inkrementacja wartości w celu przygotowania się do utworzenia następnego konta bankowego.
        self.nextAccountNumber = self.nextAccountNumber + 1
        return newAccountNumber

    def openAccount(self):
        print('*** Otworzenie konta bankowego ***')
        userName = input('Jak masz na imię? ')
        userStartingAmount = input('Jakie jest saldo początkowe? ')
        userPassword = input('Podaj hasło do tego konta? ')
        userAccountNumber = self.createAccount(userName, userStartingAmount, userPassword)
        print('Numer nowego konta:', userAccountNumber)

    def closeAccount(self):
        print('*** Zamknięcie konta ***')
        userAccountNumber = self.askForValidAccountNumber()
        oAccount = self.accountsDict[userAccountNumber]
        self.askForValidPassword(oAccount)
        theBalance = oAccount.getBalance()
        print('Na koncie znajdują się środki w wysokości', theBalance, ', które zostaną zwrócone.')
        del self.accountsDict[userAccountNumber]
        print('Twoje konto zostało zamknięte.')

    def balance(self):
        print('*** Wyświetl saldo ***')
        oAccount = self.getUsersAccount()
        theBalance = oAccount.getBalance()
        print('Wysokość salda wynosi:', theBalance)

    def deposit(self):
        print('*** Wpłata środków ***')
        oAccount = self.getUsersAccount()
        depositAmount = input('Proszę podać kwotę wpłaty: ')
        theBalance = oAccount.deposit(depositAmount)
        print('Wpłacona kwota:', depositAmount)
        print('Wysokość salda po operacji wynosi:', theBalance)

    def withdraw(self):
        print('*** Wypłata środków ***')
        oAccount = self.getUsersAccount()
        userAmount = input('Proszę podać kwotę wpłaty: ')
        theBalance = oAccount.withdraw(userAmount)
        print('Wypłata:', userAmount)
        print('Wysokość salda po operacji wynosi:', theBalance)

    def getInfo(self):
        print('Godziny pracy:', self.hours)
        print('Adres:', self.address)
        print('Telefon:', self.phone)
        print('Aktualnie obsługujemy ', len(self.accountsDict), 'kont.')

    # Metoda specjalna dla celów administracyjnych klasą Bank.
    def show(self):
        print('*** Informacje ***')
        print('(To zwykle będzie wymagało podania hasła administratora.)')
        for userAccountNumber in self.accountsDict:
            oAccount = self.accountsDict[userAccountNumber]
            print('Konto:', userAccountNumber)
            oAccount.show()
            print()

