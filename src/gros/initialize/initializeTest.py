import sys
sys.path.append("f:/0Desk/IBDP/ComputerScience/IA/code/GROS/src")

from gros.gesture.Gesture import Gesture
from gros.gesture.GestureSet import GestureSet
from gros.gesture.GestureSequence import GestureSequence
from gros.action.Action import Action
from gros.action.ActionSet import ActionSet
from gros.initialize.Initialize import Initialize
from gros.initialize.SequenceActionPair import SequenceActionPair

class InitializeTest(Initialize):
    def __init__(self) -> None:
        super().__init__()
        self.action_activation_list = ["showDesktop", "switch"]
        self.gesture_activation_list = ["palm", "fist", "side_palm", "horiz_palm"]
        self.partial_action_activation(self.action_activation_list)
        self.partial_gesture_activation(self.gesture_activation_list)
    
    def pairing(self):
        gesPool = []
        gesPool.append(GestureSequence("grip", ["palm", "fist"]))
        gesPool.append(GestureSequence("swip", ["side_palm", "horiz_palm"]))
        pool = []
        for i in range(len(gesPool)):
            pool.append(SequenceActionPair(gesPool[i], Action(self.action_activation_list[i], activate=True)))
        return pool
    
init_box = InitializeTest()
print(init_box.pairing)