from pracownik import *


class Lekarz(Pracownik):
    def __init__(self, imie, nazwisko, staz, specjalizacja):
        super().__init__(imie, nazwisko, staz)
        self.specjalizacja = specjalizacja

    def info(self):
        print(f"Lekarz: {super().info()}, Specjalizacja: {self.specjalizacja}")
