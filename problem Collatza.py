c0 = int(input("podaj liczbe nie ujemną i nie zerowa "))
i = 0
while c0!=1:
    if c0 % 2 == 0 :
        c0 = c0/2
        i+=1
        print(c0)
    elif c0 % 2 != 0 :
        c0=3 * c0 + 1
        i+=1
        print(c0)
print("tyle razy trzeba bylo zmienic", i)
