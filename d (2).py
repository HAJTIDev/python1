def czy_przestepny(rok):
    
    if rok % 4 == 0:
        if rok % 100 == 0:
            if rok % 400 == 0:
                return 1
            else:
                return 0
        else:
            return 1
    else:
       return 0

def dni_w_miesiacu(rok, miesiac):

    if czy_przestepny(rok)== 0:
        if miesiac ==2:
            print(28)
        elif miesiac == 5:
            print(31)
        elif miesiac %2 ==0:
            print(30)
        else:
            print(31)
    else:
        if miesiac ==2:
            print(29)
        elif miesiac == 5:
            print(31)
        elif miesiac %2 ==0:
            print(30)
        else:
            print(31)

def dzien_w_roku(rok, miesiac, dzien):
        x=dni_w_miesiacu(miesiac)-dzien
        print(x)


testuj_lata = [1900, 2000, 2016, 1987]
testuj_miesiace = [2, 2, 1, 11]
testuj_wynik = [28, 29, 31, 30]
for i in range(len(testuj_lata)):
	r = testuj_lata[i]
	m = testuj_miesiace[i]
	print(r, m, "-> ", end="")
	wynik = dni_w_miesiacu(r, m)
print(dzien_w_roku(2000, 12, 31))
