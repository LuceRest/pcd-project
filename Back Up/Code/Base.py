import cv2 as cv
import numpy as np


imgPath="Image\Test\image 1.jpg"
# imgPath="Image\image (6).png"
# imgPath= "Image\image 1.jpg"

img = cv.imread(imgPath)

y = int(img.shape[0])
x = int(img.shape[1])

# Titik Tengah
xMid = int(img.shape[1] / 2)
yMid = int(img.shape[0] / 2)

cv.circle(img, (xMid,yMid), 5, (0,255,0), cv.FILLED)

print(f'X \t: {x}\n')
print(f'Y \t: {y}\n')
print(f'X Mid \t: {xMid}\n')
print(f'Y Mid \t: {yMid}\n')
print(f'shape \t: {img.shape}\n')


# Color Detection
imgHsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
lowerRange = np.array([26, 65, 149], dtype=np.uint8)
upperRange = np.array([33, 255, 255], dtype=np.uint8)
imgMask = cv.inRange(imgHsv, lowerRange, upperRange)
imgResult = cv.bitwise_and(img, img, mask = imgMask)

cv.circle(imgResult, (xMid,yMid), 5, (0,0,255), cv.FILLED)


# Rectangle Bawah

# xRec = xMid + 20
xRec = xMid
# yRec = yMid + 30
persen = int((55/100) * y)
yRec = persen
print(f'xRec \t: {xRec}\n')      # 50%
print(f'yRec \t: {yRec}\n')      # 58%
print(f'persen yRec \t: {persen}\n')
cv.circle(imgResult, (xMid,yRec), 5, (0,255,255), cv.FILLED)

'''
Untuk "Image\Test\image 1.jpg"
Turun 30px => (xRec,yRec) =  (50%, 55%)
Turun 50px => (xRec,yRec) =  (50%, 58%)
'''

xRec =  xMid - 25
yRec = yRec - 25
widthRec, heightRec = 50, 50
cv.rectangle(img, (xRec,yRec), (xRec+widthRec, yRec+heightRec), (255,0,0), 2)
cv.rectangle(imgResult, (xRec,yRec), (xRec+widthRec, yRec+heightRec), (255,0,0), 2)

# ------------------------------------------------------

# Rectangle Kanan

# xRec = xMid + 20
# xRec = xMid + 50
# yRec = yMid
# print(f'xRec\t: {xRec}\n')      # 50%
# print(f'yRec\t: {yRec}\n')      # 58%
# cv.circle(imgResult, (xMid,yRec), 5, (0,255,255), cv.FILLED)

# xRec =  xMid - 25
# yRec = yRec - 25
# widthRec, heightRec = 50, 50
# cv.rectangle(imgResult, (xRec,yRec), (xRec+widthRec, yRec+heightRec), (255,0,0), 2)


# ROI

imgCrop = img[yRec:yRec+heightRec, xRec:xRec+widthRec]
# cv.imwrite('Image no 16', imgCrop)

cv.imshow("Img Original",img)
cv.imshow('ImgResult', imgResult)
cv.imshow('imgCrop', imgCrop)

cv.waitKey(0)


