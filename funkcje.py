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


testuj_lata = [1900, 2000, 2016, 1987]
testuj_miesiace = [2, 2, 1, 11]
testuj_wynik = [28, 29, 31, 30]
for i in range(len(testuj_lata)):
	r = testuj_lata[i]
	m = testuj_miesiace[i]
	print(r, m, "-> ", end="")