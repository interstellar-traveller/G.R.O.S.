import sys
sys.path.append("f:/0Desk/IBDP/ComputerScience/IA/code/GROS/src")

import os
from threading import Thread

def taskContainer():
    os.system('D:/Anaconda3/envs/ml/python.exe f:/0Desk/IBDP/ComputerScience/IA/code/GROS/src/gros/Container.py')

def taskGUI():
    os.system('D:/Anaconda3/envs/ml/python.exe f:/0Desk/IBDP/ComputerScience/IA/code/GROS/src/gros/gui.py')

def main():
    t1 = Thread(target=taskContainer)
    t2 = Thread(target=taskGUI)
    t1.start()
    t2.start()

if __name__ == "__main__":
    main()