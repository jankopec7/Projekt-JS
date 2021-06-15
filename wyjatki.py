
class ZlyNominalException(Exception):
    def __init__(self, info="Zły nominał"):
        self.info = info
        super().__init__(self.info)

class NiepoprawnaLiczbaMonetException(Exception):
    def __init__(self, info="Niepoprawna liczba monet"):
        self.info = info
        super().__init__(self.info)

class NieznanaWalutaException(Exception):
    def __init__(self, info="Nieznana Waluta"):
        self.info = info
        super().__init__(self.info)

class ZlaDataException(Exception):
    def __init__(self, info="Niepoprawna data"):
        self.info = info
        super().__init__(self.info)

class PrzepelnienieParkomatuException(Exception):
    def __init__(self, info="Parkomat przepełniony, proszę wrzucić inną monetę"):
        self.info = info
        super().__init__(self.info)

class BlednaRejestracjaException(Exception):
    def __init__(self, info="Niepoprawny numer rejestracyjny, wprowadź ponownie"):
        self.info = info
        super().__init__(self.info)

class NieWrzuconoPieniedzyException(Exception):
    def __init__(self, info="Nie wrzucono pieniędzy"):
        self.info = info
        super().__init__(self.info)