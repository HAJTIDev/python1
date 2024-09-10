tajny_numer = 777
print(
"""
+================================+
| Witaj w mojej grze, mugolu!    |
| Wprowadź liczbę całkowitą      |
| i zgadnij, jaki numer          |
| wybrałem dla ciebie.           |
| Jaki jest więc sekretny numer? |
+================================+
""")
a=int (input ("podaj liczbe "))

while a!=tajny_numer:
    print("Nie, to nie jest ta liczba, którą wybrałem dla ciebie. Spróbuj ponownie!")
    a=int (input ("podaj liczbe "))
if a==tajny_numer:
    print("Dobra robota! To numer, który wybrałem dla ciebie! Jesteś teraz wolny.")
    exit()