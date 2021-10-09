from time import sleep
import pyautogui as pg
import ctypes

user32 = ctypes.windll.user32

# user32.keybd_event(0x12, 0, 0, 0) #Alt
# sleep(1)
# user32.keybd_event(0x09, 0, 0, 0) #Tab
# sleep(1)
# user32.keybd_event(0x09, 0, 2, 0) #~Tab
# sleep(0.1)
# user32.keybd_event(0x12, 0, 2, 0) #~Alt

pg.keyDown('alt')
pg.press('tab')
pg.keyUp('alt')

