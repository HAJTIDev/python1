def count_none():
    lista=[2,3,None,2,3,None,2,3,None,2,3,None]
    licznik=0
    for i in lista:
        if not i:
            licznik+=1
    print(licznik)

count_none()