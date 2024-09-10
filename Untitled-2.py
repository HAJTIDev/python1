liczby_z_kapelusza = [1, 2, 3, 4, 5]  # Istniejąca lista liczb ukrytych w kapeluszu.

# Krok 1: Napisz wiersz kodu, który prosi użytkownika
# o zastąpienie środkowego numeru liczbą całkowitą wprowadzoną przez użytkownika.
liczba=int(input("podaj liczbę "))
liczby_z_kapelusza[2]=liczba
# Krok 2: Napisz tutaj wiersz kodu, który usuwa ostatni element z listy.
del liczby_z_kapelusza[-1]
# Krok 3: Napisz tutaj wiersz kodu, który wypisuje długość istniejącej listy.
print(liczby_z_kapelusza)  # Wyświetlanie zawartości listy.
print(len (liczby_z_kapelusza))
