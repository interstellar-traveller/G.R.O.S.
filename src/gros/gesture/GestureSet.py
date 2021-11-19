import inspect

class GestureSet(object):
    def __init__(self, handid:int, activationlist:list=[]) -> None:
        """Initilization of the a new gesture set.
        If under default condition, all gestures will be activated.
        If not, then only chosen gestures will be activated, thus this gestures can be paired with actions.
        All gestures are stored in the dictionary: self.gestures

        Args:
            handid (int): defines the hand that this gestureSet will apply to
            activationlist (list, optional): Customizable gesture activation list. Defaults to [].
        """
        self.id = handid
        if activationlist == []:
            self.activateAll = True
        else:
            self.activateAll = False
        self.activationlist = activationlist
        self.gestures = self._initGestureSet()
        self._customize_activation()

    def _initGestureSet(self):
        """Get all the gesture functions by inpecting this class

        Returns:
            gestures_activation (dict): a dictionary that returns all the gestures' activation status
        """
        self.gestures_activation = {}
        all_funcs = inspect.getmembers(GestureSet, inspect.isfunction)
        gesture_funcs = []
        print(all_funcs)
        for index in range(len(all_funcs)):
            if str(list(all_funcs[index])[0]) not in ["__init__","_initGestureSet","_customize_activation","get_all_gestures","update_gesture_activation_status"]:
                gesture_funcs.append(str(list(all_funcs[index])[0]))
        for func in gesture_funcs:
            self.gestures_activation[func] = False
        return self.gestures_activation

    def _customize_activation(self):
        """Customize the gesture set by activating all the required gestures
        """
        if self.activateAll:
            for func in self.gestures.keys():
                self.gestures[func]=True
        else:
            for func in self.activationlist:
                self.gestures[func]=True
    
    def get_all_gestures(self):
        """get all the gestures defined name

        Returns:
            gestures.keys (list(str)): all the gesture names
        """
        return self.gestures.keys()
    
    def update_gesture_activation_status(self, new_activation_list):
        """update the gestures' activation status base on the new activation list

        Args:
            new_activation_list (list(str)): new activation list
        """
        self.activationlist = new_activation_list
        self._customize_activation()

    def palm(self):
        # palm: all five fingers are straight
        status = self.gestures["palm"]
        return status
    
    def side_palm(self):
        status = self.gestures["side_palm"]
        return status
    
    def horiz_palm(self):
        status = self.gestures["horiz_palm"]
        return status
    
    def fist(self):
        # fist: all five fingers cruched
        status = self.gestures["fist"]
        return status
    
    def side_fist(self):
        status = self.gestures["side_fist"]
        return status
    
    def point(self):
        status = self.gestures["point"]
        return status
    
    def double_point(self):
        status = self.gestures["double_point"]
        
        return status
    
# ges = GestureSet(0)
# print(ges.gestures)