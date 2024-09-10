data = { }
nazwa_pliku = input("Wpisz nazwe pliku danych ucznia:")
try:
    f = open(nazwa_pliku, "rt")
    lines = f.readlines()
    f.close()
    for i in range(len(lines)):
        line = lines[i]
        kolumny = line.split()
        student = kolumny[0] + ' ' + kolumny[1]
        points = float(kolumny[2])
        try:
            data[student] += points
        except KeyError:
            data[student] = points
    for student in sorted(data.keys()):
        print(student,'\t', data[student])

except IOError as e:
    print("Blad I/O: ")

