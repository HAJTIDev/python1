import random

liczba_kostek = int(input("Podaj liczbę kostek: "))
if liczba_kostek > 0:
  n = 1000000

  rzuty = [0] * (6 * liczba_kostek - liczba_kostek + 1)
  for i in range(n):
    suma = 0
    for j in range(liczba_kostek):
      rzut = random.randint(1, 6)
      suma += rzut
    rzuty[suma - liczba_kostek] += 1

  for i in range(liczba_kostek, 6 * liczba_kostek + 1):
    print(i, end="-")
    print(rzuty[i-liczba_kostek]," rzutów", end="-")
    print(round(100 * rzuty[i - liczba_kostek] / n,2),"%")
