
def print_hi(name):

    print(f'Hi, {name}')


if __name__ == '__main__':
    print_hi('PyCharm')


# 1 BEGIN #####################################################
# wyświetlanie na ekranie wiadomości, pobranie wartości z klawiatury i jej wyświetlenie
def typeAndDisplay():
    print("Wpisz frazę i naciśnij Enter")
    przechowajWpis = input()
    print(przechowajWpis)
    print("Process terminated.")

typeAndDisplay()

# 1 END ######################################################


# 2 BEGIN #####################################################
# to jest lista - nie tablica! Lista może przechowywać różne typy danych, żre więcej pamięci niż tablica

def displayList():
    myList1 = {2.45, 6, 8, 10, "m"}
    for iterator in myList1:
        print(iterator)

displayList()

# 2 END ######################################################


# TABLICE - BEGIN #####################################################
# to jest tablica - przyjmuje tylko jeden typ danej w każdej instancji
# nie są też wbudowane w Pythona, stąd należy je zaimportować - patrz wyżej
# dzięki homogeniczności potrzebują mniej pamięci od list

# BEGIN ------------------------------------------------------
#zaimportowana w ten sposób:
#import  array
#daje się wywołać tak:
# tablica = array.array()

myArray1 = array.array('i', [1, 2, 3])
print("This is the array:", myArray1)
for iterator in myArray1:
    print(iterator)
# END ------------------------------------------------------


# BEGIN ------------------------------------------------------
#zaimportowana w ten sposób:
#import array as arr # ==> arr.array()
#daje się wywołać tak:
# tablica = arr.array()
# END------------------------------------------------------


# BEGIN ------------------------------------------------------
#zaimportowana w ten sposób:
#from array import *
#daje się wywołać tak:
#tablica = array()
# END ------------------------------------------------------

# TABLICE - END ######################################################