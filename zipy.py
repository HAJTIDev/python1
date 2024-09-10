import zipfile,os
os.chdir(r'C:\users\uczen54\desktop\temp\\')
exampleZip=zipfile.ZipFile('temp.zip')
print(exampleZip.namelist())

spamInfo=exampleZip.getinfo('000.txt')
print(spamInfo.file_size)
print(spamInfo.compress_size)
exampleZip.extractall()
exampleZip.close()