import sys
sys.path.append("f:/0Desk/IBDP/ComputerScience/IA/code/GROS/src")

from gros.gesture.Gesture import Gesture
from gros.gesture.GestureSet import GestureSet
from gros.gesture.GestureSequence import GestureSequence
from gros.action.Action import Action
from gros.action.ActionSet import ActionSet
from gros.initialize.Initialize import Initialize

class InitializeModeOS(Initialize):
    def __init__(self) -> None:
        super().__init__()
        self.action_activation_list = ["switch", "printscreen", "showDesktop", "minimize"]
        self.gesture_activation_list = ["palm", "fist", "point", "double_point", "side_palm"]
        self.partial_action_activation(self.action_activation_list)
        self.partial_gesture_activation(self.gesture_activation_list)
    
    