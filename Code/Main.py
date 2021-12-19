import cv2 as cv
import numpy as np


imgPath="Resource\Image\Kuning-Back\image 7.jpg"

img = cv.imread(imgPath)

y = int(img.shape[0])
x = int(img.shape[1])

# Titik Tengah
xMid = int(img.shape[1] / 2)
yMid = int(img.shape[0] / 2)

cv.circle(img, (xMid,yMid), 5, (0,255,0), cv.FILLED)

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


# Rectangle

# xRec = xMid + 20
yRec = yMid + 50
cv.circle(imgResult, (xMid,yRec), 5, (0,255,255), cv.FILLED)

xRec =  xMid - 25
yRec = yRec - 25
cv.rectangle(imgResult, (xRec,yRec), (xRec+50, yRec+50), (255,0,0), 2)


# ROI

imgCrop = imgResult[xRec:xRec+50, yRec:yRec+50]


cv.imshow("Img Original",img)
cv.imshow('ImgResult', imgResult)
cv.imshow('imgCrop', imgCrop)

cv.waitKey(0)


