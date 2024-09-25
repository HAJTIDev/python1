class Osoba:
    liczba_instancji = 0

    def __init__(self, id=0, imie=""):
        self.__id = id
        self.__imie = imie
        Osoba.liczba_instancji += 1

    def kopiuj(self):
        return Osoba(self.__id, self.__imie)

    def przywitaj(self, argument):
        if self.__imie:
            print(f"Cześć {argument}, mam na imię {self.__imie}")
        else:
            print("Brak danych")

osoba1 = Osoba()
osoba2 = Osoba(1, "Jan")
osoba3 = osoba2.kopiuj()

osoba1.przywitaj("Anna") 
osoba2.przywitaj("Anna") 
osoba3.przywitaj("Anna")  

print(f"Liczba instancji klasy Osoba: {Osoba.liczba_instancji}")
