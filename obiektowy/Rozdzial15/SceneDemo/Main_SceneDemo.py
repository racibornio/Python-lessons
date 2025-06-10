# Przykładowy program główny używający trzech scen.

# To jest przykład typowego programu głównego, który korzysta z menedżera scen.
# Na początku trzeba zdefiniować wielkość okna, zainicjalizować pygame i utworzyć okno.
# Następnym krokiem jest utworzenie egzemplarzy poszczególnych scen.
# Później trzeba wymienić wszystkie sceny, a lista będzie miała następującą postać:
#    [<egzemplarzSceny1>, <egzemplarzSceny2>, ... <egzemplarzScenyN>]
# Pierwsza scena na liście zostanie użyta jako początkowa.
# Kolejność pozostałych scen nie ma znaczenia.
# Używając tej listy, scenesList, i podanej liczby klatek na sekundę tworzysz obiekt typu SceneMgr.
# Następnie w tym obiekcie trzeba wywołać metodę run().
# Egzemplarz SceneMgr przejmuje kontrolę, uruchamia pętlę główną oraz zapewnia obsługę nawigacji i komunikacji między scenami.

# 1 - Importowanie pakietów.
import pygame
import pyghelpers
from SceneA import *
from SceneB import *
from SceneC import *

# 2 - Definiowanie stałych.
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 180
FRAMES_PER_SECOND = 30

# 3 - Inicjalizacja środowiska pygame.
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# 4 - Wczytanie zasobów: obrazy, dźwięki itd.

# 5 - Inicjalizacja zmiennych.
# Przygotowanie wszystkich scen i umieszczenie ich na liście.
scenesList = [SceneA(window),
              SceneB(window),
              SceneC(window)]

# Utworzenie menedżera scen, a także przekazanie mu listy scen i oczekiwanej liczby klatek na sekundę.
oSceneMgr = pyghelpers.SceneMgr(scenesList, FRAMES_PER_SECOND)

# Nakazanie menedżerowi scen uruchomienia programu.
oSceneMgr.run()
