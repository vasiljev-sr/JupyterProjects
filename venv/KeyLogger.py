import pynput
import time
from pynput.keyboard import Key, Listener



def timer():
    get_time = int(time.time())
    return get_time


KEY_PUSHED_TIME = 0


def on_press(key):
    global KEY_PUSHED_TIME
    KEY_PUSHED_TIME = timer()
    print(KEY_PUSHED_TIME)


#with Listener(on_press=on_press) as l:

listener = Listener (
    on_press = on_press)
listener.start ()
