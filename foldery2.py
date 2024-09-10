import os
import shutil
path=os.getcwd()
print(os.path.isfile(os.path.join(path,"foldery.py")))
#kopiowanie
shutil.copyfile(os.path.join(path,"foldery.py"),
                os.path.join(path,"temp1","kopia1.py"))
shutil.copy2(os.path.join(path,"foldery.py"),
                os.path.join(path,"temp1","kopia2.py"))
#usuwanie
os.remove(os.path.join(path,"temp1","kopia1.py"))
#usuwanie pustych folderów
os.rmdir(os.path.join(path,"temp"))
#usuwanie wszystkiego w środku i folderu
shutil.rmtree(os.path.join(path,"temp"))