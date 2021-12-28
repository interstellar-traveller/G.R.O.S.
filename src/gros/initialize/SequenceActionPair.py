import sys
sys.path.append("f:/0Desk/IBDP/ComputerScience/IA/code/GROS/src")

from gros.action.Action import Action
from gros.gesture.Gesture import Gesture
from gros.gesture.GestureSequence import *

class SequenceActionPair(object):
    def __init__(self, sequence:GestureSequence, action:Action) -> None:
        """Initialize a sequence-action pair.

        Args:
            sequence (GestureSequence): sequence of gestures
            action (Action): action
        """
        self.sequence = sequence
        self.action = action
        self.activated = action.get_activate_status()
        
    def get_sequence(self):
        """ get assigned sequence name
        """
        return self.sequence._name
    
    def get_action(self):
        """ get assigned action name
        """
        return self.action.name
    
    def sequence_capture(self, cache:list):
        """listen on the cache memory and decide whether if the sequence is captured.
        If sequence is captured, the action will be triggered.

        Args:
            cache (list): cache memory

        Returns:
            (bool): indicates whether if the sequence is captured
        """
        if self.sequence.listen_on_cache(cache):
            # print("captured")
            return self.trigger()
        # print("not captured")
        return False
    
    def trigger(self):
        """trigger the action if gesture is detected and activated
        
        Return:
            (bool): if action is successfully triggered
        """
        if self.activated:
            self.action.use()
            return True
        return False
        
    def update_action(self, new_action:Action):
        """ update assigned action
        """
        self.action = new_action
        
    def update_activation_status(self, new_status):
        """sets up the new activation status, either activated or non-activated

        Args:
            new_status (bool): new activation status
        """
        self.activated = new_status
  
# minimize = Action('minimize', True)
# sap = SequenceActionPair(
#         GestureSequence(
#             'grip', 
#             [Gesture('palm', False, 'right'), 
#              Gesture('fist', True, 'right')], 
#             position_restrict=True), 
#         minimize)
# dpalm = Gesture('palm', position='right')
# dfist = Gesture('fist', position='right')
# cache = [dfist, dpalm, dfist]
# print(sap.sequence_capture(cache))

