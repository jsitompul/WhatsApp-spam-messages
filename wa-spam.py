import random
import pyautogui as pg
import time


message = ['Cieee penipu','Dasar tukang tipu','Ketauan nihh yee','Lu kurang jago bro hahaha','SDM RENDAH']

time.sleep(5)

for i in range(1000):
    ejekan = random.choice(message)
    pg.write(ejekan)
    pg.press('enter')

