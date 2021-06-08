
class ZlyNominalException(Exception):
    def __init__(self, info):
        super().__init__(info)


class NiepoprawnaLiczbaMonetException(Exception):
    def __init__(self, info):
        super().__init__(info)

class NieznanaWalutaException(Exception):
    def __init__(self, info):
        super().__init__(info)