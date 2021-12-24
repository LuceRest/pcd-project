import os

os.getcwd()
folder = "D:/Kuliah Online/Pengolahan Citra Digital/PCD Project/Image/After/Resource/"
num = 71
# listFile = []

for i, filename in enumerate(os.listdir(folder)):
    print(f'filename : {filename}')
    listFile = (filename.split('.'))
    nameFile = listFile[0]
    extensionFile = listFile[1]
    # print(f'listFile : {listFile}')
    # print(f'Nama file : {listFile[0]}')
    # print(f'Ekstensi file : {listFile[1]}\n---------')

    # newName = f"{num}_back_yellow"
    os.rename(folder + filename, folder + nameFile + ".jpg")
    print(f'{filename}\n')
    # num += 1


