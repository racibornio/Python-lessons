# Klasa Account.
# Błędy wskazywane przez polecenia "raise".

# Zdefiniowanie własnego wyjątku.
class AbortTransaction(Exception):
    '''Polecenie raise zgłasza wyjątek w celu przerwania transakcji bankowej.'''
    pass

class Account():
    def __init__(self, name, balance, password):
        self.name = name
        self.balance = self.validateAmount(balance)
        self.password = password

    def validateAmount(self, amount):
        try:
            amount = int(amount)
        except ValueError:
            raise AbortTransaction('Wartość musi być liczbą całkowitą.')
        if amount <= 0:
            raise AbortTransaction('Wartość musi być liczbą dodatnią.')
        return amount

    def checkPasswordMatch(self, password):
        if password != self.password:
            raise AbortTransaction('Hasło do tego konta jest nieprawidłowe.')

    def deposit(self, amountToDeposit):
        amountToDeposit = self.validateAmount(amountToDeposit)
        self.balance = self.balance + amountToDeposit
        return self.balance

    def getBalance(self):
        return self.balance

    def withdraw(self, amountToWithdraw):
        amountToWithdraw = self.validateAmount(amountToWithdraw)
        if amountToWithdraw > self.balance:
            raise AbortTransaction('Kwota wypłaty nie może być większa od wysokości salda.')

        self.balance = self.balance - amountToWithdraw
        return self.balance

    # Kod dodany na potrzeby debugowania.
    def show(self):
        print('       Imię:', self.name)
        print('       Saldo:', self.balance)
        print('       Hasło:', self.password)
