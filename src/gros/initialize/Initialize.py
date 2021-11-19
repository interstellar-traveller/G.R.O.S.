import sys
sys.path.append("f:/0Desk/IBDP/ComputerScience/IA/code/GROS/src")

from gros.gesture.Gesture import Gesture
from gros.gesture.GestureSet import GestureSet
from gros.gesture.GestureSequence import GestureSequence
from gros.action.Action import Action
from gros.action.ActionSet import ActionSet

class Initialize(object):
    def __init__(self) -> None:
        """initialize gesture set and action set
        """
        self.action_activation_list = []
        self.gesture_activation_list = []
        self.gestures = {}
        self.init_gestures()
        self.actions = {}
        self.init_actions()
        
    def init_gestures(self):
        all_gestures = GestureSet(0).get_all_gestures()
        for gesture in all_gestures:
            self.gestures.update({gesture : Gesture(gesture)})
            
    def init_actions(self):
        all_actions = ActionSet().get_action_list()
        for action in all_actions:
            self.actions.update({action : Action(action)})
            
    def get_gestures(self):
        return self.gestures
    
    def get_actions(self):
        return self.actions
    
    def partial_action_activation(self, activation_list):
        if len(self.action_activation_list) == 0:
            for action in self.actions.keys():
                self.actions[action].update_activation_status(True)
        for action in self.action_activation_list:
            self.actions[action].update_activation_status(True)
            
    def partial_gesture_activation(self, activation_list):
        if len(self.gesture_activation_list) == 0:
            for gesture in self.gestures.keys():
                self.gestures[gesture].update_activation_status(True)
        for gesture in self.gesture_activation_list:
            self.gestures[gesture].update_activation_status(True)
    
    
    

# init = Initialize()
# print(init.get_gestures())
# print(init.get_actions())