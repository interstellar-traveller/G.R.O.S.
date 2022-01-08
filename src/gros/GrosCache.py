from gros.gesture.Gesture import *

class GrosCache(object):
    def __init__(self, gestureActivationStatus:dict, limit:int=3) -> None:
        """Maintains a cache that stores a sequence of gestures detected

        Args:
            limit (int, optional): The limit length of the cache list. Defaults to 3.
        """
        self._cache = [Gesture("placeholder"), Gesture("placeholder"), Gesture("placeholder")]
        self.gesActStatus = gestureActivationStatus
        self._limit = limit
        self.placeHoldThreshhold = 2
        self.buffer = 0
        
    def update_gesActStatus(self, new_gestureActivationStatus:dict):
        """update the gesture activation status dictionary when mode changes

        Args:
            new_gestureActivationStatus (dict(Gesture)): 
            the new gesture activation status dictionary from the initialization box
        """
        self.gesActStatus = new_gestureActivationStatus
        
    def reset(self):
        """reset the cache memory when mode changes
        """
        self._cache = [Gesture("placeholder"), Gesture("placeholder"), Gesture("placeholder")]
        
    def get_cache(self):
        """get current cache list

        Returns:
            [Gesture]: the cache list
        """
        return self._cache
    
    def get_limit(self):
        """get current cache list limit length

        Returns:
            (int): the current length limit
        """
        return self._limit
    
    def limit_restrict(self):
        """Pop out the first item when the cache list reaches its upper limit
        """
        if len(self._cache) > self._limit:
            self._cache.pop(0)
    
    def update_limit(self, new_limit):
        """update the cache length limit

        Args:
            new_limit (int): the new limit
        """
        self._limit = new_limit
            
    def update_permit(self, prev:Gesture, curr:Gesture):
        """check if the new gesture detected is exactly the same as the previous one.
        If so, reject the update.

        Args:
            prev (Gesture): the last gesture stored in the cache
            curr (Gesture): the gesture to be updated into the cache

        Returns:
            (bool): True or False condition
        """
        if prev.get_name() == curr.get_name() and prev.get_position() == curr.get_position():
            return False
        else:
            return True
            
    def update(self, new_ges:Gesture):
        """update the cache memory

        Args:
            new_ges (Gesture): the newly detected gesture
        """
        if self.update_permit(self._cache[self._limit-1], new_ges):
            self._cache.append(new_ges)
            self.limit_restrict()