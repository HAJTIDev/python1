def szyfr():
    szyfr = ''
    for char in tekst:
        if char==" ":
            szyfr=szyfr+" "
        if char.isdigit():
            szyfr+=char
        if not char.isalpha():
            continue
        if char.islower():
            kod = ord(char) + z
            if kod > ord('z'):
                 kod = kod -26
            szyfr += chr(kod)
        if char.isupper():
            kod = ord(char) + z
            if kod > ord('Z'):
                kod = kod-65
            szyfr += chr(kod)
    print(szyfr)
while True:
    z=int(input("jaki ma być szyfr? "))
    if z>25 or z<1:
        continue
    else:
        break
tekst = str(input("Wpisz wiadomosc: "))
szyfr()
