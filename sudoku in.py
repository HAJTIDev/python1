global N
def SprawdzPoprawnosc(tablica):
  liczniki = [0 for x in range(27)]
  for x in range(N):
    for y in range(N):
      wartosc = tablica[x][y]
      if wartosc < 1 or wartosc > 9:
        return False
      liczniki[x] += wartosc
      liczniki[y + 9] += wartosc
      liczniki[(x // 3 + (y // 3) * 3) + 18] += wartosc
  for licznik in liczniki:
    if licznik != 45:
      return False
  return True

print("Podaj wartości tablicy:")
tablica = []
for i in range(0, N):
	tab = [int(x) for x in input().split()]
tablica.append(tab)
wynik = SprawdzPoprawnosc(tablica)
print("Sudoku " + ("" if wynik else "nie") + "poprawnie rozwiazane")