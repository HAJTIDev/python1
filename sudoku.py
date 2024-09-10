# sudo=[
# "431865927","295743861",
# "876192543",
# "387459216",
# "612387495",
# "549216738",
# "763524189",
# "928671354",
# "154938672"]# TAK
#sudo=["195743862",
# "431865927",
# "876192543",
# "387459216",
# "612387495",
# "549216738",
# "763524189",
# "928671354",
# "254938671"]# NIE
sudo=[]
tak=True
l=0
# poziomo
for i in range (0,9):
    print("Podaj ",i+1," linie: ",end="")
    a=str(input())
    sudo.append(a) 
    for j in sudo[i]:
        j=int(j)
        l+=j
    if l!=45: tak=False
    l=0
# pionowo 
tab=[0,0,0,0,0,0,0,0,0]
for i in range (0,9):
    for l in sudo[i]:
        tab[i]+=int(l)
for i in range (0,9):
    if tab[i]!=45: tak=False
# kwadraty
tab=[0,0,0,0,0,0,0,0,0]
for i in range(0,9):
    l=sudo[i]
    for j in range(0,3):
        if i<=2:
            tab[0]+=int(l[j])
        elif i<=5:
            tab[3]+=int(l[j])
        else:
            tab[6]+=int(l[j])
    for j in range(3,6):
        if i<=2:
            tab[1]+=int(l[j])
        elif i<=5:
            tab[4]+=int(l[j])
        else:
            tab[7]+=int(l[j])
    for j in range(6,9):
        if i<=2: 
            tab[2]+=int(l[j])
        elif i<=5:
            tab[5]+=int(l[j])
        else:
            tab[8]+=int(l[j])
for i in range (0,9): 
    if tab[i]!=45: tak=False     
if tak:print("TAK")
else: print("NIE")