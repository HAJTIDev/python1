def czy_przestepny(rok):
    x=0
    if rok % 4 == 0:
        if rok % 100 ==0:
            if rok % 400 == 0:
                x+=1
            else:
                x=0
        else:
            x+=1
    else:
        x=0

def dni_w_miesiacu(rok, miesiac):
    if czy_przestepny(rok)== 0:
        if miesiac ==2:
            print(29)
        elif miesiac == 5:
            print(31)
        elif miesiac %2 ==0:
            print(30)
        else:
            print(31)


testuj_lata = [1900, 2000, 2016, 1987]
testuj_miesiace = [2, 2, 1, 11]
testuj_wynik = [28, 29, 31, 30]
for i in range(len(testuj_lata)):
	r = testuj_lata[i]
	m = testuj_miesiace[i]
	print(r, m, "-> ", end="")
	wynik = dni_w_miesiacu(r, m)
	if wynik == testuj_wynik[i]:
		print("OK")
	else:
		print("Nie powiodło się")