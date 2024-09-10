def clean_hashtags(inp,out,leng):
    with open(inp, 'rt') as file:
        c=file.read()
        hash=c.split()
        j=0
        tab=[]
        for i in hash:
            if len(i)-1<=leng:
                if i not in tab:
                    tab.append(i)
                    j+=1
        tab=sorted(tab)
    with open (out,"w") as file2:
        k=1
        for j in tab:
            file2.write(str(k)+". "+j+'\n')
            k+=1

clean_hashtags("hashtags.txt","clean.txt",5)