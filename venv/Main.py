import time
from datetime import datetime
import pyautogui
import threading
from GetParams import GetParams

params = GetParams('parameters.json')


def timer():
    get_time = int(time.time())
    return get_time


NOW = timer()
SCREENSHOT_TIME = timer()


def mouse_event():
    global NOW
    pos = pyautogui.position()
    last_position_time = timer()
    while True:
        NOW = timer()
        if pos != pyautogui.position():
            pos = pyautogui.position()
            last_position_time = timer()
        if NOW - last_position_time > params.get_sleep_time():
            pass
        else:
            start_screenshot()


def start_screenshot():
    global NOW
    global SCREENSHOT_TIME
    if (NOW - SCREENSHOT_TIME) > params.get_shot_rate():  # and event.is_set():
        image = pyautogui.screenshot(params.get_path() + str(datetime.now()) + '.png')
        SCREENSHOT_TIME = timer()
    NOW = timer()


event = threading.Event()
t1 = threading.Thread(target=mouse_event)
t2 = threading.Thread(target=start_screenshot)
t1.start()
t2.start()
