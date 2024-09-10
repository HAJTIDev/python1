def fill_value(a,b,c):
##lista= [[c]*b for i in range (a)]
    for i in range(a+1):
        lista=[[c]*b]*i
    print(lista)


fill_value(4,2,0)