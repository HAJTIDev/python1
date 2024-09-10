from pathlib import Path

p=Path(r'C:\users\uczen54\desktop\temp\\')

list_of_text_file=list(p.glob('*txt'))
#print(list_of_text_file)
i=0
for path in list_of_text_file:
    print(path.stat().st_size)
    if path.stat().st_size > 1024*1024:
        continue
    zeros=str(i).zfill(3)
    print(zeros)
    i+=1
    target=Path('\\'.join(str(path).split('\\')[:-2])+'\\temp2\\'+zeros+'.txt')
    print(target,"\n")
    path.rename(target)