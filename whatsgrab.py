import sys
import pyscreenshot as ImageGrab
import ftplib
from PIL import Image
import imagehash
import pyautogui
import sys
from time import sleep

while True:
    sleep(2)
    #reactive qrcode
    pyautogui.click(1245, 360)

    # part of the screen
    im=ImageGrab.grab(bbox=(1136,225,1400,488))
    im.save("img.png")

    #compare if qrcode
    qrcode = True
    hash0 = imagehash.average_hash(Image.open('img.png')) 
    hash1 = imagehash.average_hash(Image.open('qrcodeexample.png')) 
    cutoff = 32  # maximum bits that could be different between the hashes. 

    if hash0 - hash1 > cutoff:
        qrcode = False

    
    # to file 
    session = ftplib.FTP('SERVER DOMAIN','LOGINNAME','LOGINPASSWORD')
    if qrcode :
        file = open("img.png",'rb')
        session.cwd("WhatsHook")
        session.storbinary('STOR img.png', file)
        file.close()
        session.quit()
    else: 
        file = open("imgnotavaliable.png",'rb')
        session.cwd("WhatsHook")
        session.storbinary('STOR img.png', file)
        file.close()
        session.quit()
        sys.exit()

