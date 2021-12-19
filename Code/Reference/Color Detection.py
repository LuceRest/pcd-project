import cv2
import numpy as np


frameWidth = 1024
frameHeight = 768

# cap = cv2.VideoCapture(0)
# cap.set(3, frameWidth)            # Resize lebar dari frame
# cap.set(4, frameHeight)           # Resize tinggi dari frame

def empty(a):
    pass

cv2.namedWindow("HSV")
cv2.resizeWindow("HSV", 350, 250)
cv2.createTrackbar("HUE Min", "HSV", 0, 179, empty)
cv2.createTrackbar("HUE Max", "HSV", 179, 179, empty)
cv2.createTrackbar("SAT Min", "HSV", 0, 255, empty)
cv2.createTrackbar("SAT Max", "HSV", 255, 255, empty)
cv2.createTrackbar("VALUE Min", "HSV", 0, 255, empty)
cv2.createTrackbar("VALUE Max", "HSV", 255, 255, empty)

while True:
    # sucess, img = cap.read()
    imgPath="Resource\Image\Kuning-Back\image 7.jpg"
    
    img = cv2.imread(imgPath)

    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos("HUE Min", "HSV")
    h_max = cv2.getTrackbarPos("HUE Max", "HSV")
    s_min = cv2.getTrackbarPos("SAT Min", "HSV")
    s_max = cv2.getTrackbarPos("SAT Max", "HSV")
    v_min = cv2.getTrackbarPos("VALUE Min", "HSV")
    v_max = cv2.getTrackbarPos("VALUE Max", "HSV")

    # print(h_min)

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV, lower, upper)
    result = cv2.bitwise_and(img, img, mask = mask)
    
    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    hStack = np.hstack([img, mask, result])

    cv2.imshow("Original", img)
    cv2.imshow("HSV Color Space", imgHSV)
    cv2.imshow("Mask", mask)
    cv2.imshow("Result", result)
    
    # cv2.imshow("Horizontal Stacking", hStack)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break   

# cap.release()
cv2.destroyAllWindows()



'''
    NB :
        - cv2.COLOR_BGR2HSV	    ~> Berfungsi untuk mengubah warna gambar menjadi format HSV.

        - cv2.namedWindow()		~> Berfungsi untuk membuat suatu window yg dapat digunakan sebagai tempat untuk gambar dan trackbar.
        - cv2.namedWindow("<nama window>")

        - cv2.resizeWindow()	~> Berfungsi untuk meresize ukuran suatu window.
        - cv2.resizeWindow("<nama window yg ingin diresize>", <width / lebar>, <height / tinggi>)

        - cv2.createTrackbar()	~> Berfungsi untuk membuat suatu trackbar / slider pada window yg telah dibuat.
        - cv2.createTrackbar("<nama trackbar>", "<nama window yg telah dibuat>", <nilai slider>, <nilai maksimal slider>, <function yg akan dijalankan>)

        - cv2.getTrakcbarPos()	~> Berfungsi untuk mengambil nilai terkini dari suatu trackbar / untuk mengembalikan posisi saat terkini pada suatu trackbar.
        - cv2.getTrackbarPos("<nama trackbar>", "<nama window pada trackbar>")

        - cv2.inRange()		    ~> Berfungsi untuk memeriksa apakah suatu nilai terletak di antara dua array lainnya.
        - cv2.inRange(<sumber gambar yg telah dibaca / input array>, <array batas bawah>, <array batas atas>)

        - cv2.bitwise_and()	    ~> Berfungsi untuk menghitung konjungsi bit-wise per element dari dua array atau array dan skalar.
        - cv2.bitwise_and(<sumber gambar 1 / input array 1>, <sumber gambar 2 / input array>, mask = <nilai dari element yg akan diubah>)

        - np.hstack()		    ~> Berfungsi untuk menumpuk urutan array input secara horizontal untuk membuat array tunggal.
        - np.hstack(<input array>) 
        - np.hstack()		    ~> Berfungsi juga untuk menggabungkan 2 gambar / lebih secara horizontal.
        - np.hstack([<gambar 1>, <gambar 2>]) 



'''


