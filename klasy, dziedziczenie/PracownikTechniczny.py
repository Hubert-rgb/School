from pracownik import *
class PracownikTechniczny(Pracownik):
    def __init__(self, imie, nazwisko, staz, nazwa):
        super().__init__(imie, nazwisko, staz)
        self.__nazwa = nazwa
        self.__zakresObowiazkow = []
    def podajZakresObowiazkow(self, obowiazek):
        self.__zakresObowiazkow.append(obowiazek)
    def info(self):
        print(f"Pracownik techniczny: {super().info()}, zakres obowiazkow {self.__zakresObowiazkow}")