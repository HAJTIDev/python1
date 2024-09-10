def readint(prompt, min, max):
    if(prompt >=min and prompt<=max):
        print("mieści się w przedziale ")
        return True
    else:
        print("Błąd: podana liczba jest spoza dozwolonego zakresu ",min," ",max)
        return False
while True:
    try: 
        v=int(input("Podaj liczbe od -10 do 10: "))
        if readint(v,-10,10):
            print("Liczba to:", v)  
            break
    except:
        print("Błąd: wprowadzono nieprawidłową liczbę")

