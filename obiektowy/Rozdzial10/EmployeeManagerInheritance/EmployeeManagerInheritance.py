# Klasa Employee, po której inne będą dziedziczyć.
#
# Definicja klasy Employee, która będzie używana jako klasa bazowa.
class Employee():
    def __init__(self, name, title, ratePerHour=None):
        self.name = name
        self.title = title
        if ratePerHour is not None:
            ratePerHour = float(ratePerHour)
        self.ratePerHour = ratePerHour

    def getName(self):
        return self.name

    def getTitle(self):
        return self.title

    def payPerYear(self):
        # 52 tygodnie * 5 dni w tygodniu * 8 godzin dziennie.
        pay = 52 * 5 * 8 * self.ratePerHour
        return pay


# Definicja podklasy Manager dziedziczącej po klasie Employee.
class Manager(Employee):
    def __init__(self, name, title, salary, reportsList=None):
        self.salary = float(salary)
        if reportsList is None:
            reportsList = []
        self.reportsList = reportsList
        super().__init__(name, title)

    def getReports(self):
        return self.reportsList

    def payPerYear(self, giveBonus=False):
        pay = self.salary
        if giveBonus:
            pay = pay + (.10 * self.salary)  # Dodanie premii w wysokości 10%.
            print(self.name, 'otrzymuje premię za dobre wyniki w pracy.')
        return pay

    # Dodatkowe metody unikatowe dla menedżera.
    def addEmployee(self, oEmployeeToAdd):
        self.reportsList.append(oEmployeeToAdd)

    def removeEmployee(self, oEmployeeToRemove):
        self.reportsList.remove(oEmployeeToRemove)


# Tworzenie obiektów.
oEmployee1 = Employee('Jan Kowalski', 'kucharz', 16)
oEmployee2 = Employee('Krzysztof Nowak', 'kasjer', 14)
oManager = Manager('Sara Janiak', 'menedżer restauracji',
                             55000, [oEmployee1, oEmployee2])

# Wywołanie metod obiektów Employee.
print('Imię pracownika:', oEmployee1.getName())
print('Wynagrodzenie pracownika:', '{:,.2f}'.format(oEmployee1.payPerYear()))
print('Imię pracownika:', oEmployee2.getName())
print('Wynagrodzenie pracownika:', '{:,.2f}'.format(oEmployee2.payPerYear()))
print()

# Wywołanie metod obiektów Manager.
managerName = oManager.getName()
print('Imię menedżera:', managerName)

# Menedżer zasłużył na premię.
print('Wynagrodzenie menedżera:', '{:,.2f}'.format(oManager.payPerYear(True)))
print(managerName, '(' + oManager.getTitle() + ')', 'bezpośrednio zarządza pracownikami:')
reportsList = oManager.getReports()
for oEmployee in reportsList:
    print('   ', oEmployee.getName(),
            '(' + oEmployee.getTitle() + ')')
