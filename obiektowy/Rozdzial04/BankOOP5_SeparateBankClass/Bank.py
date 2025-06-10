# Klasa Bank zarządzająca słownikiem obiektów Account.

from Account import *

class Bank():

    def __init__(self):
        self.accountsDict = {}
        self.nextAccountNumber = 0

    def createAccount(self, theName, theStartingAmount, thePassword):
        oAccount = Account(theName, theStartingAmount, thePassword)
        newAccountNumber = self.nextAccountNumber
        self.accountsDict[newAccountNumber] = oAccount
        # Inkrementacja wartości w celu przygotowania się do utworzenia następnego konta bankowego.
        self.nextAccountNumber = self.nextAccountNumber + 1
        return newAccountNumber

    def openAccount(self):
        print('*** Otworzenie konta bankowego ***')
        userName = input('Jakie jest imię klienta nowego konta bankowego? ')
        userStartingAmount = input('Jakie jest saldo początkowe dla tego konta bankowego? ')
        userStartingAmount = int(userStartingAmount)
        userPassword = input('Jakie jest hasło dla tego konta bankowego? ')

        userAccountNumber = self.createAccount(userName, userStartingAmount, userPassword)
        print('Numer nowego konta:', userAccountNumber)
        print()

    def closeAccount(self):
        print('*** Zamknięcie konta ***')
        userAccountNumber = input('Proszę podać numer konta bankowego? ')
        userAccountNumber = int(userAccountNumber)
        userPassword = input('Jakie jest hasło dla tego konta bankowego? ')
        oAccount = self.accountsDict[userAccountNumber]
        theBalance = oAccount.getBalance(userPassword)

        if theBalance is not None:
            print('Na koncie znajdują się środki w wysokości', theBalance, ', które zostaną zwrócone.')
            # Usunięcie konta bankowego klienta ze słownika kont.
            del self.accountsDict[userAccountNumber]
            print('Twoje konto zostało zamknięte.')

    def balance(self):
        print('*** Wyświetl saldo ***')
        userAccountNumber = input('Proszę podać numer konta: ')
        userAccountNumber = int(userAccountNumber)
        userAccountPassword = input('Proszę podać hasło: ')
        oAccount = self.accountsDict[userAccountNumber]
        theBalance = oAccount.getBalance(userAccountPassword)
        if theBalance is not None:
            print('Wysokość salda wynosi:', theBalance)

    def deposit(self):
        print('*** Wpłata środków ***')
        accountNum = input('Proszę podać numer konta: ')
        accountNum = int(accountNum)
        depositAmount = input('Proszę podać kwotę wpłaty: ')
        depositAmount = int(depositAmount)
        userAccountPassword = input('Proszę podać hasło: ')
        oAccount = self.accountsDict[accountNum]
        theBalance = oAccount.deposit(depositAmount, userAccountPassword)
        if theBalance is not None:
            print('Wysokość salda po operacji wynosi:', theBalance)

    def show(self):
        print('*** Informacje ***')
        for userAccountNumber in self.accountsDict:
            oAccount = self.accountsDict[userAccountNumber]
            print('   Numer konta bankowego:', userAccountNumber)
            oAccount.show()

    def withdraw(self):
        print('*** Wypłata środków ***')
        userAccountNumber = input('Proszę podać numer konta: ')
        userAccountNumber = int(userAccountNumber)
        userAmount = input('Proszę podać kwotę wpłaty: ')
        userAmount = int(userAmount)
        userAccountPassword = input('Proszę podać hasło: ')
        oAccount = self.accountsDict[userAccountNumber]
        theBalance = oAccount.withdraw(userAmount, userAccountPassword)
        if theBalance is not None:
            print('Wypłata:', userAmount)
            print('Wysokość salda po operacji wynosi:', theBalance)

    def bankInfo(self):
        print('Godziny pracy: od 9 do 5')
        print('Adres: 123 Main Street, Anytown, USA')
        print('Telefon:  (650) 555-1212')
        print('Aktualnie obsługujemy ', len(self.accountsDict), 'kont.')
