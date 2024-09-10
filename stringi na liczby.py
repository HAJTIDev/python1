text=input()
sign='+'
result=0
dod=""
uj=""
k=0
for i in text:
    if i in '-+':
        if i in '+-':
            if sign == '+':
                k=int(k)
                result += k
                if k==0:
                    dod+=str(k)+"  "
                else:
                    dod += str(k) +"  "
            else:
                k=int(k)
                result -= k
                if k==0:
                    dod+=str(k)+"  "
                else:
                    uj += "-" + str(k)+"  "
            k = ""
            sign = i
    else:
        k+=i
if sign == '+':
    k=int(k)
    result += k
    if k==0:
        dod+=str(k)+"  "
    else:
        dod += str(k) +"  "
else:
    k=int(k)
    result -= k
    if k==0:
        dod+=str(k)+"  "
    else:
        uj += "-" + str(k)+"  "
    
print("dodatnie: ",dod)
print("ujemne: ",uj)
print(result)