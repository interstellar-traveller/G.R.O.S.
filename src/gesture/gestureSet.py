import inspect

class gestureSet(object):
    def __init__(self, handid:int, activateAll:bool=True, activationlist:list=[]) -> None:
        """Initilization of the a new gesture set

        Args:
            handid (int): defines the hand that this gestureSet will apply to
            activateAll (bool, optional): Determines if all gestures are activated. Defaults to True.
            activationlist (list, optional): Customizable gesture activation list. Defaults to [].
        """
        self.id = handid
        self.activateAll = activateAll
        self.activationlist = activationlist

    def initgestureSet(self):
        """Get all the gesture functions by inpecting this class

        Returns:
            gestures_activation (dict): a dictionary that returns all the gestures' activation status
        """
        gestures_activation = {}
        all_funcs = inspect.getmembers(gestureSet, inspect.ismethod)
        gesture_funcs = []
        for func in all_funcs:
            if str(list(func)[0])[0:4] == "ges_":
                gesture_funcs.append(str(list(func)[0]))
        for func in gesture_funcs:
            gestures_activation[func] = False
        return gestures_activation

    def customize_activation(self):
        """Customize the gesture set by activating all the required gestures

        Returns:
            gestures (dict): a dictionary with all required gestures value set to be true
        """
        gestures = self.initgestureSet()
        if self.activateAll:
            for func in gestures.keys():
                gestures[func]=True
        else:
            for func in self.activationlist:
                gestures[func]=True
        return gestures
        

    