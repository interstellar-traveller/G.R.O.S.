import gesture.gestureSet as gestureSet
from hand.finger import finger


class hand(object):

    def __init__(self, id, lmlist):
        self.id = id
        self.lms = lmlist
        self.gestureSet = gestureSet(self.id, True)
        
    def wrist(self):
        return self.lms[0]

    def fingerlms(self):
        self.thumblms = self.lms[1:5]
        self.indexlms = self.lms[5:9]
        self.middlelms = self.lms[9:13]
        self.ringlms = self.lms[13:17]
        self.littlelms = self.lms[17:21]

    def init_fingers(self):
        self.thumb = finger("thumb", self.thumblms)
        self.index = finger("index", self.indexlms)
        self.middle = finger("middle", self.middlelms)
        self.ring = finger("ring", self.ringlms)
        self.little = finger("little", self.little)
    