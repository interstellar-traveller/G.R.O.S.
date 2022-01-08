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
        # print(self.gestures)
        # print(self.actions)
        
    def init_gestures(self):
        """pre-initializing all gestures as default
        """
        all_gestures = list(GestureSet(0).get_all_gestures())
        # print(all_gestures)
        for gesture in all_gestures:
            self.gestures.update({gesture : Gesture(gesture)})
            
    def init_actions(self):
        """pre-initializing all actions as default
        """
        all_actions = ActionSet().get_action_list()
        for action in all_actions:
            self.actions.update({action : Action(action)})
            
    def get_gestures(self):
        """Get a dictionary of gestures

        Returns:
            dict: gesture dictionary
        """
        return self.gestures
    
    def get_actions(self):
        """Get a dictionary of actions

        Returns:
            dict: action dictionary
        """
        return self.actions
    
    def partial_action_activation(self, activation_list):
        """Provided for presets and customize setting mode.
        Partially activating the action set according to a activation list,
        unlisted actions' Activation attributes will be set to be False.

        Args:
            activation_list (list): a list of actions' names that are wished to be activated
        """
        if len(activation_list) == 0:
            for action in self.actions.keys():
                self.actions[action].update_activation_status(True)
        for action in activation_list:
            self.actions[action].update_activation_status(True)
            
    def partial_gesture_activation(self, activation_list):
        """Provided for presets and customize setting mode.
        Partially activating the gesture set according to a activation list,
        unlisted gestures' Activation attributes will be set to be False.

        Args:
            activation_list (list): a list of gestures' names that are wished to be activated
        """
        if len(activation_list) == 0:
            for gesture in self.gestures.keys():
                self.gestures[gesture].update_activation_status(True)
        for gesture in activation_list:
            self.gestures[gesture].update_activation_status(True)
    
    
    

# init = Initialize()
# print(init.get_gestures())
# print(init.get_actions())