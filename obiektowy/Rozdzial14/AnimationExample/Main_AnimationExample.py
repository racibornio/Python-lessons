# Przykład użycia animacji.
# Wykorzystane zostały obiekty klas Animation i SpriteSheetAnimation.

# 1 - Importowanie bibliotek.
import pygame
from pygame.locals import *
import sys
import pygwidgets

# 2 Definiowanie stałych.
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
FRAMES_PER_SECOND = 30
BGCOLOR = (220, 220, 220)

# Zdefiniowane funkcji używanej jako "wywołanie zwrotne".
def myFunction(theNickname):
    if theNickname is None:
        print('W funkcji myFunction() animacja została zakończona.')
    else:
        print('W funkcji myFunction() animacja o nazwie', theNickname, 'została zakończona.')

# Zdefiniowanie przykładowej klasy z przykładową metodą przeznaczoną do użycia jako "wywołanie zwrotne".
class CallBackTest():
    def myMethod(self, theNickname):
        if theNickname is None:
            print('W metodzie myMethod() animacja została zakończona')
        else:
            print('W metodzie myMethod() animacja o nazwie', theNickname, 'została zakończona.')

# 3 - Inicjalizacja środowiska pygame.
pygame.init()
window = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
clock = pygame.time.Clock()

# 4 - Wczytanie zasobów: obrazy, dźwięki itd.
dinosaurAnimList = [('images/Dinowalk/f1.png', .1),
                      ('images/Dinowalk/f2.png', .1),
                      ('images/Dinowalk/f3.png', .1),
                      ('images/Dinowalk/f4.png', .1),
                      ('images/Dinowalk/f5.png', .1),
                      ('images/Dinowalk/f6.png', .1),
                      ('images/Dinowalk/f7.png', .1),
                      ('images/Dinowalk/f8.png', .1),
                      ('images/Dinowalk/f9.png', .1),
                      ('images/Dinowalk/f10.png', .1),
                      ('images/Dinowalk/f11.png', .1),
                      ('images/Dinowalk/f12.png', .1),
                      ('images/Dinowalk/f13.png', .1),
                      ('images/Dinowalk/f14.png', .1),
                      ('images/Dinowalk/f15.png', .1),
                      ('images/Dinowalk/f16.png', .1),
                      ('images/Dinowalk/f17.png', .1)]

# Tyranozaur.
TRexAnimationList = [('images/TRex/f1.gif', .1),
                      ('images/TRex/f2.gif', .1),
                      ('images/TRex/f3.gif', .1),
                      ('images/TRex/f4.gif', .1),
                      ('images/TRex/f5.gif', .1),
                      ('images/TRex/f6.gif', .1),
                      ('images/TRex/f7.gif', .1),
                      ('images/TRex/f8.gif', .1),
                      ('images/TRex/f9.gif', .1),
                      ('images/TRex/f10.gif', .1)]

# 5 - Inicjalizacja zmiennych.
oCallBackTest = CallBackTest() # Utworzenie obiektu testowego.
oTitleText = pygwidgets.DisplayText(window, (110, 80), \
                                    'Animacje                      SpriteSheetAnimations', fontSize=32)
oDinosaurAnimation = pygwidgets.Animation(window, (22, 145), dinosaurAnimList,
                                     autoStart=True, loop=False, callBack=myFunction, nickname='Dinozaur')
oPlayButton = pygwidgets.TextButton(window, (20, 240), "Uruchom")
oPauseButton = pygwidgets.TextButton(window, (20, 280), "Wstrzymaj")
oStopButton = pygwidgets.TextButton(window, (20, 320), "Stop")
oLoopCheckBox = pygwidgets.TextCheckBox(window, (20, 370), "Pętla", value=False)
oShowCheckBox = pygwidgets.TextCheckBox(window, (20, 400), "Pokaż", value=True)

oTRexAnimation = pygwidgets.Animation(window, (180, 140), TRexAnimationList, \
                                       autoStart=False, loop=False, nIterations=3, callBack=oCallBackTest.myMethod)
oInstructionsText = pygwidgets.DisplayText(window, (160, 320), '(Kliknij obraz, aby aktywować)')

oEffectAnimation = pygwidgets.SpriteSheetAnimation(window, (400, 150), 'images/effect_010.png',
                                         35, 192, 192, .1, autoStart=True, loop=True)

oWalkAnimation = pygwidgets.SpriteSheetAnimation(window, (460, 335), 'images/male_walkcycle.png',
                            36, 64, 64, \
                            (.1, .1, .1, .1, .1, .1, .1, .1, .3, .1, .1, .1, .1, .1, .1, .1, .1, .3, \
                             .1, .1, .1, .1, .1, .1, .1, .1, .3, .1, .1, .1, .1, .1, .1, .1, .1, .3), \
                             autoStart=False, loop=False)

oStartButton = pygwidgets.TextButton(window, (440, 400), "Start")

# 6 - Pętla działająca w nieskończoność.
while True:

    # 7 - Sprawdzenie pod kątem zdarzeń i ich obsługa.
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if oPlayButton.handleEvent(event):
            oDinosaurAnimation.start()

        if oPauseButton.handleEvent(event):
            oDinosaurAnimation.pause()

        if oStopButton.handleEvent(event):
            oDinosaurAnimation.stop()

        if oLoopCheckBox.handleEvent(event):
            currentLoopState = oDinosaurAnimation.getLoop()
            oDinosaurAnimation.setLoop(not currentLoopState)

        if oShowCheckBox.handleEvent(event):
            showState = oDinosaurAnimation.getVisible()
            if showState:
                oDinosaurAnimation.hide()
            else:
                oDinosaurAnimation.show()

        if oStartButton.handleEvent(event):
            oWalkAnimation.start()

        if oDinosaurAnimation.handleEvent(event):
            oDinosaurAnimation.start()

        if oTRexAnimation.handleEvent(event):
            oTRexAnimation.start()


    # 8 - Wykonywanie wszelkich akcji dla „danej klatki”.
    if oTRexAnimation.update():
        print('W kodzie głównym - zakończenie animacji tyranozaura.')
    if oDinosaurAnimation.update():
        print('W kodzie głównym - zakończenie animacji dinnozaura.')
    if oEffectAnimation.update():
        print('W kodzie głównym - zakończenie animacji efektu.')
    if oWalkAnimation.update():
        print('W kodzie głównym - zakończenie animacji człowieka.')

    # 9 - Usunięcie zawartości okna.
    window.fill(BGCOLOR)

    # 10 - Wyświetlenie wszystkich elementów okna.
    oTitleText.draw()
    oDinosaurAnimation.draw()
    oPlayButton.draw()
    oPauseButton.draw()
    oStopButton.draw()
    oLoopCheckBox.draw()
    oShowCheckBox.draw()
    oTRexAnimation.draw()
    oInstructionsText.draw()
    oEffectAnimation.draw()
    oWalkAnimation.draw()
    oStartButton.draw()

    # 11 - Uaktualnienie okna.
    pygame.display.update()

    # 12 - Niewielkie spowolnienie całości.
    clock.tick(FRAMES_PER_SECOND)  # Framework pygame wstrzyma na chwilę działanie.
