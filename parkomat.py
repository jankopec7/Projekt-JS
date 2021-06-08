from decimal import *
from datetime import *
from tkinter import *
from tkinter import ttk
import time
import datetime


dzienTygodnia = ("Poniedziałek", "Wtorek", "Środa", "Czwartek", "Piątek", "Sobota", "Niedziela")


class ZlyNominalException(Exception):
    def __init__(self, info):
        super().__init__(info)


class ListaMonetException(Exception):
    def __init__(self, info):
        self.message = info


class NieznanaWalutaException(Exception):
    def __init__(self, info):
        super().__init__(info)


class Moneta:
    def __init__(self, value, currency):

        if value in {0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50}:
            self._value = Decimal(str(value)).quantize(Decimal('.01'), rounding=ROUND_DOWN)
        else:
            raise ZlyNominalException('Zły nominał')

        if currency in {'PLN'}:
            self._currency = currency
        else:
            raise NieznanaWalutaException('Nieznana waluta')

    def getValue(self):
        return self._value

    def getCurrency(self):
        return self._currency


class PrzechowywaczMonet():

    def __init__(self, currency):
        if currency not in ['PLN']:
            print('Nieznana moneta')
        else:
            self.__coins = []
            self.__currency = currency

    def add_coin(self, coin):
        if isinstance(coin, Moneta):
            if coin.get_currency() == self.__currency:
                if coin.get_value() != 0:
                    self.__coins.append(coin)
            else:
                print('Zła waluta')
        else:
            print('Przesłany obiekt nie jest monetą')

    def get_sum(self):
        suma = 0
        for i in self.__coins:
            suma += i.get_value()
        return suma

    def get_coin(self, coin):
        for i in self.__coins:
            if i.get_currency() == coin.get_currency():
                if i.get_value() == coin.get_value():
                    self.__coins.remove(coin)
                    return i
        return Moneta(0, 'PLN')


class Parkomat():
    def __init__(self):
        self.licz = dict.fromkeys(list(map(Decimal, ['0.01', '0.02', '0.05', \
                                                            '0.1', '0.2', '0.5', '1', '2', '5'])), 0)
        self._wszystkiemonety = 0

    def add_coin(self, coin):
        if not isinstance(coin, Moneta):
            raise ZlyNominalException('Zły nominał')

        def add_coin(self, coin):
            if isinstance(coin, Moneta):
                if coin.get_currency() == self.__currency:
                    if coin.get_value() != 0:
                        self.__coins.append(coin)
                else:
                    print('Zła waluta')
            else:
                print('Przesłany obiekt nie jest monetą')
        if coin.getValue() not in (10, 20, 50):

            if self.licz[coin.getValue()] == 4:
                print("Przepełnienie parkomatu")
                return
            else:
                self.licz[coin.get_val()] += 1
        self._wszystkiemonety += coin.get_val()
        print("Dodano", coin.get_val(), "kredytu")
