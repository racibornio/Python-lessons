# Person class

class Person():

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # Umożliwienie komponentowi wywołującemu pobrania wartości salary.
    def getSalary(self):
        return self.salary

    # Umożliwienie komponentowi wywołującemu przypisania wartości salary.
    def setSalary(self, salary):
        self.salary = salary
