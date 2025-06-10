# Scena B.

import pygwidgets
import pyghelpers
import pygame
from pygame.locals import *
from Constants import *

class SceneB(pyghelpers.Scene):
    def __init__(self, window):
        self.window = window

        self.messageField = pygwidgets.DisplayText(self.window,
                            (15, 25), 'To jest scena B', fontSize=50,
                            textColor=WHITE, width=610, justified='center')

        self.gotoAButton = pygwidgets.TextButton(self.window,
                                    (100, 100), 'Przejdź na scenę A')
        self.gotoBButton = pygwidgets.TextButton(self.window,
                                    (250, 100), 'Przejdź na scenę B')
        self.gotoCButton = pygwidgets.TextButton(self.window,
                                    (400, 100), 'Przejdź na scenę C')
        self.gotoBButton.disable()

    def getSceneKey(self):
        return SCENE_B

    def handleInputs(self, eventsList, keyPressedList):
        for event in eventsList:
            if self.gotoAButton.handleEvent(event):
                self.goToScene(SCENE_A)

            if self.gotoCButton.handleEvent(event):
                self.goToScene(SCENE_C)

            # Testowanie:  Naciśnij a lub c, aby wysłać komunikat na te sceny.
            #              Naciśnij 1 lub 3, aby pobrać dane ze scen A i C.
            #              Naciśnij x, aby wysłać komunikat na wszystkie sceny.
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.send(SCENE_A, SEND_MESSAGE,
                                    'Wysyłanie komunikatu na scenę A')

                if event.key == pygame.K_c:
                    self.send(SCENE_C, SEND_MESSAGE,
                                    'Wysyłanie komunikatu na scenę C')

                if event.key == pygame.K_1:
                    answer = self.request(SCENE_A, GET_DATA)
                    print('Otrzymano dane ze sceny A')
                    print('Odpowiedź miała postać:', answer)

                if event.key == pygame.K_3:
                    answer = self.request(SCENE_C, GET_DATA)
                    print('Otrzymano dane ze sceny C')
                    print('Odpowiedź miała postać:', answer)

                if event.key == pygame.K_x:
                    self.sendAll(SEND_MESSAGE,
                                 'Wysyłanie komunikatu na wszystkie sceny.')

    def draw(self):
        self.window.fill(GRAYB)
        self.messageField.draw()
        self.gotoAButton.draw()
        self.gotoBButton.draw()
        self.gotoCButton.draw()

    def receive(self, receiveID, data):
        print('Na scenie B.')
        print('Otrzymano komunikat typu:', receiveID)
        print('Otrzymane dane to:', data)

    def respond(self, msgType):
        if msgType == GET_DATA:
            return 'To są dane pochodzące ze sceny B.'
