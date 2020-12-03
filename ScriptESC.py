import datetime
import time
import pyautogui
import pynput
import PIL.ImageGrab
from pynput.mouse import Button,Controller

mouse = Controller()
keyboard = Controller()
time.sleep(3)
mouse.click(Button.left, 1)
pyautogui.press("O")
"""mouse = Controller()
time.sleep(3)
t1 = time.time()
x, y = pyautogui.position()
rgb = PIL.ImageGrab.grab().load()[x,y]
print("PRIMO CLICK",rgb)
mouse.click(Button.left,1)
t2=time.time()
x,y = pyautogui.position()
rgb = PIL.ImageGrab.grab().load()[x,y]
print("SECONDO CLICK",rgb)
print(t2-t1)
"""