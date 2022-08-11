import time
import numpy as np
import win32com.client as win32
import win32api, win32con
import cv2
from PIL import ImageGrab
import imgutils
import easyocr
from matplotlib import pyplot as pl
from mss import mss

import argparse
import pyautogui
from time import sleep
from matplotlib import pyplot as pltd
from termcolor import colored
from evade_afk import *
from rewind_chain import *


Max_days = 5650 # цифра дня, после которого ревайнд




time.sleep(2)

repeat = 1


while True:



    time.sleep(0.2)
    pyautogui.moveTo(800, 800)



    base_screen = ImageGrab.grab(bbox=(0,0, 1920, 1080))
    base_screen.save('image/DBG/Screens/base_screen.jpeg')

    img_grb = cv2.imread('image/DBG/Screens/base_screen.jpeg')
    img_gray = cv2.cvtColor(img_grb, cv2.COLOR_BGR2GRAY)

    # res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    # loc = np.where (res >=0.7)

    for i in range(1):


        #

                #координаты дня 2000+ (866, 56, 1010, 121)
            #координаты области дня 51 (889, 60, 990, 110)

        clean_screen = ImageGrab.grab(bbox=(866, 56, 1010, 121))  # координаты области дня!!!!!!!!!!!!!!!!!!!!!
        clean_screen.save('image/DBG/Screens/clean_screen.jpeg')
        clean_screen = cv2.imread('image/DBG/Screens/clean_screen.jpeg')
        clean_screen_gray = cv2.cvtColor(clean_screen, cv2.COLOR_BGR2GRAY)

        # проверка на >=51 дню
        text = easyocr.Reader(['en'])
        text = text.readtext(clean_screen_gray)
        try:
            new_text = int(text[0][-2])  # фильтр кортежа [([[0, 3], [44, 3], [44, 45], [0, 45]], '51', 0.9999925821627202)]
        except:
            new_text = 0


        print(new_text)

        defeat_screen = ImageGrab.grab(bbox=(750, 339, 1103, 441))  # координаты области DEFEAT!!!!!!!!!!!!!!!!!!!!!
        defeat_screen.save('image/DBG/Screens/defeat_screen.jpeg')
        defeat_screen = cv2.imread('image/DBG/Screens/defeat_screen.jpeg')
        clean_defeat_screen_gray = cv2.cvtColor(defeat_screen, cv2.COLOR_BGR2GRAY)

        # проверка на >=51 дню
        defeat_text = easyocr.Reader(['en'])
        defeat_text = defeat_text.readtext(clean_defeat_screen_gray )
        new_defeat_text = str(defeat_text)

        print(new_defeat_text)


        # проверка на наличие поражения

        if (new_text >= Max_days):  # тут вставлять день

            print(colored('Итерация № ' + str(repeat) + ';', 'green'))  # зеленый цвет вывода кол-ва повторений кода

            repeat = repeat + 1


            rewind_chain() #основная цепочка действий


            break

        elif ("oefeat" or "ofeat" or"defeat" or "Defeat") in new_defeat_text: #сли экран DEFEAT

            print(colored('Итерация № ' + str(repeat) + ';', 'green'))  # зеленый цвет вывода кол-ва повторений кода

            repeat = repeat + 1


            rewind_chain()

            break





