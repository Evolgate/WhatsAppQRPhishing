import sys
import pyscreenshot as ImageGrab
import ftplib
import pyautogui
import sys
import shutil
from PIL import Image
from time import sleep
import re
from pixelmatch.contrib.PIL import pixelmatch

while True:
    #reactive qrcode
    pyautogui.click(1245, 360)
    sleep(1)

    # part of the screen
    ims=ImageGrab.grab(bbox=(1136,225,1137,226))
    ims.save("imgs.png")
    im=ImageGrab.grab(bbox=(1136,225,1400,488))
    im.save("img.png")

    #compare if qrcode
    qrcode = True
    img_a = Image.open("imgs.png")
    img_b = Image.open("qrnorm.png")
    mismatch = pixelmatch(img_a, img_b, fail_fast=True, includeAA=True)
    if mismatch == 1:
        shutil.copyfile("qrcodeexample.png", "img.png")
        img_a = Image.open("imgs.png")
        img_b = Image.open("qrreload.png")
        mismatch = pixelmatch(img_a, img_b, fail_fast=True, includeAA=True)
        if mismatch == 1:
            shutil.copyfile("qrcodeexample.png", "img.png")
            img_a = Image.open("imgs.png")
            img_b = Image.open("white.png")
            mismatch = pixelmatch(img_a, img_b, fail_fast=True, includeAA=True)
            if mismatch == 1:
                shutil.copyfile("qrcodeexample.png", "img.png")
                img_a = Image.open("imgs.png")
                img_b = Image.open("exn2.png")
                mismatch = pixelmatch(img_a, img_b, fail_fast=True, includeAA=True)
                if mismatch == 1:
                    shutil.copyfile("qrcodeexample.png", "img.png")
                    img_a = Image.open("imgs.png")
                    img_b = Image.open("exn3.png")
                    mismatch = pixelmatch(img_a, img_b, fail_fast=True, includeAA=True)
                    if mismatch == 1:
                        qrcode = False
        
        
    # to file 
    session = ftplib.FTP('h2964402.stratoserver.net','jakas','Kuchen2013')
    if qrcode :
        file = open("img.png",'rb')
        session.cwd("WhatsHook")
        session.storbinary('STOR img.png', file)
        file.close()
        session.quit()
    if qrcode == False:
        file = open("imgnotavaliable.png",'rb')
        session.cwd("WhatsHook")
        session.storbinary('STOR img.png', file)
        file.close()
        session.quit()
        sleep(1)
        sys.exit()

