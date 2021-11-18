from gros.gesture.Gesture import Gesture

class GestureSequence(object):
    def __init__(self, name:str, gestureSequence:list, activate=True):
        self._name = name
        self._gestureSequence = gestureSequence
        self._status = activate
        
    def _listen_on_cache(self, cache:list):
        self.cache = cache
        
    