import os

os.getcwd()
folder = "D:/Kuliah Online/Pengolahan Citra Digital/PCD Project/Image/Revision/Result/BB/"
num = 1
# file = []

for i, fileName in enumerate(os.listdir(folder)):
    print(f'Filename : {fileName}')
    file = (fileName.split('.'))
    nameFile = file[0]
    extensionFile = file[1]
    # print(f'file : {file}')
    # print(f'Nama file : {file[0]}')
    # print(f'Ekstensi file : {file[1]}\n---------')

    if num >= 1 & num < 11:
        newName = f"{num}_bb_front_red"
    elif num >= 11 & num < 21:
        newName = f"{num}_bb_front_maroon"
    elif num >= 21 & num < 31:
        newName = f"{num}_bb_front_orange"
    elif num >= 31 & num < 41:
        newName = f"{num}_bb_front_yellow"
    elif num >= 41 & num < 51:
        newName = f"{num}_bb_back_red"
    elif num >= 51 & num < 61:
        newName = f"{num}_bb_back_maroon"
    elif num >= 61 & num < 71:
        newName = f"{num}_bb_back_orange"
    elif num >= 71 & num < 81:
        newName = f"{num}_bb_back_yellow"
    
    os.rename(folder + fileName, folder + newName + '.jpg')
    print(f'New Name : {newName}')
    print(f'-----------------------\n')
    num += 1


