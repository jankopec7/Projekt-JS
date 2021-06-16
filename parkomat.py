from decimal import *
from datetime import datetime
from datetime import timedelta
from re import compile
from wyjatki import *


class Moneta():
    monety = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50]

class Pieniadze(Moneta):

    def __init__(self, value):
        super().__init__()

        if value in self.monety:
            self._value = Decimal(str(value))
        else:
            self._value = Decimal('0')
            raise ZlyNominalException

        self._currency = 'ZŁ'

    def get_value(self):
        return self._value

    def get_currency(self):
        return self._currency


class Parkomat():

    def __init__(self):
        self._MoneyList = []
        self._Sum = 0
        self._plate = ''
        self._currentTime = datetime.now()
        self._departureTime = self._currentTime
        self._Quantity = {0.01: 0, 0.02: 0, 0.05: 0, 0.1: 0, 0.2: 0, 0.5: 0, 1: 0, 2: 0, 5: 0}

    def add_coin(self, coin, number):

        try:
            self.check_amount_of_money(number)

        except NiepoprawnaLiczbaMonetException:
            raise NiepoprawnaLiczbaMonetException

        number = int(number)
        grosze = int(100 * coin)
        self._MoneyList.append(Pieniadze(coin))

        for i in range(number):
            for j in range(grosze):
                if self._Sum < 2.0:
                    self.departure(18)
                elif self._Sum < 6.0:
                    self.departure(9)
                else:
                    self.departure(7.2)
        self.money_count(coin, number)

    def money_count(self, value, amount):
        value = Decimal(str(value))

        for i in range(len(self._MoneyList)):
            if value == self._MoneyList[i].get_value():
                if value < Decimal(str(10)):
                    self._Quantity[value] = amount
                    if self._Quantity[value] > 200:
                        raise PrzepelnienieParkomatuException

    def check_amount_of_money(self, amount):
        try:
            int(amount)
        except ValueError:
            raise NiepoprawnaLiczbaMonetException

    def get_license_plate(self, value):
        value = value.rstrip('\n')
        format = compile("^[\w ]*$")

        if format.match(value) is not None and 3 < len(value) < 11 and value:
            value = value.replace(' ', '').upper()
            self._plate = value
        else:
            raise BlednaRejestracjaException

        return self._plate

    def check_date(self):
        pass

    def get_current_time(self):
        return self._currentTime

    def change_current_time(self, rok, miesiac, dzien, godziny, minuty, sekundy):
        d = datetime.strptime(str(rok + ' ' + miesiac + ' ' + dzien), '%Y %m %d')
        zamiana = d.replace(hour=godziny, minute=minuty, second=sekundy)
        self._currentTime = zamiana
        self._departureTime = self._currentTime
        self._Sum = 0
        return self._departureTime

    def get_departure_time(self):
        return self._departureTime


    def departure(self, seconds):

        doKiedy = self._departureTime.weekday()

        if self._departureTime.hour < 8:
            self._departureTime = self._departureTime.replace(hour=8, minute=0, second=0, microsecond=0)

        if self._departureTime.hour >= 20:
            sec = self._departureTime.second
            self._departureTime += timedelta(days=1)
            self._departureTime = self._departureTime.replace(hour=8, minute=0, second=0, microsecond=0)
            if self._Sum != 0:
                self._departureTime += timedelta(seconds=sec)

        if doKiedy == 5:
            sec = self._departureTime.second
            self._departureTime += timedelta(days=2)
            self._departureTime = self._departureTime.replace(hour=8, minute=0, second=0, microsecond=0)
            if self._Sum != 0:
                self._departureTime += timedelta(seconds=sec)
        if doKiedy == 6:
            sec = self._departureTime.second
            self._departureTime += timedelta(days=1)
            self._departureTime = self._departureTime.replace(hour=8, minute=0, second=0, microsecond=0)
            if self._Sum != 0:
                self._departureTime += timedelta(seconds=sec)
        self._Sum += Decimal(0.01)
        self._departureTime += timedelta(seconds=seconds)

    def confirm(self, license):
        self.get_license_plate(license)
        if self._Sum == 0:
            raise NieWrzuconoPieniedzyException
        ticket = 'Rejestracja: ' + self.get_license_plate(license) + \
                 '\n\nData zakupu: ' + str(self.get_current_time()) \
                + '\n\nData wyjazdu: ' + str(self.get_departure_time())

        self._Sum = 0
        self._departureTime = self._currentTime
        return ticket







