import math

class Fraction():
    def __init__(self, numerator, denominator):
        if not isinstance(numerator, int):
            raise TypeError('Licznik', numerator, 'musi być liczbą całkowitą.')
        if not isinstance(denominator, int):
            raise TypeError('Mianownik', denominator, 'musi być liczbą całkowitą.')
        self.numerator = numerator
        self.denominator = denominator

        # Użycie pakietu math do znalezienia największego wspólnego dzielnika.
        greatestCommonDivisor = math.gcd(self.numerator, self.denominator)
        if greatestCommonDivisor > 1:
            self.numerator = self.numerator // greatestCommonDivisor
            self.denominator = self.denominator // greatestCommonDivisor
        self.value = self.numerator / self.denominator

        # Normalizacja znaku licznika i mianownika.
        self.numerator = int(math.copysign(1.0, self.value)) * abs(self.numerator)
        self.denominator = abs(self.denominator)

    def getValue(self):
        return self.value

    def __str__(self):
        '''Utworzenie tekstowej reprezentacji ułamka.'''
        output = '  Ułamek: ' + str(self.numerator) + '/' + \
                 str(self.denominator) + '\n' +\
                '  Wartość: ' + str(self.value) + '\n'
        return output

    def __add__(self, oOtherFraction):
        '''Dodanie dwóch obiektów typu Fraction.'''
        if not isinstance(oOtherFraction, Fraction):
            raise TypeError('Druga wartość w działaniu nie jest typu Fraction.')
        # Użycie pakietu math do znalezienia najmniejszej wspólnej wielokrotności.
        newDenominator = math.lcm(self.denominator, oOtherFraction.denominator)

        multiplicationFactor = newDenominator // self.denominator
        equivalentNumerator = self.numerator * multiplicationFactor

        otherMultiplicationFactor = newDenominator // oOtherFraction.denominator
        oOtherFractionEquivalentNumerator = oOtherFraction.numerator * otherMultiplicationFactor

        newNumerator = equivalentNumerator + oOtherFractionEquivalentNumerator

        oAddedFraction = Fraction(newNumerator, newDenominator)
        return oAddedFraction

    def __eq__(self, oOtherFraction):
        '''Sprawdzenie równości.'''
        if not isinstance(oOtherFraction, Fraction):
            return False  # Brak porównania z ułamkiem.
        if (self.numerator == oOtherFraction.numerator) and \
           (self.denominator == oOtherFraction.denominator):
            return True
        else:
            return False

 # Kod testujący klasę Fraction.
oFraction1 = Fraction(1, 3)  # Utworzenie obiektu typu Fraction.
oFraction2 = Fraction(2, 5)
print('Obiekt Fraction1\n', oFraction1)  # Wyświetlenie obiektu... wywołanie metody __str__().
print('Obiekt Fraction2\n', oFraction2)

oSumFraction = oFraction1 + oFraction2  # Wywołanie metody __add__().
print('Suma wynosi\n', oSumFraction)

print('Czy obiekty Fraction1 i Fraction2 są takie ?', (oFraction1 == oFraction2)) # Oczekiwana wartość to False.
print()

oFraction3 = Fraction(-20, 80)
oFraction4 = Fraction(4, -16)
print('Obiekt Fraction3\n', oFraction3)
print('Obiekt Fraction4\n', oFraction4)
print('Czy obiekty Fraction3 i Fraction4 są takie same?', (oFraction3 == oFraction4)) # Oczekiwana wartość to True.
print()

oFraction5 = Fraction(5, 2)
oFraction6 = Fraction(500, 200)
print('Suma 5/2 i 500/2\n', oFraction5 + oFraction6)
