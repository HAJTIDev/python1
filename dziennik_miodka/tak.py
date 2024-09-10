dane = {}
plik = input(" Wpisz nazwe pliku danych ucznia: ")

o = open(plik, "rt")
lines = o.readlines()
o.close()

for i in range(len(lines)):
    line = lines[i]
    kol = line.split()
    student = kol[0] + ' ' + kol[1]
    points = float(kol[2])
    if student in dane:
        dane[student] += points
    else:
        dane[student] = points

for student in sorted(dane.keys()):
        print(student,"-->", dane[student])
