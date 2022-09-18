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
from find_window import *

def rewind_chain():




    print('done')
    clicks(60, 60)  # кор-ды кнопки паузы

    sleep(1)
    clicks(1368, 126) #кнопка ежедневной награды

    sleep(1)
    clicks(797, 675)  # кнопка выхода

    sleep(0.8)
    clicks(797, 675)  # подтверждение выхода

    sleep(7)

    # тут проверка АФК!!!!

    ######начало афк
    ######

    evade_afk_check()  # функция обхода проверки афк

    ######конец афк
    ######

    ########прокачка голды меты

    sleep(1)
    clicks(79, 206)  # прокачка скилов

    sleep(0.5)

    # 50% - (1412, 906);
    # 25% - (1269, 903);
    # sleep(0.5)
    # pyautogui.moveTo(1269, 903)  # наводка на проценты 50 или 25%
    # pyautogui.click()
    # sleep(0.5)
    #
    # sleep(0.5)
    # pyautogui.moveTo(884, 246)  # прокачка урона
    # pyautogui.click()
    # sleep(1)

    sleep(0.5)
    clicks(1489, 876)  # наводка на проценты 100%

    sleep(1)

    sleep(0.5)
    clicks(1586, 602)  # прокачка крита

    sleep(1)

    ########конец прокачки голды меты

    clicks(68, 909)  # нопка дерева-элексира
    sleep(0.5)

    sleep(0.5)

    clicks(528, 372)  # кнопка rewind

    sleep(0.7)
    clicks(1127, 826)  # подтверждение ревайнда

    sleep(1)

    # вставка прокачки за элексир начало
    # pyautogui.moveTo(1620, 321)  # прокачка элексира
    # pyautogui.click()
    # sleep(1)
    #
    # pyautogui.moveTo(942, 689)  # подтверждение
    # pyautogui.click()
    # sleep(0.7)

    # вставка прокачки за элексир конец

    ######вставка для прокачки за золото начало

    sleep(1)
    clicks(79, 206)  # прокачка скилов

    sleep(0.5)

    sleep(0.5)
    clicks(811, 864)  # прокачка голды

    sleep(0.4)

    ######вставка для прокачки за золото конец

    clicks(1631, 60)  # бой

    sleep(1)

    clicks(867, 279)  # кнопка компания

    sleep(0.3)

    clicks(1004, 658)  # кнопка подтверждение

    sleep(7)

