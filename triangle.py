import math
f = open('testy.txt','r')
maxObw = 0
maxObwP = []
minObw = 100
minObwP = []
def pitagoras(A,B):
    a = int(A[0]) - int(B[0])
    b = int(A[1]) - int(B[1])
    if a<0:
        a = a*-1
    if b<0:
        b = b*-1
    a = a*a
    b = b*b
    c = a+b
    c = math.sqrt(c)
    return c
for x in range(31):
    test = 0
    punktA = []
    punktB = []
    punktC = []
    a = f.readline()
    a = a.split(' ')
    del a[len(a)-1]
    punktA.append(int(a[0]))
    punktA.append(int(a[1]))
    punktB.append(int(a[2]))
    punktB.append(int(a[3]))
    punktC.append(int(a[4]))
    punktC.append(int(a[5]))
    AB = round(pitagoras(punktA,punktB),2)
    AC = round(pitagoras(punktA,punktC),2)
    BC = round(pitagoras(punktB,punktC),2)
    obw = AB + AC + BC
    obw = round(obw,2)
    SlopeAB = (punktA[0]-punktA[1])/(punktB[0]-punktB[1])
    SlopeAC = (punktA[0]-punktA[1])/(punktC[0]-punktC[1])
    SlopeCB = (punktC[0]-punktC[1])/(punktB[0]-punktB[1])
    if SlopeAB == SlopeAC:
        test+=1
    if SlopeAB == SlopeCB:
        test+=1
    if SlopeCB == SlopeCB:
        test+=1
    if test>2:
        print('Nie da się zbudować z tych punktów trójkąta bo leża na tej samej prostej')
    else:
        if obw>maxObw:
            maxObw = obw
            maxObwP = punktA+punktB+punktC
        if obw<minObw:
            minObw = obw
            minObwP = punktA+punktB+punktC
        print(obw)
print('Maksymalny obwód to ',maxObw,' a punkty to ',maxObwP)
print('Maksymalny obwód to ',minObw,' a punkty to ',minObwP)
f.close()