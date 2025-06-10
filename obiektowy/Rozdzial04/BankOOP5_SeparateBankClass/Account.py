# Klasa Account.

class Account():
    def __init__(self, name, balance, password):
        self.name = name
        self.balance = int(balance)
        self.password = password

    def deposit(self, amountToDeposit, password):
        if password != self.password:
            print('Podane hasło jest nieprawidłowe.')
            return None

        if amountToDeposit < 0:
            print('Kwota wpłaty musi być wartością dodatnią.')
            return None

        self.balance = self.balance + amountToDeposit
        return self.balance

    def withdraw(self, amountToWithdraw, password):
        if password != self.password:
            print('Hasło do tego konta jest nieprawidłowe.')
            return None

        if amountToWithdraw < 0:
            print('Kwota wypłaty musi być wartością dodatnią.')
            return None

        if amountToWithdraw > self.balance:
            print('Kwota wypłaty nie może być większa od wysokości salda.')
            return None

        self.balance = self.balance - amountToWithdraw
        return self.balance

    def getBalance(self, password):
        if password != self.password:
            print('Podane hasło jest nieprawidłowe.')
            return None
        return self.balance

    # Kod dodany na potrzeby debugowania.
    def show(self):
        print('       Imię:', self.name)
        print('       Saldo:', self.balance)
        print('       Hasło:', self.password)
        print()


