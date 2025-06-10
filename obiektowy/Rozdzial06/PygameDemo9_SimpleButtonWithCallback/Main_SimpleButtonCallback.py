# Demo pygame 9 - trzy przyciski z odmiennymi sposobami obsługi ich kliknięcia.

# 1 - Importowanie pakietów.
import pygame
from pygame.locals import *
from SimpleButton import *
import sys

# 2 - Definiowanie stałych.
GRAY = (200, 200, 200)
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 100
FRAMES_PER_SECOND = 30

# Definicja funkcji używanej jako "wywołanie zwrotne".
def myCallBackFunction():
    print('Użytkownik kliknął przycisk B, wywołano funkcję myCallBackFunction()')

# Utworzenie klasy razem z metodą przeznaczoną do użycia jako "wywołanie zwrotne".
class CallBackTest():
    def __init__(self):
        pass

    def myMethod(self):
        print('Użytkownik kliknął przycisk C, wywołano metodę myMethod() obiektu CallBackTest.')

# 3 - Inicjalizacja środowiska pygame.
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Wczytanie zasobów: obrazy, dźwięki itd.

# 5 - Inicjalizacja zmiennych.

oCallBackTest = CallBackTest()
# Utworzenie egzemplarzy typu SimpleButton.
# Brak wywołania zwrotnego.
oButtonA = SimpleButton(window, (25, 30),
                        'images/buttonAUp.png',
                        'images/buttonADown.png')
# Określenie funkcji wywołania zwrotnego.
oButtonB = SimpleButton(window, (150, 30),
                        'images/buttonBUp.png',
                        'images/buttonBDown.png',
                        callBack=myCallBackFunction)
# Określenie metody obiektu działającej jako wywołanie zwrotne.
oButtonC = SimpleButton(window, (275, 30),
                        'images/buttonCUp.png',
                        'images/buttonCDown.png',
                        callBack=oCallBackTest.myMethod)
counter = 0


# 6 - Pętla działająca w nieskończoność.
while True:

    # 7 - Sprawdzenie pod kątem zdarzeń i ich obsługa.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Przekazanie zdarzenia do przycisku w celu sprawdzenia, czy został kliknięty.
        if oButtonA.handleEvent(event):
            print('Użytkownik kliknął przycisk A, który został obsłużony w pętli głównej.')

        # Egzemplarze oButtonB i oButtonC mają zdefiniowane wywołania zwrotne,
        # nie ma potrzeby sprawdzania wyników tych wywołań.
        oButtonB.handleEvent(event)

        oButtonC.handleEvent(event)

    # 8 - Wykonywanie wszelkich akcji dla „danej klatki”.
    counter = counter + 1

    # 9 - Usunięcie zawartości okna.
    window.fill(GRAY)

    # 10 - Wyświetlenie wszystkich elementów okna.
    oButtonA.draw()
    oButtonB.draw()
    oButtonC.draw()

    # 11 - Uaktualnienie okna.
    pygame.display.update()

    # 12 - Niewielkie spowolnienie całości.
    clock.tick(FRAMES_PER_SECOND)  # Framework pygame wstrzyma na chwilę działanie.
