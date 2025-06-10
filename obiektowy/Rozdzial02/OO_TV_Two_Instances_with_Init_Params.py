# Klasa TV pobierająca parametry inicjalizacyjne.

# Klasa TV.

class TV():
    def __init__(self, brand, location):  # Przekazanie marki i położenia telewizora.
        self.brand = brand
        self.location = location
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
        self.isOn = not self.isOn  # Przełączanie wartości.

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
            self.channelIndex = self.nChannels - 1  # Zawinięcie wartości i przejście do ostatniego kanału.

    def mute(self):
        if not self.isOn:
            return
        self.isMuted = not self.isMuted

    def setChannel(self, newChannel):
        if newChannel not in self.channelList:
            return  # Jeżeli wartość newChannel nie znajduje się na liście kanałów, nie zostanie podjęte żadne działanie.
        self.channelIndex = self.channelList.index(newChannel)

    def showInfo(self):
        print()
        print('Status of TV:', self.brand)
        print('    Location:', self.location)
        if self.isOn:
            print('    Telewizor jest: włączony')
            print('    Aktualny kanał:', self.channelList[self.channelIndex])
            if self.isMuted:
                print('    Głośność:', self.volume, '(dźwięk jest wyciszony)')
            else:
                print('    Głośność:', self.volume)
        else:
            print('    TV is: Off')

# Kod testowy - utworzenie dwóch obiektów typu TV.
oTV1 = TV('Sony', 'salon')  # Utworzenie obiektu klasy TV.
oTV2 = TV('Samsung', 'sypialnia')  # Utworzenie innego obiektu klasy TV.

# Włączenie obu telewizorów.
oTV1.power()
oTV2.power()

# Zwiększenie głośności w pierwszym telewizorze.
oTV1.volumeUp()
oTV1.volumeUp()

# Zwiększenie głośności w drugim telewizorze.
oTV2.volumeUp()
oTV2.volumeUp()
oTV2.volumeUp()
oTV2.volumeUp()
oTV2.volumeUp()

# Zmiana kanału w drugim telewizorze, a następnie wyłączenie w nim dźwięku.
oTV2.setChannel(44)
oTV2.mute()

# Wyświetlenie informacji o obu telewizorach.
oTV1.showInfo()
oTV2.showInfo()
