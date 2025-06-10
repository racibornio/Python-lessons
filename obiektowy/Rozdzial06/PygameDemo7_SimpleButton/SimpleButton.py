# Klasa SimpleButton.
#
# Wykorzystano podejście „maszyny stanów”.
#

import pygame
from pygame.locals import *

class SimpleButton():
    # Stałe używane do śledzenia stanu przycisku.
    STATE_IDLE = 'idle' # Przycisk jest nienaciśnięty, kursor myszy nie znajduje się nad przyciskiem.
    STATE_ARMED = 'armed' # Przycisk jest naciśnięty, kursor myszy znajduje się nad przyciskiem.
    STATE_DISARMED = 'disarmed' # Przycisk jest naciśnięty, kursor myszy nie znajduje się nad przyciskiem.

    def __init__(self, window, loc, up, down):
        self.window = window
        self.loc = loc
        self.surfaceUp = pygame.image.load(up)
        self.surfaceDown = pygame.image.load(down)

        # Pobranie prostokąta ograniczającego przycisk (używany do sprawdzenia, czy kursor myszy znajduje się nad przyciskiem).
        self.rect = self.surfaceUp.get_rect()
        self.rect[0] = loc[0]
        self.rect[1] = loc[1]

        self.state = SimpleButton.STATE_IDLE

    def handleEvent(self, eventObj):
        # Ta metoda zwróci wartość True, jeżeli użytkownik kliknie przycisk.
        # Standardowo wartością zwrotną jest False.

        if eventObj.type not in (MOUSEMOTION, MOUSEBUTTONUP, MOUSEBUTTONDOWN):
            # Ważne są tylko zdarzenia powiązane z myszą.
            return False

        eventPointInButtonRect = self.rect.collidepoint(eventObj.pos)

        if self.state == SimpleButton.STATE_IDLE:
            if (eventObj.type == MOUSEBUTTONDOWN) and eventPointInButtonRect:
                self.state = SimpleButton.STATE_ARMED

        elif self.state == SimpleButton.STATE_ARMED:
            if (eventObj.type == MOUSEBUTTONUP) and eventPointInButtonRect:
                self.state = SimpleButton.STATE_IDLE
                return True  # Kliknięty!

            if (eventObj.type == MOUSEMOTION) and (not eventPointInButtonRect):
                self.state = SimpleButton.STATE_DISARMED

        elif self.state == SimpleButton.STATE_DISARMED:
            if eventPointInButtonRect:
                self.state = SimpleButton.STATE_ARMED
            elif eventObj.type == MOUSEBUTTONUP:
                self.state = SimpleButton.STATE_IDLE

        return False

    def draw(self):
        # Wyświetlenie w oknie aktualnego wyglądu przycisku.
        if self.state == SimpleButton.STATE_ARMED:
            self.window.blit(self.surfaceDown, self.loc)

        else:  # Stan IDLE lub DISARMED.
            self.window.blit(self.surfaceUp, self.loc)
