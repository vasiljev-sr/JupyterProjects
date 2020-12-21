import time
from datetime import datetime
import json
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
        if s['pos'] != pyautogui.position():
            s = {'pos': pyautogui.position(), 'timer': timer()}
        if NOW - s['timer'] > data["sleep time"]:
            event.clear()
        else:
            event.set()


def start_screenshot():
    global NOW
    global SCREENSHOT_TIME
    while True:
        if (NOW - SCREENSHOT_TIME) > data["shot rate"] and event.is_set():
            image = pyautogui.screenshot(data['path'] + str(datetime.now()) + '.png')
            SCREENSHOT_TIME = timer()
        NOW = timer()


event = threading.Event()
t1 = threading.Thread(target=mouse_event)
t2 = threading.Thread(target=start_screenshot)
t1.start()
t2.start()
