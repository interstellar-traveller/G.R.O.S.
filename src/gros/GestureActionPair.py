from gros.gesture.Gesture import *
from gros.action.Action import *

class GestureActionPair():
    def __init__(self, gesture:Gesture, action:Action):
        self.gesture = gesture
        self.action = action
        
    def get_gesture(self):
        return self.gesture.name
    
    def get_action(self):
        return self.action.name
        
    def trigger(self):
        if self.gesture.detected:
            self.action.use()
    
    def update_action(self, action:Action):
        self.action = action


# palm = Gesture('palm')
# switch = Action('switch') 
# gap = GestureActionPair(palm, switch)
# palm.update_detected()
# gap.trigger()