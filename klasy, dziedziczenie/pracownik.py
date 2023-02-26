class Pracownik:
    def __init__(self, imie, nazwisko, staz):
        self._imie = imie
        self.__nazwisko = nazwisko
        self.staz = staz
    def info(self):
        return f"imie: {self._imie}, nazwisko: {self.__nazwisko}"