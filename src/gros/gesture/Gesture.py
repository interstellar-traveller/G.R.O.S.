class Gesture():
    def __init__(self, name, activate:bool=False, position='') -> None:
        """Initialize a single gesture.
        If a single gesture needs to be detected, then this class will be used.

        Args:
            name (str): name of the gesture
            activate (bool, optional): the activation status. Defaults to True.
            position (str, optional): the position of the gesture captured by the camera. Defaults to ''.
        """
        self._name = name
        self._activated = activate
        self._position = position
      
    def get_name(self) -> str:
        """ get the name of the gesture
        """
        return self._name
    
    def get_activation_status(self) -> bool:
        """ get the activation status
        """
        return self._activated
    
    def get_position(self) -> str:
        """ get the position fot the gesture
        """
        return self._position
    
    def update_position(self, new_position) -> None:
        """ set new gesture position
        """
        self._position = new_position
        
    def update_activation_status(self, new_status):
        self._activated = new_status
    
# palm = Gesture("palm")
# print(palm.get_activation_status())