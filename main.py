import pyqrcode
import sys
ssid = input("Please enter network id: ")
security = 'WPA'
password = input("Please Enter password: ")
qr = pyqrcode.create(f'WIFI:S:{ssid};T:{security};P:{password};;')
print(qr.terminal(quiet_zone=1))
