import random

class Bombelkowe:
    def __init__(self, tab):
        self.tab = tab

    def sortowanie(self):
        for i in range(len(self.tab)):
            print(self.tab)
            for j in range(len(self.tab)-1):
                if self.tab[j] > self.tab[j+1]:
                    self.tab[j], self.tab[j+1] = self.tab[j+1], self.tab[j]

tablica = [random.randint(1, 100) for _ in range(100)]

b = Bombelkowe(tablica)
b.sortowanie()
print("Posortowane", b.tab)