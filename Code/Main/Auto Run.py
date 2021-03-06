import os
import cv2 as cv
import numpy as np


def getColorObject(data):
    hueMin = int(data[0])
    satMin = int(data[1])
    valueMin = int(data[2])
    hueMax = int(data[3])
    satMax = int(data[4])
    valueMax = int(data[5])
    
    lower = [hueMin, satMin, valueMin]
    upper = [hueMax, satMax, valueMax]
    return lower, upper

def resizeImg(img, width, height):
    img = cv.resize(img, (width, height), interpolation=cv.INTER_CUBIC)
    return img

os.getcwd()
folderSource = "D:/Kuliah Online/Pengolahan Citra Digital/PCD Project/Image/Revision/Resource/"
folderResult = "D:/Kuliah Online/Pengolahan Citra Digital/PCD Project/Image/Revision/Result/Roi/"
folderBox = "D:/Kuliah Online/Pengolahan Citra Digital/PCD Project/Image/Revision/Result/BB/"

fileFull = open("Code/Data/Name & Value.txt",'r')
fileValue = open("Code/Data/Value (Without Enter).txt",'r')

num = 1 
for values in fileValue: 
    values = values.split(';')
    for fileName, value in zip(os.listdir(folderSource),values):
        # Get Image Path
        sourcePath = folderSource+fileName
        print(f'Name file : {fileName}')

        # Get Color Object
        value = value.split(',')
        lower, upper = getColorObject(value)
        
        # Read Image
        img = cv.imread(sourcePath)
        
        # Get X & Y of Image
        y = int(img.shape[0])
        x = int(img.shape[1])

        # Titik Tengah
        xMid = int(img.shape[1] / 2)
        yMid = int(img.shape[0] / 2)
        # cv.circle(img, (xMid,yMid), 5, (0,255,0), cv.FILLED)

        # Color Detection
        imgHsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
        lowerRange = np.array(lower, dtype=np.uint8)
        upperRange = np.array(upper, dtype=np.uint8)
        imgMask = cv.inRange(imgHsv, lowerRange, upperRange)
        imgResult = cv.bitwise_and(img, img, mask = imgMask)

        # cv.circle(imgResult, (xMid,yMid), 5, (0,0,255), cv.FILLED)


        # Rectangle
        # xRec = xMid + 20
        xRec = int((34/100) * x)
        yRec = yMid
        # yRec = int((52/100) * y)
        # cv.circle(imgResult, (xMid,yRec), 5, (0,255,255), cv.FILLED)

        '''
        Untuk "Image\Test\image 1.jpg"
            Turun 10px  => (xRec,yRec) =  (50%, 52%)
            Turun 30px  => (xRec,yRec) =  (50%, 55%)
            Turun 50px  => (xRec,yRec) =  (50%, 58%)
            Kiri 75px   => (xRec,yRec) =  (40%, 50%)
            Kiri 85px   => (xRec,yRec) =  (39%, 50%)
            Kiri 100px  => (xRec,yRec) =  (37%, 50%)
            Kiri 125px  => (xRec,yRec) =  (34%, 50%)
        '''

        xRec =  xRec - 25
        yRec = yRec - 25
        widthRec, heightRec = 50, 50
        # cv.rectangle(img, (xRec,yRec), (xRec+widthRec, yRec+heightRec), (255,0,0), 2)
        # cv.rectangle(imgResult, (xRec,yRec), (xRec+widthRec, yRec+heightRec), (255,0,0), 2)

        # Roi
        imgCrop = imgResult[yRec:yRec+heightRec, xRec:xRec+widthRec]
        imgCrop = resizeImg(imgCrop, 100, 100)

        # Menyimpan Roi
        if num >= 1 and num < 11:
            cv.imwrite(folderResult + '0' + str(num) + '_roi_' +'front_' + 'red' + '.jpg', imgCrop)
        elif num >= 11 and num < 21:
            print('11-20 \n')
            cv.imwrite(folderResult + str(num) + '_roi_' +'front_' + 'maroon' + '.jpg', imgCrop)
        elif num >= 21 and num < 31:
            cv.imwrite(folderResult + str(num) + '_roi_' +'front_' + "orange" + '.jpg', imgCrop)
        elif num >= 31 and num < 41:
            cv.imwrite(folderResult + str(num) + '_roi_' +'front_' + "yellow" + '.jpg', imgCrop)
        elif num >= 41 and num < 51:
            cv.imwrite(folderResult + str(num) + '_roi_' +'back_' + 'red' + '.jpg', imgCrop)
        elif num >= 51 and num < 61:
            cv.imwrite(folderResult + str(num) + '_roi_' +'back_' + "maroon" + '.jpg', imgCrop)
        elif num >= 61 and num < 71:
            cv.imwrite(folderResult + str(num) + '_roi_' +'back_' + "orange" + '.jpg', imgCrop)
        elif num >= 71 and num < 81:
            cv.imwrite(folderResult + str(num) + '_roi_' +'back_' "yellow" + '.jpg', imgCrop)
        # cv.imwrite(folderResult + newNameRoi + '.jpg', imgCrop)
        # print(f'Roi {newNameRoi}.jpg BERHASIL!')

        # Menyimpan Citra + Boundingbox
        cv.rectangle(img, (xRec,yRec), (xRec+widthRec, yRec+heightRec), (255,0,0), 2)
        if num >= 1 and num < 11:
            cv.imwrite(folderBox + '0' + str(num) + '_bb_' +'front_' + 'red' + '.jpg', img)
        elif num >= 11 and num < 21:
            print('11-20 \n')
            cv.imwrite(folderBox + str(num) + '_bb_' +'front_' + 'maroon' + '.jpg', img)
        elif num >= 21 and num < 31:
            print('21-30 \n')
            cv.imwrite(folderBox + str(num) + '_bb_' +'front_' + "orange" + '.jpg', img)
        elif num >= 31 and num < 41:
            cv.imwrite(folderBox + str(num) + '_bb_' +'front_' + "yellow" + '.jpg', img)
        elif num >= 41 and num < 51:
            cv.imwrite(folderBox + str(num) + '_bb_' +'back_' + 'red' + '.jpg', img)
        elif num >= 51 and num < 61:
            cv.imwrite(folderBox + str(num) + '_bb_' +'back_' + "maroon" + '.jpg', img)
        elif num >= 61 and num < 71:
            cv.imwrite(folderBox + str(num) + '_bb_' +'back_' + "orange" + '.jpg', img)
        elif num >= 71 and num < 81:
            cv.imwrite(folderBox + str(num) + '_bb_' +'back_' "yellow" + '.jpg', img)
        
        # print(f'Citra + Boundingbox {newNameBb}.jpg BERHASIL!')

        print(f'--------------------\n')
        num += 1
            
            

                        
            
    
    
    
    


