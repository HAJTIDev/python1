def top_n(items,n):
    j=0
    sortedf=sorted(items)

    for i in range (n):
        print(sortedf[-1+j])
        j=j-1


lista=[4,5,6,7,3,2,1,11,123,75]
top_n(lista,4)