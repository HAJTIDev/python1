import random

def los(tab):
    while len(tab) !=a:
        num = random.randint(1, 50)
        if num not in tab:
            tab.append(num)

def sor(tab,tab2):
    while len(tab2)!=a:
        k=50
        for i in tab:
            if i<k:
                k=i
        tab.remove(k)
        tab2.append(k)
    print(tab2)
def va(tab):
    maks = None
    for number in tab:
        if maks is None or maks < number:
            maks = number
    print("max= ",maks)
    mini = None

    for number in tab:
        if mini is None or number < mini:
            mini = number
    print("min= ",mini)
    
def print_(tab):
    a = len(tab)
    if a % 2 == 0:
        x = tab[int(a / 2) - 1]
        y = tab[int(a / 2)]
        print(str(x) + " and " + str(y))
        print("avg:" + str((x + y) // 2))
    else:
        print("middle= " + str(tab[int(a / 2)]))
    va(tab2)

index = -1
a = int(input("podaj liczbe "))

if a >= 5 and a <= 25:
    tab = []
    tab2=[]
    los(tab)
    sor(tab,tab2)
    print_(tab2)
else:
    print("zła wartość")    