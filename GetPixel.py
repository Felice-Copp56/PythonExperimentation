import time
import PIL.ImageGrab
import cv2
import pyautogui,sys
import numpy as np
"""
time.sleep(3)
rgb = PIL.ImageGrab.grab().load()[100,100]
print(rgb)
"""


print('Press Ctrl-C to quit.')
try:
    while True:

        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\n')

