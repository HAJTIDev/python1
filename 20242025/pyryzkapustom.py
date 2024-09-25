import random

def pobierz_liczbe_kostek():
    while True:
        try:
            liczba_kostek = int(input("Podaj liczbę kostek do rzucenia (3-10): "))
            if 3 <= liczba_kostek <= 10:
                return liczba_kostek
        except ValueError:
            pass

def rzuc_kostkami(liczba_kostek):
    rzuty_kostkami = [random.randint(1, 6) for _ in range(liczba_kostek)]
    return rzuty_kostkami

def wyswietl_rzuty(rzuty_kostkami):
    for i, rzut in enumerate(rzuty_kostkami, start=1):
        print(f"Kostka {i}: {rzut}")

def oblicz_punkty(rzuty_kostkami):
    pogrupowane_rzuty = [x for x in rzuty_kostkami if rzuty_kostkami.count(x) > 1]
    return sum(pogrupowane_rzuty)

def czy_zagrac_ponownie():
    odpowiedz = input("Czy chcesz zagrać ponownie? (t/n): ").lower()
    return odpowiedz == 't'

def main():
    zagraj_ponownie = True
    while zagraj_ponownie:
        liczba_kostek = pobierz_liczbe_kostek()
        rzuty_kostkami = rzuc_kostkami(liczba_kostek)
        wyswietl_rzuty(rzuty_kostkami)
        punkty = oblicz_punkty(rzuty_kostkami)
        print(f"Punkty: {punkty}")
        zagraj_ponownie = czy_zagrac_ponownie()

if __name__ == "__main__":
    main()
