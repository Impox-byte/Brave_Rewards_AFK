from pynput.mouse import Button, Controller
import pyautogui
import time
from pynput.keyboard import Controller as Controller2, Key
import ctypes
import random

PROCESS_PER_MONITOR_DPI_AWARE = 2
ctypes.windll.shcore.SetProcessDpiAwareness(PROCESS_PER_MONITOR_DPI_AWARE)  
#(1565, 912)
#(255, 32, 0)
# initialize mouse
mouse = Controller()
kb = Controller2()
# set default values of variables
# tested on Win10, 1920x1280, default taskbar size and position
# position of the close botton of the brave for windows notification
brave_close_x = 1725
brave_close_y = 900
# postion of an orange pixel of the brave icon in the notification area
brave_pix_x = 1565
brave_pix_y_1 = 912
brave_pix_y_2 = 916 
# how often the script is run in seconds
sleep_timer = 5
# pixel value to compare in RGB, default (255, 85, 0) is orange
pixel_compare_val = (255, 32, 0)
def check_pixel_val():
    try:
        pix_val = pyautogui.pixel(brave_pix_x, brave_pix_y_1)
        pix_val_2 = pyautogui.pixel(brave_pix_x, brave_pix_y_2)
        print(pix_val + pix_val_2)
    except:
        print("Cannot get pixel for the moment")
        pix_val = (0, 0, 0)
        pix_val_2 = (0, 0, 0)
    # if pix_val == pixel_compare_val:
    if pix_val == pixel_compare_val or pix_val_2 == pixel_compare_val:
        return True
    else:
        return False


def close_brave_notify():
    currentp = mouse.position
    mouse.position = (brave_close_x, brave_close_y)
    mouse.press(Button.left)
    mouse.release(Button.left)
    mouse.position = currentp


while True:
    negative = random.randint(-9, 0)
    positive = random.randint(0, 9)
    mouse.scroll(0, positive)
    time.sleep(1)
    mouse.scroll(0, negative)
    if check_pixel_val() is True:
        close_brave_notify()    
        time.sleep(5)
        kb.press(Key.ctrl)
        kb.press("w")
        kb.release("w")
        kb.release(Key.ctrl)
    # print(check_pixel_val())
    time.sleep(sleep_timer)
