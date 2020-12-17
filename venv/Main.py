import time
from datetime import datetime
import json

import pyautogui

with open("parametrs.json", "r") as reader:
    data = json.load(reader)

def timer():
    get_time = int(time.time())
    return  get_time

def mouse_is_active():
    while True:
        s = {'pos': pyautogui.position(), 'timer': timer()}
        if s['pos'] == pyautogui.position(): #and (timer() - s['timer']) > data["sleep time"] :

            return False
        else:
            return True
while True:
    image = pyautogui.screenshot(data['path'] + str(datetime.now()) + '.png')
    time.sleep(data['shot rate'])




