# Program przeznaczony do testowania okien dialogowych.

import sys
import os

# Te polecenia są na wypadek uruchomienia programu z poziomu powłoki.
currentPath = os.path.dirname(os.path.abspath(__file__))
sys.path.append(currentPath)

# 1 - Importowanie pakietów.
import pygame
import pygwidgets
import pyghelpers

# 2 - Definiowanie stałych.
BLACK = (0, 0, 0)
BACKGROUND_COLOR = (0, 138, 138)
WHITE = (255, 255, 255)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30


def showCustomAlertDialog(theWindow, theText):
    oDialogBackground = pygwidgets.Image(theWindow, (60, 80),
                                            'images/dialog.png')
    oPromptDisplayText = pygwidgets.DisplayText(theWindow, (0, 150),
                                            theText, width=WINDOW_WIDTH,
                                            justified='center', fontSize=36)
    oOKButton = pygwidgets.CustomButton(theWindow, (355, 235),
                                            'images/okNormal.png',
                                            over='images/okOver.png',
                                            down='images/okDown.png',
                                            disabled='images/okDisabled.png')
    response = pyghelpers.customYesNoDialog(theWindow,
                                            oDialogBackground,
                                            oPromptDisplayText,
                                            oOKButton, None)
    return response


def showCustomYesNoDialog(theWindow, theText):
    oDialogBackground = pygwidgets.Image(theWindow, (60, 80),
                                            'images/dialog.png')
    oPromptDisplayText = pygwidgets.DisplayText(theWindow, (0, 150),
                                            theText, width=WINDOW_WIDTH,
                                            justified='center', fontSize=36)
    oNoButton = pygwidgets.CustomButton(theWindow, (95, 235),
                                            'images/noNormal.png',
                                            over='images/noOver.png',
                                            down='images/noDown.png',
                                            disabled='images/noDisabled.png')
    oYesButton = pygwidgets.CustomButton(theWindow, (355, 235),
                                            'images/yesNormal.png',
                                            over='images/yesOver.png',
                                            down='images/yesDown.png',
                                            disabled='images/yesDisabled.png')
    response = pyghelpers.customYesNoDialog(theWindow,
                                            oDialogBackground,
                                            oPromptDisplayText,
                                            oYesButton, oNoButton)
    return response

def showCustomAnswerDialog(theWindow, theText):
    oDialogBackground = pygwidgets.Image(theWindow, (60, 80),
                                            'images/dialog.png')
    oPromptDisplayText = pygwidgets.DisplayText(theWindow, (0, 120),
                                            theText, width=WINDOW_WIDTH,
                                            justified='center', fontSize=36)
    oUserInputText = pygwidgets.InputText(theWindow, (225, 165), '',
                                            fontSize=36, initialFocus=True)
    oNoButton = pygwidgets.CustomButton(theWindow, (105, 235),
                                            'images/cancelNormal.png',
                                            over='images/cancelOver.png',
                                            down='images/cancelDown.png',
                                            disabled='images/cancelDisabled.png')
    oYesButton = pygwidgets.CustomButton(theWindow, (375, 235),
                                            'images/okNormal.png',
                                            over='images/okOver.png',
                                            down='images/okDown.png',
                                            disabled='images/okDisabled.png')
    response = pyghelpers.customAnswerDialog(theWindow,
                                            oDialogBackground, oPromptDisplayText,
                                            oUserInputText,
                                            oYesButton, oNoButton)
    return response


# 3 - Inicjalizacja środowiska pygame.
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()  # Określenie szybkości (liczba klatek na sekundę). (frames per second)

# 4 - Wczytanie zasobów: obrazy, dźwięki itd.

# 5 - Inicjalizacja zmiennych.
oTextAlertButton = pygwidgets.TextButton(window, (75, 320), 'Komunikat tekstowy')
oCustomAlertButton = pygwidgets.TextButton(window, (75, 380), 'Komunikat niestandardowy')
oTextYesNoButton = pygwidgets.TextButton(window, (280, 320), 'Okno dialogowe typu Tak/Nie')
oCustomYesNoButton = pygwidgets.TextButton(window, (280, 380), 'Niestandardowe okno dialogowe typu Tak/Nie')
oTextAnswerButton = pygwidgets.TextButton(window, (485, 320), 'Okno dialogowe typu Odpowiedź')
oCustomAnswerButton = pygwidgets.TextButton(window, (485, 380), 'Niestandardowe okno dialogowe typu Odpowiedź')

oTitle = pygwidgets.DisplayText(window, (150, 25), 'Klikaj przycisku w celu przetestowania wszystkich okien dialogowych',
                                    fontSize=36, textColor=WHITE)
oResults = pygwidgets.DisplayText(window, (20, 450), '',
                                    fontSize=36, textColor=WHITE, width=600)

# 6 - Pętla działająca w nieskończoność.
while True:

    # 7 -  Sprawdzenie pod kątem zdarzeń i ich obsługa.
    for event in pygame.event.get():
        # Sprawdzenie, czy zdarzenie dotyczy przycisku X.
        if event.type == pygame.QUIT:
            # Po wystąpieniu tego zdarzenia należy zakończyć program.
            pygame.quit()
            sys.exit()

        if oTextAlertButton.handleEvent(event):
            ignore = pyghelpers.textYesNoDialog(window,
                                                  (75, 80, 500, 150),
                                                  'To jest powiadomienie!', 'OK', None)
            oResults.setValue('Użytkownik kliknął przycisk OK')

        if oCustomAlertButton.handleEvent(event):
            ignore = showCustomAlertDialog(window, 'To jest powiadomienie!')
            oResults.setValue('Użytkownik kliknął przycisk OK')

        if oTextYesNoButton.handleEvent(event):
            returnedValue = pyghelpers.textYesNoDialog(window, (75, 80, 500, 150),
                                                  'Czy chcesz frytki z dodatkami?')
            if returnedValue:
                oResults.setValue('Użytkownik kliknął przycisk Tak')
            else:
                oResults.setValue('Użytkownik kliknął przycisk Tak')

        if oCustomYesNoButton.handleEvent(event):
            returnedValue = showCustomYesNoDialog(window, 'Czy chcesz frytki z dodatkami?')
            if returnedValue:
                oResults.setValue('Użytkownik kliknął przycisk Tak')
            else:
                oResults.setValue('Użytkownik kliknął przycisk Tak')

        if oTextAnswerButton.handleEvent(event):
            userAnswer = pyghelpers.textAnswerDialog(window, (75, 80, 500, 200),
                                    'Jakie lody lubisz najbardziej?', 'OK', 'Anuluj')
            if userAnswer is not None:
                oResults.setValue('Użytkownik kliknął przycisk OK, dane to: ' + userAnswer)
            else:
                oResults.setValue('Użytkownik kliknął przycisk Anuluj')

        if oCustomAnswerButton.handleEvent(event):
            userAnswer = showCustomAnswerDialog(window,
                                    'Jakie lody lubisz najbardziej?')
            if userAnswer is not None:
                oResults.setValue('Użytkownik kliknął przycisk OK, dane to: ' + userAnswer)
            else:
                oResults.setValue('Użytkownik kliknął przycisk Anuluj')

    # 8 - Wykonywanie wszelkich akcji dla „danej klatki”.

    # 9 - Usunięcie zawartości okna przed jego ponownym wyświetleniem.
    window.fill(BACKGROUND_COLOR)

    # 10 - Wyświetlenie wszystkich elementów ekranu.
    oTitle.draw()
    oTextAlertButton.draw()
    oCustomAlertButton.draw()
    oTextYesNoButton.draw()
    oCustomYesNoButton.draw()
    oTextAnswerButton.draw()
    oCustomAnswerButton.draw()
    oResults.draw()

    # 11 - Uaktualnienie okna.
    pygame.display.update()

    # 12 - Niewielkie spowolnienie całości.
    clock.tick(FRAMES_PER_SECOND)  # Framework pygame wstrzyma na chwilę działanie.
