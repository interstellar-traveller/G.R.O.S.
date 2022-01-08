import inspect
from time import sleep
import pyautogui as pg

class ActionSet(object):
    def __init__(self):
        """initialize an abstract concept: action set
        Specifies all the keys invovled in performing the actions
        Initialize an action list that stores all the action that are defined.
        All actions are performed based on Windows10 keyboard shortcuts.
        """
        self.keys = [
            "\t","\n","\r"," ","!",'"',"#","$","%","&","'","(",")","*","+",",","-",".","/",
            "0","1","2","3","4","5","6","7","8","9",
            ":",";","<","=",">","?","@","[","\\","]","^","_","`",
            "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
            "{","|","}","~",
            "accept","add","alt","altleft","altright","apps","backspace","browserback","browserfavorites","browserforward","browserhome","browserrefresh","browsersearch","browserstop",
            "capslock","clear","convert","command","ctrl","ctrlleft","ctrlright",
            "decimal","del","delete","divide","down",
            "end","enter","esc","escape","execute",
            "f1","f2","f3","f4","f5","f6","f7","f8","f9","f10","f11","f12","f13","f14","f15","f16","f17","f18","f19","f2","f20","f21","f22","f23","f24","final","fn",
            "hanguel","hangul","hanja","help","home",
            "insert",
            "junja",
            "kana","kanji",
            "launchapp1","launchapp2","launchmail","launchmediaselect","left",
            "modechange","multiply",
            "nexttrack","nonconvert","num0","num1","num2","num3","num4","num5","num6","num7","num8","num9","numlock",
            "option","optionleft","optionright",
            "pagedown","pageup","pause","pgdn","pgup","playpause","prevtrack","print","printscreen","prntscrn","prtsc","prtscr",
            "return","right",
            "scrolllock","select","separator","shift","shiftleft","shiftright","sleep","space","stop","subtract",
            "tab",
            "up",
            "volumedown","volumemute","volumeup",
            "win","winleft","winright",
            "yen",
        ]
        self.action_list = []

    def get_keys(self):
        """get all keys that can be used to form keyboard shortcuts
        """
        return self.keys
    
    def get_action_list(self):
        """get all actions that are defined.
        Actions are defined as attribute functions of this class.
        The functions are collected by the inspect module of Python,
        and all of them are stored in the list: action_list
        

        Returns:
            action_list [list]: all actions defined in this class
        """
        all_funcs = inspect.getmembers(ActionSet, inspect.isfunction)
        # print(all_funcs)
        for index in range(len(all_funcs)):
            if str(list(all_funcs[index])[0]) not in ["__init__","get_keys","get_action_list"]:
                self.action_list.append(str(list(all_funcs[index])[0]))
        return self.action_list
    
    # OS mode actions    
    def switch(self):
        # switch between the first two opened pages
        pg.keyDown('alt')
        pg.keyDown('ctrl')
        pg.press('tab')
        pg.keyUp('ctrl')
        pg.keyUp('alt')
        
    def printScreen(self):
        # open printscreen
        pg.keyDown("win")
        pg.keyDown("shift")
        pg.keyDown("s")
        pg.keyUp("s")
        pg.keyUp("shift")
        pg.keyUp("win")

    def showDesktop(self):
        # show the desktop of your computer
        pg.keyDown('win')
        pg.press('d')
        pg.keyUp('win')
        
    def minimize(self):
        # minimize the active window on top
        pg.keyDown('alt')
        pg.press('space')
        pg.press('n')
        pg.keyUp('alt')
        
    # PPT mode actions
    def nextpage(self):
        # to next ppt page
        pg.press("right")
        
    def prevpage(self):
        # to previous ppt page
        pg.press("left")
        
    def enter(self):
        # press enter
        pg.press("enter")
        
    def exit(self):
        pg.press("esc")
    
    # virtual desktop actions
    def create(self):
        # create a new virtual desktop
        pg.keyDown("win")
        pg.keyDown("ctrl")
        pg.keyDown("d")
        pg.keyUp("d")
        pg.keyUp("ctrl")
        pg.keyUp("win")
        
    def close(self):
        # close the current activate virtual desktop
        pg.keyDown("win")
        pg.keyDown("ctrl")
        pg.keyDown("f4")
        pg.keyUp("f4")
        pg.keyUp("ctrl")
        pg.keyUp("win")
        
    def prevdesk(self):
        # shift to the previous virtual desktop
        pg.keyDown("win")
        pg.keyDown("ctrl")
        pg.keyDown("left")
        pg.keyUp("left")
        pg.keyUp("ctrl")
        pg.keyUp("win")
        
    def nextdesk(self):
        # shift to the next virtual desktop
        pg.keyDown("win")
        pg.keyDown("ctrl")
        pg.keyDown("right")
        pg.keyUp("right")
        pg.keyUp("ctrl")
        pg.keyUp("win")

    # document mode (additional actions to desktop mode)
    def save(self):
        pg.keyDown('ctrl')
        pg.press('s')
        pg.keyUp('ctrl')

# acs = ActionSet()
# acs.minimize()
# acs.switch()
# acs.create()
# print(acs.get_action_list())