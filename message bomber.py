#firstly run this script and then set the cursor to the textbox in whatsapp web

import random
import pyautogui
import time

list = []  #enter messages as strings inside this list.
time.sleep(5)

while (True):
    for word in list:
        ab = random.choice(list)
        pyautogui.typewrite(ab)
        pyautogui.press("enter")
