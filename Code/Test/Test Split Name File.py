import os

os.getcwd()
fln = "D:/Kuliah Online/Pengolahan Citra Digital/PCD Project/Image/After/Resource/01_front_red.jpg"
listFiles = []

# fileFull = open("Code\Data\Name & Value.txt",'w')
# fileValue = open("Code\Data\Value.txt",'w')

listFln = fln.split('/')
fullName = listFln[-1]
nameFile = fullName.split('.')[0]
extensionFile = fullName.split('.')[1]

print(f'\n-----------------\n')
print(f'listFln : {listFln}')
print(f'fullName : {fullName}')
print(f'nameFile : {nameFile}')
print(f'extensionFile : {extensionFile}')
print(f'\n-----------------')


# for file in listFiles:
#     fileFull.write(f'{file}\n')
    

