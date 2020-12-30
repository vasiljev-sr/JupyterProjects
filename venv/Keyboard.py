import time
from datetime import datetime
import json
import threading

import pyautogui

with open("parametrs.json", "r") as reader:
    data = json.load(reader)


def timer():
    get_time = int(time.time())
    return get_time


NOW = timer()
SCREENSHOT_TIME = timer()


def mouse_event():
    global NOW
    s = {'pos': pyautogui.position(), 'timer': timer()}
    while True:
        NOW = timer()
        if s['pos'] != pyautogui.position():  # and (timer() - s['timer']) > data["sleep time"] :
            s = {'pos': pyautogui.position(), 'timer': timer()}

        if NOW - s['timer'] > 10:
            event.clear()
        else:
            event.set()



def start_screenshot():
    global NOW
    global SCREENSHOT_TIME
    event.wait()
    while event.is_set():
        if (NOW - SCREENSHOT_TIME) > 5: # and event.is_set():
            #image = pyautogui.screenshot(data['path'] + str(datetime.now()) + '.png')
            print('Screenshot')
            SCREENSHOT_TIME = timer()
        NOW = timer()


event = threading.Event()
t1 = threading.Thread(target=mouse_event)
t2 = threading.Thread(target=start_screenshot)
t1.start()
t2.start()
