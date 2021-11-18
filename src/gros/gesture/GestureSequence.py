from gros.gesture.Gesture import Gesture

class GestureSequence(object):
    def __init__(self, name:str, gestureSequence:list(Gesture), activate=True):
        """Initialize a gesture sequence that listens on the cache memory of gestures

        Args:
            name (str): the name of the gesture sequence
            gestureSequence (list): a list of gesture that forms the gesture sequence
            activate (bool, optional): the activation status. Defaults to True.
        """
        self._name = name
        self._gestureSequence = gestureSequence
        self._status = activate
        self.detected = False
        
    def get_name(self):
        # get name of the gesture
        return self._name
    
    def get_activation_status(self):
        # get the name of the activation status
        return self._status
        
    def listen_on_cache(self, cache:list(Gesture)):
        """listen on the cache memory, sequence is detected, then return True

        Args:
            cache (list): a copy of the cache memory

        Returns:
            (bool): indicator of whether if the sequence is detected
        """
        cache_comp = self.cache[-len(self._gestureSequence):-1]
        for i in range(len(cache_comp)):
            if cache_comp[i].get_name() == self._gestureSequence[i].get_name():
                if cache_comp[i].get_position == self._gestureSequence[i].get_position():
                    pass
                else:
                    return False
            else:
                return False
        return True
