plik=str(input("podaj nazwe pliku "))
slow={}
o=open(plik+'.txt')
zapis=open(plik+'2'+'.txt'+".hist",'wt')
for linia in o:
    for litera in linia:
        litera=litera.lower()
        if litera in slow:
            slow[litera]+=1
        else:
            slow[litera]=1
sor=(sorted(slow.items(), key=lambda x: x[1], reverse=True))      
sor=dict(sor)
for key,val in  sorted(sor.items()):
    print(key," -> ",val)
    val=str(val)
    s=(key," -> ",val,"  ")
    for c in s:
        zapis.write(c)
o.close()
zapis.close()

