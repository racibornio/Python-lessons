# Zarządzanie scenami za pomocą menedżera scen.
# Gra "Kamień, papier, nożyce".

# 1 - Importowanie pakietów.

import pygame
import pyghelpers
import sys
from Constants import *
from SceneSplash import *
from ScenePlay import *
from SceneResults import *


# 2 - Definiowanie stałych.
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30

# 3 - Inicjalizacja środowiska pygame.
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Wczytanie zasobów: obrazy, dźwięki itd.

# 5 - Inicjalizacja zmiennych.
# Przygotowanie wszystkich scen i umieszczenie ich na liście.
scenesList = [SceneSplash(window),
              ScenePlay(window),
              SceneResults(window)]

# Utworzenie menedżera scen, a także przekazanie mu listy scen i oczekiwanej liczby klatek na sekundę.
oSceneMgr = pyghelpers.SceneMgr(scenesList, FRAMES_PER_SECOND)

# Nakazanie menedżerowi scen uruchomienia programu.
oSceneMgr.run()
