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


def rewind_chain():



    pyautogui.moveTo(530, 66)
    print('done')
    pyautogui.moveTo(123, 100)  # кор-ды кнопки паузы
    pyautogui.click()
    sleep(1)
    pyautogui.moveTo(855, 715)  # кнопка выхода
    pyautogui.click()
    sleep(0.8)
    pyautogui.moveTo(855, 715)  # подтверждение выхода
    pyautogui.click()
    sleep(7)

    # тут проверка АФК!!!!

    ######начало афк
    ######

    evade_afk_check()  # функция обхода проверки афк

    ######конец афк
    ######

    ########прокачка голды меты

    sleep(1)
    pyautogui.moveTo(135, 257)  # прокачка скилов
    pyautogui.click()
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
    pyautogui.moveTo(1557, 907)  # наводка на проценты 100%
    pyautogui.click()
    sleep(1)

    sleep(0.5)
    pyautogui.moveTo(1664, 640)  # прокачка крита
    pyautogui.click()
    sleep(1)

    ########конец прокачки голды меты

    pyautogui.moveTo(130, 938)  # нопка дерева-элексира
    sleep(0.5)
    pyautogui.click()
    sleep(0.5)

    pyautogui.moveTo(608, 412)  # кнопка rewind
    pyautogui.click()
    sleep(0.7)
    pyautogui.moveTo(1119, 869)  # подтверждение ревайнда
    pyautogui.click()
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
    pyautogui.moveTo(135, 257)  # прокачка скилов
    pyautogui.click()
    sleep(0.5)

    sleep(0.5)
    pyautogui.moveTo(867, 901)  # прокачка голды
    pyautogui.click()
    sleep(0.4)

    ######вставка для прокачки за золото конец

    pyautogui.moveTo(1699, 105)  # бой
    pyautogui.click()
    sleep(1)

    pyautogui.moveTo(944, 330)  # кнопка компания
    pyautogui.click()
    sleep(0.3)

    pyautogui.moveTo(1070, 692)  # кнопка подтверждение
    pyautogui.click()
    sleep(7)

