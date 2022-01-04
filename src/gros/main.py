import sys
import cv2
import mediapipe as mp
import numpy as np

sys.path.append("f:/0Desk/IBDP/ComputerScience/IA/code/GROS/src")

from gros.gesture.Gesture import Gesture
from gros.initialize.Initialize import Initialize
from gros.initialize.initializeTest import InitializeTest
from nn.training.handDetector import handDetector
from gros.GrosCache import GrosCache
from utils.Errors import FuncNoResponseError

# MAIN
if __name__ == "__main__":
    
    # initialize
    init_box = InitializeTest()
    print(init_box.get_gestures())
    
    # initialize sequence-to-action pool
    pool = init_box.pairing()
    print(pool)
    
    landMarkCaptured = False
    gestureDetected = False
    gestureType = ""
    
    # initialize Cache
    cache = GrosCache(limit=3)
    # TODO: test code, when finished, delete
    try: # check Cache is correctly initialized
        if type(cache.get_cache()) is list and len(cache.get_cache()) == 0:
            print("Cache successfully initialized...")
            pass
        else:
            raise FuncNoResponseError("Cache initialization failed")
    except FuncNoResponseError as e:
        print(e)
        sys.exit(1)
        
    # camera stream loop (main function loop start)
    cap = cv2.VideoCapture(0)
    detector = handDetector()
    while True:
        if cv2.waitKey(1) == 27:
            cv2.destroyAllWindows()
            break
        
        setting = False
        # check if customize settings
        buttonSetPressed = True
        if buttonSetPressed:
            setting = True
            
        if setting:
            # rechoosing gesture/sequence-action pairs
            
            # close customize setting mode
            setting = False
            # apply changes by re-initializing
        
        success, img = cap.read()
        img = detector.findHands(img, draw=True)
        lmList = detector.findPosition(img, personDraw=False)
        if len(lmList) != 0:
            landMarkCaptured = True
        
        ## nn classification
        # TODO: use real nn classification to give the correct gesture type
        if landMarkCaptured:
            # classification
            gestureType = "grip"
            if len(gestureType) > 0:
                gestureDetected = True

        cache.update(Gesture(gestureType))


            ## listen on cache and trigger




            ## back to loop (main loop end)



        # listen on a variable to end both loop and video stream



 