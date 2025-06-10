# Klasa DisplayMoney - wyświetlenie liczby jako wartości walutowej.
#
# Przykład użycia dziedziczenia.

import pygwidgets

BLACK = (0, 0, 0)

# Klasa DisplayMoney dziedziczy po klasie DisplayText.
class DisplayMoney(pygwidgets.DisplayText):

    def __init__(self, window, loc, value=None,
                 fontName=None, fontSize=24, width=150, height=None,
                 textColor=BLACK, backgroundColor=None,
                 justified='left', nickname=None, currencySymbol='$',
                 currencySymbolOnLeft=True, showCents=True):

        self.currencySymbol = currencySymbol
        self.currencySymbolOnLeft = currencySymbolOnLeft
        self.showCents = showCents
        if value is None:
            value = 0.00

        # Wywołanie metody __init__() klasy bazowej.
        super().__init__(window, loc, value, fontName, fontSize,
                            width, height, textColor, backgroundColor,
                            justified, nickname)

    def setValue(self, money):
        if money == '':
            money = 0.00

        money = float(money)

        if self.showCents:
            money = '{:,.2f}'.format(money)
        else:
            money = '{:,.0f}'.format(money)

        if self.currencySymbolOnLeft:
            theText = self.currencySymbol + money
        else:
            theText = money + self.currencySymbol

        # Wywołanie metody setValue() w klasie bazowej.
        super().setValue(theText)
