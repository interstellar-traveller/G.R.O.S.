import sys
import cv2
import mediapipe as mp
import numpy as np

sys.path.append("f:/0Desk/IBDP/ComputerScience/IA/code/GROS/src")

from gros.gesture.Gesture import Gesture
from gros.initialize.Initialize import Initialize
from gros.initialize.initializeTest import InitializeTest
from gros.initialize.InitializeModeOS import InitializeModeOS
from gros.initialize.InitializeModeDoc import InitializeModeDoc
from gros.initialize.InitializeModePPT import InitializeModePPT
from gros.initialize.InitializeModeVD import InitializeModeVD
from nn.training.handDetector import handDetector
from nn.training.classification import Net
from gros.GrosCache import GrosCache
from utils.Errors import FuncNoResponseError
import time
import pyautogui as pg

# initialize
init_box = InitializeTest()
# print(init_box.get_gestures())

# initialize sequence-to-action pool
pool = init_box.pairing()
print(pool)

landMarkCaptured = False
gestureType = ""
gestrigger = False

# initialize Cache
cache = GrosCache(init_box.gestures, limit=3)
# TODO: test code, when finished, delete
try: # check Cache is correctly initialized
    if type(cache.get_cache()) is list and len(cache.get_cache()) == 3:
        print("Cache successfully initialized...")
        pass
    else:
        raise FuncNoResponseError("Cache initialization failed")
except FuncNoResponseError as e:
    print(e)
    sys.exit(1)

# camera stream loop (main function loop start)
# cur_stream = 0
# cap = cv2.VideoCapture(cur_stream, cv2.CAP_DSHOW)
# detector = handDetector()
cur_stream = 0
while True:
    
    cap = cv2.VideoCapture(cur_stream, cv2.CAP_DSHOW)
    detector = handDetector()
    
    stamp = time.time()
    while True:
        success, img = cap.read()
        img = detector.findHands(img, draw=True)
        lmList = detector.findPosition(img, personDraw=False)
        img = cv2.flip(img, 1)
        cv2.waitKey(100)
        
        # read interaction file and store the data pulled from the GUI
        file = open("./interact.txt", mode="r")
        data = file.readline().split(" ")
        mode = data[0]
        stream = int(data[1])
        file.close()
        
        if cur_stream != stream:
            cur_stream = stream
            cap.release()
            cv2.destroyAllWindows()
            break
        
        # # listen on a variable to end both loop and video stream
        # if cv2.waitKey(100) == 27:
        #     # modify interaction file
        #     file = open("./interact.txt", mode="w")
        #     file.write("OS 0")
        #     file.close()
        #     cv2.destroyAllWindows()
        #     sys.exit(0)

        # TODO: get this variable from the GUI
        var = mode

        currentMode = "OS"
        # TODO: Consider adding in the customize feature.
        if var != currentMode:
            # apply changes by re-initializing
            if var == "OS":
                init_box = InitializeModeOS()
            elif var == "DOC":
                init_box = InitializeModeDoc()
            elif var == "PPT":
                init_box = InitializeModePPT()
            elif var == "VD":
                init_box = InitializeModeVD()
            cache.update_gesActStatus(init_box.gestures)
            cache.reset()

        # cap = cv2.VideoCapture(stream, cv2.CAP_DSHOW)
        cv2.putText(img, "MODE " + mode +" Camera " + str(stream), (50, 75), 100, 1.2, (105,105,105), 2)
        cv2.imshow("Image", img)
        if len(lmList) != 0:
            ## nn classification
            # TODO: use real nn classification to give the correct gesture type
            # classification

            # net = Net(8,10,2)
            # gesturetype = net.use(img)
            
            # Pseudo-classification
            if cache.get_cache()[2].get_name() == "placeholder":
                gestureType = "palm"
            elif cache.get_cache()[2].get_name() == "palm":
                gestureType = "fist"
            elif cache.get_cache()[2].get_name() == "fist":
                gestureType = "palm"
            cache.update(Gesture(gestureType))
            gestureType = ""
            lmList = []
            stamp = time.time()
            gestrigger = True
        else:
            cache.update(Gesture("placeholder"))
            # TODO:
            if time.time() - stamp >= 2:
                if gestrigger:
                    pg.press("enter")
                    gestrigger = False

        # print(cache.get_cache())
        # print(cache.get_cache()[2].get_name())

        for sequence in pool:
            ## listen on cache and trigger
            if sequence.sequence_capture(cache.get_cache()):
                # print("Trigger")
                ## if sequence captured, back to loop (main loop end)
                break