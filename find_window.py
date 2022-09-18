# import win32gui
# from ctypes import windll
# import win32ui

import win32gui
import win32ui
from ctypes import windll

import pywinauto as pywinauto
from PIL import Image
import win32api, win32con
import time



def unactive_window_screen(item_path, width, height):
    hwnd = win32gui.FindWindow(None, 'BlueStacks App Player')



    hwndDC = win32gui.GetWindowDC(hwnd)
    mfcDC  = win32ui.CreateDCFromHandle(hwndDC)
    saveDC = mfcDC.CreateCompatibleDC()

    saveBitMap = win32ui.CreateBitmap()
    saveBitMap.CreateCompatibleBitmap(mfcDC, width, height) # отвечает за разрешение области считает от 0,0 до указанной пары координат

    saveDC.SelectObject(saveBitMap)


    result = windll.user32.PrintWindow(hwnd, saveDC.GetSafeHdc(), 0)
    # print (result)

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
    img.save('image/DBG/Screens/'+ item_path +'.jpeg')







def img_crop(item_path, item_path_new, w, h, l, t):

    Nimg = Image.open('image/DBG/Screens/' + item_path + '.jpeg')
    Nimg = Nimg.crop((w, h, l, t))
    Nimg.save('image/DBG/Screens/' + item_path_new + '.jpeg')













def clicks(x,y):

    hwnd = win32gui.FindWindow(None, "BlueStacks App Player")
    lParam = win32api.MAKELONG(x, y)
    hwndChild = win32gui.GetWindow(hwnd, win32con.GW_CHILD)


    win32gui.SendMessage(hwnd, win32con.WM_ACTIVATE, win32con.WA_CLICKACTIVE, lParam)
    time.sleep(1)
    win32gui.PostMessage(hwndChild,win32con.WM_LBUTTONDOWN,win32con.MK_LBUTTON, lParam)
    time.sleep(0.5)
    win32gui.PostMessage(hwndChild, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, lParam)



#пример функций
# unactive_window_screen('test_window_grab', 1920, 1024)
#
# img_crop('test_window_grab', , , , )
#
#
# clicks(56,56)




#функция скрина обрабатывает весь экран с рамкой, кроме быстрой панели винды
#функция клика работает с окном обрезая черные рамки и рамки окна