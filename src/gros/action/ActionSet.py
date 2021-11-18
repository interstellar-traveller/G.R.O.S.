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
            "\t",
            "\n",
            "\r",
            " ",
            "!",
            '"',
            "#",
            "$",
            "%",
            "&",
            "'",
            "(",
            ")",
            "*",
            "+",
            ",",
            "-",
            ".",
            "/",
            "0",
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            ":",
            ";",
            "<",
            "=",
            ">",
            "?",
            "@",
            "[",
            "\\",
            "]",
            "^",
            "_",
            "`",
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
            "g",
            "h",
            "i",
            "j",
            "k",
            "l",
            "m",
            "n",
            "o",
            "p",
            "q",
            "r",
            "s",
            "t",
            "u",
            "v",
            "w",
            "x",
            "y",
            "z",
            "{",
            "|",
            "}",
            "~",
            "accept",
            "add",
            "alt",
            "altleft",
            "altright",
            "apps",
            "backspace",
            "browserback",
            "browserfavorites",
            "browserforward",
            "browserhome",
            "browserrefresh",
            "browsersearch",
            "browserstop",
            "capslock",
            "clear",
            "convert",
            "ctrl",
            "ctrlleft",
            "ctrlright",
            "decimal",
            "del",
            "delete",
            "divide",
            "down",
            "end",
            "enter",
            "esc",
            "escape",
            "execute",
            "f1",
            "f10",
            "f11",
            "f12",
            "f13",
            "f14",
            "f15",
            "f16",
            "f17",
            "f18",
            "f19",
            "f2",
            "f20",
            "f21",
            "f22",
            "f23",
            "f24",
            "f3",
            "f4",
            "f5",
            "f6",
            "f7",
            "f8",
            "f9",
            "final",
            "fn",
            "hanguel",
            "hangul",
            "hanja",
            "help",
            "home",
            "insert",
            "junja",
            "kana",
            "kanji",
            "launchapp1",
            "launchapp2",
            "launchmail",
            "launchmediaselect",
            "left",
            "modechange",
            "multiply",
            "nexttrack",
            "nonconvert",
            "num0",
            "num1",
            "num2",
            "num3",
            "num4",
            "num5",
            "num6",
            "num7",
            "num8",
            "num9",
            "numlock",
            "pagedown",
            "pageup",
            "pause",
            "pgdn",
            "pgup",
            "playpause",
            "prevtrack",
            "print",
            "printscreen",
            "prntscrn",
            "prtsc",
            "prtscr",
            "return",
            "right",
            "scrolllock",
            "select",
            "separator",
            "shift",
            "shiftleft",
            "shiftright",
            "sleep",
            "space",
            "stop",
            "subtract",
            "tab",
            "up",
            "volumedown",
            "volumemute",
            "volumeup",
            "win",
            "winleft",
            "winright",
            "yen",
            "command",
            "option",
            "optionleft",
            "optionright",
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
            if index > 2:
                self.action_list.append(str(list(all_funcs[index])[0]))
        return self.action_list
    
    def switch(self):
        # switch between open apps
        pg.keyDown('alt')
        pg.press('tab')
        pg.keyUp('alt')
        
    def printScreen(self):
        # printscreen (full-screen)
        pg.press('printscreen')

    def showDesktop(self):
        # show the desktop of your computer
        pg.keyDown('win')
        pg.press('d')
        pg.keyUp('win')
        
    
    


acs = ActionSet()

# acs.switch()