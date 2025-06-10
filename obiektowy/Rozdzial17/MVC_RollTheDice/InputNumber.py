# Klasa InputNumber - pozwala użytkownikowi na wpisywanie jedynie liczb.
#
# Przykład użycia dziedziczenia.

import pygame
from pygame.locals import *
import pygwidgets

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
# Krotka dozwolonych klawiszy edycji.
LEGAL_KEYS_TUPLE = (pygame.K_RIGHT, pygame.K_LEFT, pygame.K_HOME,
                    pygame.K_END, pygame.K_DELETE, pygame.K_BACKSPACE,
                    pygame.K_RETURN, pygame.K_KP_ENTER)
# Jedyne znaki, które mogą być wpisane.
LEGAL_UNICODE_CHARS = ('0123456789.-')

#
#  Klasa InputNumber dziedziczy po InputText.
#
class InputNumber(pygwidgets.InputText):

    def __init__(self, window, loc, value='', fontName=None,
                 fontSize=24, width=200, textColor=BLACK,
                 backgroundColor=WHITE, focusColor=BLACK,
                 initialFocus=False, nickName=None, callback=None,
                 mask=None, keepFocusOnSubmit=False,
                 allowFloatingNumber=True, allowNegativeNumber=True):
        self.allowFloatingNumber = allowFloatingNumber
        self.allowNegativeNumber = allowNegativeNumber

        # Wywołanie metody __init__() klasy bazowej.
        super().__init__(window, loc, value, fontName, fontSize,
                         width, textColor, backgroundColor,
                         focusColor, initialFocus, nickName, callback,
                         mask, keepFocusOnSubmit)

    # Nadpisanie metody handleEvent(), aby można było odfiltrować niedozwolone znaki.
    def handleEvent(self, event):
        if (event.type == pygame.KEYDOWN):
            # Jeżeli naciśnięty jest klawisz inny niż edycyjny lub liczbowy, należy do zignorować.
            # Wartość Unicode jest dostępna jedynie po naciśnięciu klawisza.
            allowableKey = ((event.key in LEGAL_KEYS_TUPLE) or
                            (event.unicode in LEGAL_UNICODE_CHARS))
            if not allowableKey:
                return False

            if event.unicode == '-':  # Użytkownik wpisał znak minusa.
                if not self.allowNegativeNumber:
                    # Jeżeli liczba ujemna jest niedozwolona, nie będzie przekazana dalej.
                    return False
                if self.cursorPosition > 0:
                    return False # Znak minus nie może być umieszczony po pierwszym znaku.
                if '-' in self.text:
                    return False  # Nie można wpisać drugiego znaku minusa.

            if event.unicode == '.':
                if not self.allowFloatingNumber:
                    # Jeżeli liczba zmiennoprzecinkowa jest niedozwolona, nie można użyć przecinka dziesiętnego.
                    return False
                if '.' in self.text:
                    return False  # Nie można wpisać drugiego przecinka dziesiętnego.

        # Naciśnięty klawisz może być przekazany klasie bazowej.
        result = super().handleEvent(event)
        return result

    def getValue(self):
        userString = super().getValue()
        try:
            if self.allowFloatingNumber:
                returnValue = float(userString)
            else:
                returnValue = int(userString)
        except ValueError:
            raise ValueError('Wartość nie jest liczbą, konieczne jest podanie przynajmniej jednej cyfry.')

        return returnValue

