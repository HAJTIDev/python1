beatles=[]
print("krok 1:", beatles)

beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("krok 2:", beatles)

for members in range(2):
  beatles.append(input("nowczy czlonek: "))
print("krok 3:", beatles)

del beatles[-1]
del beatles[-1]
print("krok 4:", beatles)

beatles.insert(0,"Ringo Starr")
print("krok 5:", beatles)

print("The Fab", len(beatles))