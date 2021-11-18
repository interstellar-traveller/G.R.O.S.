class Gesture():
    def __init__(self, name, position='', activate=True):
        """Initialize a single gesture.
        If a single gesture needs to be detected, then this class will be used.

        Args:
            name (str): name of the gesture
            position (str, optional): the position of the gesture captured by the camera. Defaults to ''.
            activate (bool, optional): the activation status. Defaults to True.
        """
        self._name = name
        self._status = activate
        self._position = position
        
    def get_name(self):
        # get name of the gesture
        return self._name
    
    def get_activation_status(self):
        # get the name of the activation status
        return self._status
    
    def get_position(self):
        # get the position fot he gesture
        return self._position
    
# palm = Gesture("palm")
# print(palm.get_activation_status())