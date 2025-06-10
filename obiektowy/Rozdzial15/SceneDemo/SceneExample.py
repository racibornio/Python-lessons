#
# To jest pusta scena.
#
# To jest szablon pokazujący strukturę sceny.
#
import pygwidgets
import pyghelpers
import pygame

class MyScene(pyghelpers.Scene):  # Dziedziczy po klasie Scene w pakiecie pyghelpers.
    def __init__(self, window):
        """
        Ta metoda jest wywołana podczas tworzenia sceny.
        Utwórz i/lub wczytaj wszystkie zasoby (obrazy, przyciski, dźwięki),
        które są niezbędne na tej scenie.
        """
        self.window = window

        # W tym miejscu zostanie utworzony przycisk.
        self.navButton = pygwidgets.TextButton(self.window, (300, 230), 'Nawigacja')

    def getSceneKey(self):
        """
        Ta metoda jest wywoływana przez menedżera scen w celu pobrania klucza danej sceny.
        Ta metoda MUSI być zdefiniowana na każdej scenie w celu nadpisania metody bazowej..
        """
        return 'Dowolny ciąg tekstowy lub STAŁA unikatowo identyfikująca tę scenę.'

    def enter(self, data):
        """
        Ta metoda jest wywoływana podczas przejścia na tę scenę.
        'data' to wszelkie informacje przekazywane z poprzedniej sceny. Wartością domyślną jest None.
        Typowe rozwiązanie polega na przekazaniu słownika, z którego można pobrać użyteczne dane.
        """
        pass

    def handleInputs(self, events, keyPressedList):
        """
        Ta metoda jest wywoływana w trakcie każdej klatki, po wystąpieniu zdarzenia.
        Otrzymuje listę zdarzeń i listę aktualnie naciśniętych klawiszy.
        Typowe rozwiązanie polega na iteracji przez zdarzenia i obsługę tych, które Cię interesują.
        Ta metoda MUSI być zdefiniowana na każdej scenie w celu nadpisania metody bazowej.
        """
        for event in events:
            if self.navButton.handleEvent(event):
                print('Kliknięto przycisk nawigacji - zwykle dodaje się polecenie: self.goToScene("NewScene")')

    def update(self):
        """
        Ta metoda jest wywoływana jednokrotnie w trakcie każdej klatki, gdy scena jest aktywna.
        Umieść w niej kod, który ma być wykonany w trakcie każdej klatki.
        """
        pass

    def draw(self):
        """
        Ta metoda jest wykonywana w trakcie każdej klatki.
        Umieść w niej kod, który ma wyświetlić niezbędne elementy w oknie.
        (Zwykle to wypełnienie okna kolorem lub wyświetlenie obrazu tła,
        przycisków, pól tekstowych, znaków itd.)
        Ta metoda MUSI być zdefiniowana na każdej scenie w celu nadpisania metody bazowej.
        """
        self.navButton.draw()

    def leave(self):
        """
        Ta metoda jest wywoływana, gdy ma nastąpić przejście na inną scenę.
        Powinna zwrócić wszelkie dane, które scena bieżąca chce przekazać następnej scenie.
        Zwykle przekazywane dane to wartość None lub słownik.
        """
        return None
