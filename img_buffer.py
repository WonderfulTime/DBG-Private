import time
import urllib

import numpy as np
import pyperclip
import win32com.client as win32
import win32api, win32con
import cv2
from PIL import ImageGrab
import imgutils
import easyocr
from matplotlib import pyplot as pl
from mss import mss
# from cStringIO import StringIO
import io
import argparse
import pyautogui
from time import sleep
from matplotlib import pyplot as pltd
import io
import win32gui, win32con, win32api, win32ui
from ctypes import windll
from PIL import Image



def unactive_window_screen_buffer(item_path, width, height):
    hwnd = win32gui.FindWindow(None, 'BlueStacks App Player')



    hwndDC = win32gui.GetWindowDC(hwnd)
    mfcDC  = win32ui.CreateDCFromHandle(hwndDC)
    saveDC = mfcDC.CreateCompatibleDC()

    saveBitMap = win32ui.CreateBitmap()
    saveBitMap.CreateCompatibleBitmap(mfcDC, width, height) # отвечает за разрешение области считает от 0,0 до указанной пары координат

    saveDC.SelectObject(saveBitMap)


    result = windll.user32.PrintWindow(hwnd, saveDC.GetSafeHdc(), 0)
    print (result)

    bmpinfo = saveBitMap.GetInfo()
    bmpstr = saveBitMap.GetBitmapBits(True)

    img = Image.frombuffer(
        'RGB',
        (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
        bmpstr, 'raw', 'BGRX', 0, 1)

    win32gui.DeleteObject(saveBitMap.GetHandle())
    saveDC.DeleteDC()
    mfcDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, hwndDC)


    return img


def img_buffer():

    img1 = unactive_window_screen_buffer('window_grab_buffer', 1920, 1024)

    # return img1

    t = cv2.cvtColor(np.array(img1), cv2.COLOR_BGR2RGB) #в переменной хранится буфер изображения

    cv2.imwrite('image/DBG/Screens/123.jpeg', t)