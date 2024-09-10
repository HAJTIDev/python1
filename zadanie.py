import random1

def generuj_tablice():
    return [random.randint(1, 100) for _ in range(50)]

def przeszukaj_tablice(tablica, x):
    tablica.append(x)
    for i, element in enumerate(tablica):
        if element == x:
            if i == len(tablica) - 1:
                return "Element nie został znaleziony w tablicy."
            else:
                return f"Element znaleziony na pozycji {i}."
    return "Element nie został znaleziony w tablicy."

def main():
    x = int(input("Podaj liczbę do wyszukania: "))
    tablica = generuj_tablice()
    wynik = przeszukaj_tablice(tablica, x)
    print(f"Tablica: {', '.join(map(str, tablica[:-1]))}")
    print(wynik)

if __name__ == "__main__":
    main()