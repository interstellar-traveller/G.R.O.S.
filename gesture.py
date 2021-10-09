import math

class gesture(object):
    def __init__(self, lmlist):
        self.lmlist = lmlist
        self.statusCache = [0, 0, 0, 0]

    def distance(self, x1,y1,x2,y2,z1,z2):
        return math.sqrt(((x1-x2)**2+(y1-y2)**2)+(z1-z2)**2)

    