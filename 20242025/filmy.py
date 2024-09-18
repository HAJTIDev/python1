class Film:
    def __init__(self):
        self.tytul = ""
        self.liczba_wypozyczen = 0
    def set_tytul(self, tytul):
        self.tytul = tytul
    def get_tytul(self):
        return self.tytul
    def get_liczba(self):
        return self.liczba_wypozyczen
    def inkrementacja(self):
        self.liczba_wypozyczen += 1
film = Film()
print(film.get_tytul())
print(film.get_liczba())
film.set_tytul("Inception")
print(film.get_tytul())
film.inkrementacja()
print(film.get_liczba())