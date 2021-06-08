from decimal import *
from datetime import *
import time
import datetime
from wyjatki import *


class Moneta():
    monety = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50]

class Pieniadze(Moneta):

    def __init__(self, value):
        super().__init__()

        if value in self.monety:
            self._value = Decimal(str(value)).quantize(Decimal('.01'), rounding=ROUND_DOWN)
        else:
            self._value = Decimal('0')
            raise ZlyNominalException('Zły nominał')

        self._currency = 'PLN'

    def getValue(self):
        return self._value

    def getCurrency(self):
        return self._currency


class Parkomat():

    def __init__(self):

        self._listaMonet = []
        self._suma = 0
        self._plate = ''

    def addCoin(self, coin, number):

        try:
            self.checkNumberOfCoins(number)

        except NiepoprawnaLiczbaMonetException:
            raise NiepoprawnaLiczbaMonetException('Niepoprawna liczba monet')

        number = int(number)
        grosze = int(100 * coin)
        money = Pieniadze(coin)
        self._listaMonet.append(money)

        for i in range(number):
            for j in range(grosze):
                if self._suma < 2.0:
                    self.ileZaGrosza(18)
                elif self._suma < 6.0:
                    self.ileZaGrosza(9)
                else:
                    self.ileZaGrosza(7.2)
        self.zliczanieMonet(coin, number)

    def moneyCount(self, value, amount):
        value = Decimal(str(value))

        for i in range(len(self._listaMonet)):
            if value == self._listaMonet[i].getValue():
                if value < Decimal(str(10)):
                    self._iloscMonet[value] = amount

    def getLicensePlate(self, value):
        value = value.rstrip('\n')
        format = compile("^[\w\ ]*$")
        if format.match(value) is not None and 3 < len(
                value) < 11 and value:
            value = value.replace(' ', '').upper()
            self._plate = value
        return self._plate

