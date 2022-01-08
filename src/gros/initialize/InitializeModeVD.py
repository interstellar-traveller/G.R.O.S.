import sys
sys.path.append("f:/0Desk/IBDP/ComputerScience/IA/code/GROS/src")

from gros.gesture.Gesture import Gesture
from gros.gesture.GestureSet import GestureSet
from gros.gesture.GestureSequence import GestureSequence
from gros.action.Action import Action
from gros.action.ActionSet import ActionSet
from gros.initialize.Initialize import Initialize
from gros.initialize.SequenceActionPair import SequenceActionPair

class InitializeModeVD(Initialize):
    def __init__(self) -> None:
        super().__init__()
        self.action_activation_list = ["create", "close", "prevdesk", "nextdesk"]
        self.gesture_activation_list = ["palm", "fist", "three_open", "side_palm", "horiz_palm"]
        self.partial_action_activation(self.action_activation_list)
        self.partial_gesture_activation(self.gesture_activation_list)
    
    def pairing(self):
        gesPool = []
        gesPool.append(GestureSequence("three_open", [Gesture("fist"), Gesture("three_open")])) # create
        gesPool.append(GestureSequence("three_hold", [Gesture("palm"), Gesture("fist")])) # close
        gesPool.append(GestureSequence("inv_wave", [Gesture("horiz_palm"), Gesture("side_palm")])) # prevdesk
        gesPool.append(GestureSequence("wave", [Gesture("side_palm"), Gesture("horiz_palm")])) # nextdesk
        pool = []
        for i in range(len(gesPool)):
            pool.append(SequenceActionPair(gesPool[i], Action(self.action_activation_list[i], activate=True)))
        return pool