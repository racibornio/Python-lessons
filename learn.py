import random
import sys

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