from gros.gesture.Gesture import *
from gros.action.Action import *

class GestureActionPair():
    def __init__(self, gesture:Gesture, action:Action):
        """Initialize a gesture-action pair

        Args:
            gesture (Gesture): gesture
            action (Action): action
        """
        self.gesture = gesture
        self.action = action
        
    def get_gesture(self):
        # get assigned gesture name
        return self.gesture.name
    
    def get_action(self):
        # get assigned action name
        return self.action.name
    
    def gesture_capture(self, cache:list(Gesture)):
        if cache[-1] == self.get_gesture():
            self.trigger()
        
    def trigger(self):
        # trigger the action if gesture is detected
        self.action.use()
    
    def update_action(self, new_action:Action):
        # update assigned action
        self.action = new_action


# palm = Gesture('palm')
# switch = Action('switch') 
# gap = GestureActionPair(palm, switch)
# palm.update_detected()
# gap.trigger()