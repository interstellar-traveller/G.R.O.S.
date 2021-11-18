class Gesture():
    def __init__(self, name, position='', activate=True):
        self._name = name
        self._status = activate
        self._position = position
        self.detected = False
        
    def get_name(self):
        return self._name
    
    def get_activation_status(self):
        return self._status
    
    def get_position(self):
        return self._position

    def detected(self):
        self.detected = True
        
    def undetected(self):
        self.detected = False
    
# palm = Gesture("palm")
# print(palm.get_activation_status())