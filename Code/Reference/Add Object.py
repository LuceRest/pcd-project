import cv2 as cv
import numpy as np
from tkinter import *
from tkinter import messagebox
from ttkbootstrap import Style
from tkinter import ttk
from tkinter.colorchooser import askcolor
import tkinter as tk
from PIL import Image, ImageTk


def setOriOn():
    global oriOn, maskOn, hsvOn, resultOn
    oriOn = True
    maskOn, hsvOn, resultOn = False, False, False
    print(f'\Original : {oriOn}')

def setMaskOn():
    global oriOn, maskOn, hsvOn, resultOn
    maskOn = True
    oriOn, hsvOn, resultOn = False, False, False
    print(f'\nMask : {maskOn}')
    
def setHsvOn():
    global oriOn, maskOn, hsvOn, resultOn
    hsvOn = True
    oriOn, maskOn, resultOn = False, False, False
    print(f'\nHSV : {hsvOn}')
    
def setResultOn():
    global oriOn, maskOn, hsvOn, resultOn
    resultOn = True
    oriOn, maskOn, hsvOn = False, False, False
    print(f'\nResult : {resultOn}')
    
def addObject():
    hueMin = int(sldHueMin.get())
    satMin = int(sldSatMin.get())
    valueMin = int(sldValueMin.get())
    hueMax = int(sldHueMax.get())
    satMax = int(sldSatMax.get())
    valueMax = int(sldValueMax.get())
    
    colorObject.append([hueMin, satMin, valueMin, hueMax, satMax, valueMax])
    messagebox.showinfo('Notification', 'Object added successfully!')

    
def addColor():
    hasil = askcolor(title="Pilih Warnanya")
    rgb, hex = hasil
    
    if rgb != None:
        colorPoint.append( [rgb[0], rgb[1], rgb[2]] )
        messagebox.showinfo('Notification', 'Color added successfully!')

def cek():
    print(f'colorObject : {colorObject}\n')
    print(f'colorPoint : {colorPoint}\n')
    
def resizeImg(img, width, height):
    img = cv.resize(img, (width, height), interpolation=cv.INTER_CUBIC)
    return img

def hsv(img):
    imgHSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    return imgHSV

def mask(img):
    hueMin = int(sldHueMin.get())
    satMin = int(sldSatMin.get())
    valueMin = int(sldValueMin.get())
    hueMax = int(sldHueMax.get())
    satMax = int(sldSatMax.get())
    valueMax = int(sldValueMax.get())
    
    imgHSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    lower = np.array([hueMin, satMin, valueMin])
    upper = np.array([hueMax, satMax, valueMax])
    mask = cv.inRange(imgHSV, lower, upper)
    
    mask = cv.cvtColor(mask, cv.COLOR_GRAY2BGR)
    return mask

def result(img):
    hueMin = int(sldHueMin.get())
    satMin = int(sldSatMin.get())
    valueMin = int(sldValueMin.get())
    hueMax = int(sldHueMax.get())
    satMax = int(sldSatMax.get())
    valueMax = int(sldValueMax.get())
    
    imgHSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    lower = np.array([hueMin, satMin, valueMin])
    upper = np.array([hueMax, satMax, valueMax])
    mask = cv.inRange(imgHSV, lower, upper)
    
    result = cv.bitwise_and(img, img, mask = mask)
    return result
    

def videoStream():
    global cap, oriOn, maskOn, hsvOn, resultOn
    
    sucess, img = cap.read()
    imgCV = cv.cvtColor(img, cv.COLOR_BGR2RGBA)

    if oriOn:
        print("\nOriginal On")
        pass
    elif hsvOn:
        imgCV = hsv(imgCV)
        print('\nHSV On')
    elif maskOn:
        imgCV = mask(imgCV)
        print("\nMask On")
    elif resultOn:
        imgCV = result(imgCV)
        print("\nResult On")
    else:
        print("\nOriginal On")
        pass
    
    # imgCV = resizeImg(imgCV, 852, 480)
    # imgPill = Image.fromarray(imgCV)
    # imgtk = ImageTk.PhotoImage(image=imgPill)
    
    
    # lblImgRes.imgtk = imgtk
    # lblImgRes.configure(image=imgtk)
    # lblImgRes.pack()
    # lblImgRes.after(1, videoStream)


def sldMove(e):
    hueMin = int(sldHueMin.get())
    satMin = int(sldSatMin.get())
    valueMin = int(sldValueMin.get())
    hueMax = int(sldHueMax.get())
    satMax = int(sldSatMax.get())
    valueMax = int(sldValueMax.get())
    
    lblHueMin.configure(text=f'HUE Min : {hueMin}')
    lblSatMin.configure(text=f'SAT Min : {satMin}')
    lblValueMin.configure(text=f'VALUE Min : {valueMin}')
    lblHueMax.configure(text=f'HUE Max : {hueMax}')
    lblSatMax.configure(text=f'SAT Max : {satMax}')
    lblValueMax.configure(text=f'VALUE Max : {valueMax}')


if __name__ == '__main__':
    
    style = Style()
    window = style.master
    
    oriOn = True
    hsvOn, maskOn, resultOn = False, False, False

    colorObject = []
    colorPoint = []

    cap = cv.VideoCapture(0)

    
    frm = ttk.Frame(window, style='primary.TFrame')
    # frm.pack(side='top')
    frm.pack_propagate(0)
    frm.pack(fill=tk.BOTH, expand=1)

    # Size window : 852 x 480


    # Frame

    frmBtn = ttk.Frame(frm, style='secondary.TFrame', width=100, height=480)
    frmBtn.grid(row=0, column=0, padx=(50,25), pady=25)

    frmResult = ttk.Frame(frm, style='secondary.TFrame', width=852, height=480)
    # frmResult.pack_propagate(0)
    frmResult.grid(row=0, column=1, padx=(25,50), pady=25)

    frmSlider = ttk.Frame(frm, style='secondary.TFrame', width=1055, height=150)
    frmSlider.grid(row=1, column=0, columnspan=2, padx=50, pady=(20,50))

    frmSliderMin = ttk.Frame(frmSlider, style='info.TFrame', width=500, height=150)
    frmSliderMin.grid(row=0, column=0, padx=(20,30), pady=20)

    frmSliderMax = ttk.Frame(frmSlider, style='info.TFrame', width=500, height=150)
    frmSliderMax.grid(row=0, column=1, padx=(30,20), pady=20)

    # Label
    
    lblImgRes = ttk.Label(frmResult)


    # Button

    btnOri = ttk.Button(frmBtn, text='Original', style='success.TButton', cursor="hand2", width=12, command=setOriOn)
    btnOri.pack(side='top', padx=33, pady=19)

    btnMask = ttk.Button(frmBtn, text='Mask', style='success.TButton', cursor="hand2", width=12, command=setMaskOn)
    btnMask.pack(side='top', padx=33, pady=19)

    btnHSV = ttk.Button(frmBtn, text='HSV', style='success.TButton', cursor="hand2", width=12, command=setHsvOn)
    btnHSV.pack(side='top', padx=33, pady=19)

    btnResult = ttk.Button(frmBtn, text='Result', style='success.TButton', cursor="hand2", width=12, command=setResultOn)
    btnResult.pack(side='top', padx=33, pady=19)

    btnAddObject = ttk.Button(frmBtn, text='Add Object', style='success.TButton', cursor="hand2", width=12, command=addObject)
    btnAddObject.pack(side='top', padx=33, pady=19)

    btnAddColor = ttk.Button(frmBtn, text='Add Color', style='success.TButton', cursor="hand2", width=12, command=addColor)
    btnAddColor.pack(side='top', padx=33, pady=19)

    btnExit = ttk.Button(frmBtn, text='Back', style='danger.TButton', cursor="hand2", width=12, command=cek)
    btnExit.pack(side='top', padx=33, pady=19)



    # Slider

    sldHueMin = ttk.Scale(frmSliderMin, from_=0, to=179, value=0, orient='horizontal', style='info.Horizontal.TScale', length=255, command=sldMove)
    lblHueMin = ttk.Label(frmSliderMin, text=f'HUE Min : {sldHueMin.get()}', style='info.Inverse.TLabel', width=15)
    lblHueMin.grid(row=0, column=0, padx=20, pady=10)
    sldHueMin.grid(row=0, column=1, padx=20, pady=10)

    sldSatMin = ttk.Scale(frmSliderMin, from_=0, to=255, value=0, orient='horizontal', style='info.Horizontal.TScale', length=255, command=sldMove)
    lblSatMin = ttk.Label(frmSliderMin, text=f'SAT Min : {sldSatMin.get()}', style='info.Inverse.TLabel', width=15)
    lblSatMin.grid(row=1, column=0, padx=20, pady=10)
    sldSatMin.grid(row=1, column=1, padx=20, pady=10)

    sldValueMin = ttk.Scale(frmSliderMin, from_=0, to=255, value=0, orient='horizontal', style='info.Horizontal.TScale', length=255, command=sldMove)
    lblValueMin = ttk.Label(frmSliderMin, text=f'VALUE Min : {sldValueMin.get()}', style='info.Inverse.TLabel', width=15)
    lblValueMin.grid(row=2, column=0, padx=20, pady=10)
    sldValueMin.grid(row=2, column=1, padx=20, pady=10)

    sldHueMax = ttk.Scale(frmSliderMax, from_=0, to=179, value=179, orient='horizontal', style='info.Horizontal.TScale', length=255, command=sldMove)
    lblHueMax = ttk.Label(frmSliderMax, text=f'HUE Max : {sldHueMax.get()}', style='info.Inverse.TLabel', width=15)
    lblHueMax.grid(row=0, column=0, padx=20, pady=10)
    sldHueMax.grid(row=0, column=1, padx=20, pady=10)

    sldSatMax = ttk.Scale(frmSliderMax, from_=0, to=255, value=255, orient='horizontal', style='info.Horizontal.TScale', length=255, command=sldMove)
    lblSatMax = ttk.Label(frmSliderMax, text=f'SAT Max : {sldSatMax.get()}', style='info.Inverse.TLabel', width=15)
    lblSatMax.grid(row=1, column=0, padx=20, pady=10)
    sldSatMax.grid(row=1, column=1, padx=20, pady=10)

    sldValueMax = ttk.Scale(frmSliderMax, from_=0, to=255, value=255, orient='horizontal', style='info.Horizontal.TScale', length=255, command=sldMove)
    lblValueMax = ttk.Label(frmSliderMax, text=f'VALUE Max : {sldValueMax.get()}', style='info.Inverse.TLabel', width=15)
    lblValueMax.grid(row=2, column=0, padx=20, pady=10)
    sldValueMax.grid(row=2, column=1, padx=20, pady=10)


    window.title("Virtual Paint")
    # window.geometry("1280x720")
    window.resizable(0, 0)
    window.after(1, videoStream)
    window.mainloop()


