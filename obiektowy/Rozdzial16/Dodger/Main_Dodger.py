# Kod główny gry Dodger.
#
# Przygotowuje trzy sceny, a także tworzy i uruchamia menedżera scen.
#
#  Oryginala wersja gry została opracowana przez Ala Sweigarta
# na potrzeby książki "Twórz własne gry komputerowe w Pythonie"
#    (koncepcja, grafika i dźwięki zostały użyte za zgodą Ala Sweigarta)

# 1 - Importowanie pakietów.
import os
# To polecenie jest na wypadek uruchomienia programu z poziomu powłoki.
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import pygame
import pyghelpers
from SceneSplash import *
from ScenePlay import *
from SceneHighScores import *

# 2 - Definiowanie stałych.
FRAMES_PER_SECOND = 40

# 3 - Inicjalizacja środowiska pygame.
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# 4 - Wczytanie zasobów: obrazy, dźwięki itd.

# 5 - Inicjalizacja zmiennych.
# Utworzenie wszystkich scen i umieszczenie ich na liście.
scenesList = [SceneSplash(window),
                    SceneHighScores(window),
                    ScenePlay(window)]

# Utworzenie menedżera scen, a także przekazanie mu listy scen i żądanej liczby klatek na sekundę.
oSceneMgr = pyghelpers.SceneMgr(scenesList, FRAMES_PER_SECOND)

# Nakazanie menedżerowi scen uruchomienia programu.
oSceneMgr.run()
