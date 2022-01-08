import sys
sys.path.append("f:/0Desk/IBDP/ComputerScience/IA/code/GROS/src")

from gros.gesture.Gesture import Gesture
from gros.gesture.GestureSet import GestureSet
from gros.gesture.GestureSequence import GestureSequence
from gros.action.Action import Action
from gros.action.ActionSet import ActionSet
from gros.initialize.Initialize import Initialize
from gros.initialize.SequenceActionPair import SequenceActionPair

class InitializeModePPT(Initialize):
    def __init__(self) -> None:
        super().__init__()
        self.action_activation_list = ["nextpage", "prevpage", "exit", "enter"]
        self.gesture_activation_list = ["palm", "fist", "double_point", "side_palm", "horiz_palm"]
        self.partial_action_activation(self.action_activation_list)
        self.partial_gesture_activation(self.gesture_activation_list)
    
    def pairing(self):
        gesPool = []
        gesPool.append(GestureSequence("wave", [Gesture("side_palm"), Gesture("horiz_palm")])) # nextpage
        gesPool.append(GestureSequence("inv_wave", [Gesture("horiz_palm"), Gesture("side_palm")])) # prevpage
        gesPool.append(GestureSequence("grip", [Gesture("palm"), Gesture("fist")])) # exit
        gesPool.append(GestureSequence("hook", [Gesture("double_point"), Gesture("fist")])) # enter
        pool = []
        for i in range(len(gesPool)):
            pool.append(SequenceActionPair(gesPool[i], Action(self.action_activation_list[i], activate=True)))
        return pool