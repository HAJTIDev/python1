def binary(i):
    bin= ''
    while(i > 0):
        d = i % 2
        bin += str(d)
        i = i // 2
    bin = bin[::-1]
    return bin

def XOR(p):
    val = int(p)
    half = val/2
    temp = binary(half)
    
    if len(temp) < len(p):
        dif = len(p)-len(temp)
        temp[::-1]
        for i in range(dif):
            temp+="0"
        temp[::-1]
    x=""
    for i in range(len(p)):
        if p[i] == temp[i]:
            x+="0"
        else:
            x+="1"
    x[::-1]
    end = int(x,2)
    return end

with open("bin_przyklad.txt") as f:
    f=f.readlines()
    l=0
    for i in f:
        t=str(i)
        k=0
        for j in range (len(t)-1):
            if t[j]!=str(t[j+1]):
                k+=1
        if k<=2:
            l+=1
    with open("wynik_2,2.txt","w") as odp:
        odp.write("zad 2.2"+" "+str(l))

    maxnum=0
    for i in f:
        num=int(i)
        if num>maxnum:
            maxnum=num
    with open("wynik_2,3.txt","w") as odp:
        odp.write("zad 2.3 "+" "+str(maxnum))
        
    with open("wynik_2,5.txt","w") as odp:
        for i in f:
            odp.write( str(binary(XOR(i)))+'\n')
    
    
    



    