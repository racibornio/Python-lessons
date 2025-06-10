# Klasa SimpleSpriteSheetAnimation.

import pygame
import time

class SimpleSpriteSheetAnimation():
    def __init__(self, window, loc, imagePath, nImages, width, height, durationPerImage):
        self.window = window
        self.loc = loc
        self.nImages = nImages
        self.imagesList = []

        # Wczytanie arkusza duszków.
        spriteSheetImage = pygame.image.load(imagePath)
        # Optymalizacja obrazów przeznaczonych do wyświetlenia na ekranie.
        spriteSheetImage = pygame.Surface.convert_alpha(spriteSheetImage)

        # Obliczenie liczby kolumn na początkowym obrazie.
        nCols = spriteSheetImage.get_width() // width

        # Podział obrazu początkowego na podobrazy.
        row = 0
        col = 0
        for imageNumber in range(nImages):
            x = col * height
            y = row * width

            # Utworzenie podpowierzchni na podstawie większego arkusza duszków.
            subsurfaceRect = pygame.Rect(x, y, width, height)
            image = spriteSheetImage.subsurface(subsurfaceRect)
            self.imagesList.append(image)

            col = col + 1
            if col == nCols:
                col = 0
                row = row + 1

        self.durationPerImage = durationPerImage
        self.playing = False
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
