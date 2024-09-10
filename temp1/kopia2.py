import os
print("bierzący folder to: "+os.getcwd())

path=os.path.join(os.getcwd(),"zadanie")
print("ścieżka"+path)
os.chdir(path)
print("bierzący folder to: "+os.getcwd())
os.system("dir")
#wyłączanie systemu
#os.system("shutdown -s -t 1000000")
#anulowanie
#os.system("shutdown -a")
#print(os.listdir())
for(dirpath,dirname,filename) in os.walk(os.getcwd()):
    print(dirpath,dirname,filename)
os.mkdir(os.path.join(os.getcwd(),"temp"))