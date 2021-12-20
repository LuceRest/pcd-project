import cv2
import numpy as np
from tkinter import *
from ttkbootstrap import Style
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk




style = Style()
window = style.master


frm = ttk.Frame(window, style='primary.TFrame')
# frm.pack(side='top')
frm.pack_propagate(0)
frm.pack(fill=tk.BOTH, expand=1)

# Size window : 852 x 480


# Frame


frmImg = ttk.Frame(frm, style='secondary.TFrame', width=1000, height=472)
# frmImg.pack_propagate(0)
frmImg.grid(row=0, column=0, columnspan=3, padx=50, pady=20)

frmImgOri = ttk.Frame(frmImg, style='info.TFrame', width=354, height=472)
# frmImgOri.pack_propagate(0)
frmImgOri.grid(row=1, column=0, padx=30, pady=(10,20))

frmImgRoi = ttk.Frame(frmImg, style='info.TFrame', width=100, height=100)
# frmImgRoi.pack_propagate(0)
frmImgRoi.grid(row=1, column=1, padx=30, pady=(10,20))

frmImgRes = ttk.Frame(frmImg, style='info.TFrame', width=354, height=472)
# frmImgRes.pack_propagate(0)
frmImgRes.grid(row=1, column=2, padx=30, pady=(10,20))

frmSlider = ttk.Frame(frm, style='secondary.TFrame', width=1000, height=150)
# frmSlider.pack_propagate(0)
# frmSlider.pack(side="left", padx=20, pady=30)
frmSlider.grid(row=1, column=0, columnspan=2, padx=50, pady=20)

frmSliderMin = ttk.Frame(frmSlider, style='info.TFrame', width=500, height=150)
frmSliderMin.grid(row=0, column=0, padx=20, pady=20)

frmBtn = ttk.Frame(frmSlider, style='secondary.TFrame', width=40, height=150)
frmBtn.grid(row=0, column=1, padx=10, pady=20)

# frmSelectColor = ttk.Frame(frmSlider, style='info.TFrame', width=100, height=120)
# frmSelectColor.grid(row=0, column=1, padx=15, pady=15)

frmSliderMax = ttk.Frame(frmSlider, style='info.TFrame', width=500, height=150)
frmSliderMax.grid(row=0, column=2, padx=20, pady=20)


# Label Description

lblDescOri = ttk.Label(frmImg, text='Original', font='20', style='secondary.Inverse.TLabel')
lblDescOri.grid(row=0, column=0, padx=20, pady=(10,0))

lblDescRoi = ttk.Label(frmImg, text='ROI', font='20', style='secondary.Inverse.TLabel')
lblDescRoi.grid(row=0, column=1, padx=20, pady=(10,0))

lblDescRes = ttk.Label(frmImg, text='Color Detection', font='20', style='secondary.Inverse.TLabel')
lblDescRes.grid(row=0, column=2, padx=20, pady=(10,0))


# Label Image

lblImgOri = ttk.Label(frmImgOri)
# lblImgRes.pack()

lblImgRoi = ttk.Label(frmImgRoi)
# lblImgRes.pack()

lblImgRes = ttk.Label(frmImgRes)
# lblImgRes.pack()


# Button

btnBrowse = ttk.Button(frmBtn, text='Browse Image', style='success.TButton', cursor="hand2", width=12)
# btnBrowse.pack(side='top', padx=10, pady=10)
btnBrowse.grid(row=0, column=0, padx=10, pady=10)

btnRoi = ttk.Button(frmBtn, text='ROI', style='success.TButton', cursor="hand2", width=12)
btnRoi.grid(row=1, column=0, padx=10, pady=10)
# btnRoi.pack(side='top', padx=10, pady=10)

btnSave = ttk.Button(frmBtn, text='Save', style='success.TButton', cursor="hand2", width=12)
btnSave.grid(row=0, column=1, padx=10, pady=10)
# btnSave.pack(side='top', padx=10, pady=10)

btnExit = ttk.Button(frmBtn, text='Exit', style='danger.TButton', cursor="hand2", width=12)
btnExit.grid(row=1, column=1, padx=10, pady=10)
# btnExit.pack(side='top', padx=10, pady=10)


# Slider

sldHueMin = ttk.Scale(frmSliderMin, from_=0, to=179, value=0, orient='horizontal', style='info.Horizontal.TScale', length=255)
lblHueMin = ttk.Label(frmSliderMin, text=f'HUE Min : {sldHueMin.get()}', style='info.Inverse.TLabel', width=15)
lblHueMin.grid(row=0, column=0, padx=20, pady=10)
sldHueMin.grid(row=0, column=1, padx=20, pady=10)

sldSatMin = ttk.Scale(frmSliderMin, from_=0, to=255, value=0, orient='horizontal', style='info.Horizontal.TScale', length=255)
lblSatMin = ttk.Label(frmSliderMin, text=f'SAT Min : {sldSatMin.get()}', style='info.Inverse.TLabel', width=15)
lblSatMin.grid(row=1, column=0, padx=20, pady=10)
sldSatMin.grid(row=1, column=1, padx=20, pady=10)

sldValueMin = ttk.Scale(frmSliderMin, from_=0, to=255, value=0, orient='horizontal', style='info.Horizontal.TScale', length=255)
lblValueMin = ttk.Label(frmSliderMin, text=f'VALUE Min : {sldValueMin.get()}', style='info.Inverse.TLabel', width=15)
lblValueMin.grid(row=2, column=0, padx=20, pady=10)
sldValueMin.grid(row=2, column=1, padx=20, pady=10)

sldHueMax = ttk.Scale(frmSliderMax, from_=0, to=179, value=179, orient='horizontal', style='info.Horizontal.TScale', length=255)
lblHueMax = ttk.Label(frmSliderMax, text=f'HUE Max : {sldHueMax.get()}', style='info.Inverse.TLabel', width=15)
lblHueMax.grid(row=0, column=0, padx=20, pady=10)
sldHueMax.grid(row=0, column=1, padx=20, pady=10)

sldSatMax = ttk.Scale(frmSliderMax, from_=0, to=255, value=255, orient='horizontal', style='info.Horizontal.TScale', length=255)
lblSatMax = ttk.Label(frmSliderMax, text=f'SAT Max : {sldSatMax.get()}', style='info.Inverse.TLabel', width=15)
lblSatMax.grid(row=1, column=0, padx=20, pady=10)
sldSatMax.grid(row=1, column=1, padx=20, pady=10)

sldValueMax = ttk.Scale(frmSliderMax, from_=0, to=255, value=255, orient='horizontal', style='info.Horizontal.TScale', length=255)
lblValueMax = ttk.Label(frmSliderMax, text=f'VALUE Max : {sldValueMax.get()}', style='info.Inverse.TLabel', width=15)
lblValueMax.grid(row=2, column=0, padx=20, pady=10)
sldValueMax.grid(row=2, column=1, padx=20, pady=10)


window.title("Color Detection")
# window.geometry("1280x720")
window.resizable(0, 0)
window.mainloop()


