from os import path
from tkinter import messagebox
import os

def writeData(data, pathFile): 
    try:   
        fileTxt = open(pathFile,'a')

        fileTxt.write(f'{data}\n')
        # fileValue.write(f'{data}\n')
        print(f'{data} BERHASIL\n')
        # print(f'{data}\n')
        # messagebox.showinfo('Notification', 'Write data successfully!')
    except IOError:
        messagebox.showerror('Error', 'Write data failed!')

os.getcwd()

folderRead = "D:/Kuliah Online/Pengolahan Citra Digital/PCD Project/Data/dataset_80v20/test/Orange/"
# num = 1
# file = []

for i, fileName in enumerate(os.listdir(folderRead)):
    print(f'Filename : {fileName}')
    file = (fileName.split('.'))
    nameFile = file[0]
    extensionFile = file[1]

    pathFile = 'Code\Data\Data Uji 80v20.txt'
    writeData(fileName, pathFile)
    
