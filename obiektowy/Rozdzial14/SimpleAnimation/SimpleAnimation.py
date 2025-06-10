# Klasa SimpleAnimation.

import pygame
import time

class SimpleAnimation():
    def __init__(self, window, loc, picPaths, durationPerImage):
        self.window = window
        self.loc = loc
        self.imagesList = []
        for picPath in picPaths:
            image = pygame.image.load(picPath)  # Wczytanie obrazu.
            image = pygame.Surface.convert_alpha(image)  # Optymalizacja wyświetlania obrazu.
            self.imagesList.append(image)

        self.playing = False
        self.durationPerImage = durationPerImage
        self.nImages = len(self.imagesList)
        self.index = 0

    def play(self):
        if self.playing:
            return
        self.playing = True
        self.imageStartTime = time.time()
        self.index = 0

    def update(self):
        if not self.playing:
            return

        # Ilość czasu, który upłynął od chwili rozpoczęcia wyświetlania tego obrazu.
        self.elapsed = time.time() - self.imageStartTime

        # Jeżeli upłynęło wystarczająco dużo czasu, należy przejść do następnego obrazu.
        if self.elapsed > self.durationPerImage:
            self.index = self.index + 1

            if self.index < self.nImages: # Przejście do następnego obrazu.
                self.imageStartTime = time.time()
            else:  # Wyświetlanie animacji zakończyło się.
                self.playing = False
                self.index = 0  # Powrót na początek animacji.

    def draw(self):
        # Przyjmowane jest założenie o wcześniejszym zdefiniowaniu wartości zmiennej self.index - w metodzie update().
        # Ta wartość jest używana jako indeks na liście imagesList, pozwalający odszukać bieżący obraz.
        theImage = self.imagesList[self.index]  # Wybór obrazu do wyświetlenia.

        self.window.blit(theImage, self.loc)   # Wyświetlenie wybranego obrazu.

