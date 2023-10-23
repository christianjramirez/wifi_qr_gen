import pyqrcode
import tkinter
from tkinter import ttk
import sys


ssid = input("Please enter network id: ")
security = 'WPA'
password = input("Please Enter password: ")
qr = pyqrcode.create(f'WIFI:S:{ssid};T:{security};P:{password};;')

code_xbm = qr.xbm(scale=5)
##Creates window
top = tkinter.Tk()
top.title('qr_code_gen')

##Creates bitmap of qr code
code_bmp = tkinter.BitmapImage(data=code_xbm)
code_bmp.config(background="white")

label = tkinter.Label(image=code_bmp)
label.pack()
top.mainloop()