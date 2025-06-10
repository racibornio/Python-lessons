# Klasa TV razem z kodem testowym.

class TV():
    def __init__(self):
        self.isOn = False
        self.isMuted = False
        # Domyślna lista kanałów.
        self.channelList = [2, 4, 5, 7, 9, 11, 20, 36, 44, 54, 65]
        self.nChannels = len(self.channelList)
        self.channelIndex = 0
        self.VOLUME_MINIMUM = 0  # Stała.
        self.VOLUME_MAXIMUM = 10  # Stała.
        self.volume = self.VOLUME_MAXIMUM // 2  # Dzielenie całkowite.

    def power(self):
        self.isOn = not self.isOn   # Przełączanie wartości.

    def volumeUp(self):
        if not self.isOn:
            return
        if self.isMuted:
            self.isMuted = False  # Zmiana wartości przy wyciszonym dźwięku powoduje jego włączenie.
        if self.volume < self.VOLUME_MAXIMUM:
            self.volume = self.volume + 1

    def volumeDown(self):
        if not self.isOn:
            return
        if self.isMuted:
            self.isMuted = False  # Zmiana wartości przy wyciszonym dźwięku powoduje jego włączenie.
        if self.volume > self.VOLUME_MINIMUM:
            self.volume = self.volume - 1

    def channelUp(self):
        if not self.isOn:
            return
        self.channelIndex = self.channelIndex + 1
        if self.channelIndex == self.nChannels:
            self.channelIndex = 0  # Zawinięcie wartości i przejście do pierwszego kanału.

    def channelDown(self):
        if not self.isOn:
            return
        self.channelIndex = self.channelIndex - 1
        if self.channelIndex < 0:
            self.channelIndex = self.nChannels - 1    # Zawinięcie wartości i przejście do ostatniego kanału.

    def mute(self):
        if not self.isOn:
            return
        self.isMuted = not self.isMuted

    def setChannel(self, newChannel):
        if newChannel in self.channelList:
            self.channelIndex = self.channelList.index(newChannel)
        # Jeżeli wartość newChannel nie znajduje się na liście kanałów, nie zostanie podjęte żadne działanie.

    def showInfo(self):
        print()
        print('Stan telewizora:')
        if self.isOn:
            print('    Telewizor jest: włączony')
            print('    Aktualny kanał:', self.channelList[self.channelIndex])
            if self.isMuted:
                print('    Głośność:', self.volume, '(dźwięk jest wyciszony)')
            else:
                print('    Głośność:', self.volume)
        else:
            print('    TV is: Off')


# Kod główny.
oTV = TV()  # Utworzenie obiektu typu TV.

# Włączenie telewizora i wyświetlenie informacji o stanie.
oTV.power()
oTV.showInfo()

# Dwukrotna zmiana kanału na następny, dwukrotne zwiększenie głośności i wyświetlenie informacji o stanie.
oTV.channelUp()
oTV.channelUp()
oTV.volumeUp()
oTV.volumeUp()
oTV.showInfo()

# Wyłączenie telewizora, wyświetlenie informacji o stanie, włączenie telewizora i wyświetlenie informacji o stanie.
oTV.power()
oTV.showInfo()
oTV.power()
oTV.showInfo()

# Zmniejszenie poziomu głośności, wyłączenie dźwięku i wyświetlenie informacji o stanie.
oTV.volumeDown()
oTV.mute()
oTV.showInfo()

# Zmiana kanału na 11, wyłączenie i wyświetlenie informacji o stanie, wyłączenie i wyświetlenie informacji o stanie.
oTV.setChannel(11)
oTV.mute()
oTV.showInfo()
