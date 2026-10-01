import random
import sys

from pandas.core.interchange.from_dataframe import primitive_column_to_ndarray

liczba = 0
while liczba < 5:
    print("Liczba:", liczba)
    if liczba == 3:
        break
    liczba = liczba + 1


total = 0
for i in range(101):
    total = total + i

print(total)

total = 0
i = 0
while i < 101:
    total = total + i
    i = i + 1


print(total)

for i in range(5):
    print(random.randint(1, 100))



liczba = int(input("Podaj liczbę do 100:"))
if liczba > 100:
    print("Podałeś za dużą liczbę")
    sys.exit()
else:
    print("Podałeś", liczba)


def wpisz():
    napis = input("Wpisz...")
    return len(napis)

dlugosc = wpisz()

print(dlugosc)

for i in range (10,0):
    print(i)


print('siemanko', end=':-)')
print()

"""random number z funkcji random()"""
rn = random.random()
print("Random number from random() :", rn)


"""random number z funkcji randint(min, max)"""
rnd = random.randint(-90, -80)
print("Random number from random() :", rnd)


"""rzutowanie typów"""
value_to_cast = input("Enter a number:")
print(value_to_cast, "- type:", type(value_to_cast))
integered = int(value_to_cast)
print(value_to_cast, "- casted to int:", type(integered))
floated = float(integered)
print(value_to_cast, "- casted to float:", type(floated))


"""pętla i wychodzenie z pętli"""
while True:
    value = input("Enter a value:")
    if value == ' ':
        break
    else:
        print("You typed", value)


print("The loop is over.")


zmienna = 4
print('Czy zmienna typu int? - ', isinstance(zmienna, int))

inna_zmienna = 'fda'
print('Czy zmienna typu int lub float? - ', isinstance(inna_zmienna, (int, float)))
print('Czy zmienna typu string? - ', isinstance(inna_zmienna, str))

"""use sys.exit"""
# while True:
#     value = input("Enter a value to check sys.exit():")
#     integered_value = int(value)
#     if integered_value < 0:
#         print("Negative number - the program will end now...")
#         sys.exit()
#
#
#     print("You entered", value)