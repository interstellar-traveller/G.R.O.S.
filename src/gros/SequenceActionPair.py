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
        
    def get_sequence(self):
        # get assigned sequence name
        return self.sequence._name
    
    def get_action(self):
        # get assigned action name
        return self.action.name
    
    def sequence_capture(self, cache:list(Gesture)):
        """listen on the cache memory and decide whether if the sequence is captured.
        If sequence is captured, the action will be triggered.

        Args:
            cache (list): cache memory

        Returns:
            (bool): indicates whether if the sequence is captured
        """
        if self.sequence.listen_on_cache(cache):
            self.trigger()
            return True
        return False
    
    def trigger(self):
        # triggers the action
        self.action.use()
        
    def update_action(self, new_action:Action):
        # update assigned action
        self.action = new_action