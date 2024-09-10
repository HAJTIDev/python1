import zipfile,os

def backup(folder):
    folder=os.path.abspath(folder)
    print("kom1 "+folder)
    numer=1
    while True:
        zipFilename=os.path.basename(folder)+'_'+str(numer)+'.zip'
        print("kom2 "+os.path.basename(folder))
        print("kom3 "+zipFilename)
        if not os.path.exists(zipFilename):
            break
        numer+=1
    print(f"tworzenie archiwum {zipFilename}...")
    backupZip=zipfile.ZipFile(zipFilename,'w')
    for foldername,subfolder,filenames in os.walk(folder):
        # print(f"dodawanie plików w {zipFilename}...")
         backupZip.write(foldername)
         for filename in filenames:
            backupZip.write(os.path.join(foldername,filename))
    backupZip.close()
    print("gotowe")

os.chdir(r'C:\users\uczen54\desktop\\')
backup(r'C:\users\uczen54\desktop\temp\\')