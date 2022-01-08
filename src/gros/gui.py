import os
import sys
from tkinter import *
from tkinter.font import BOLD
from tkinter import ttk
from tkinter import scrolledtext
from PIL import ImageTk, Image
from cv2 import invert

class GUI():
    def __init__(self):
        self.log = ["Start logging...\n"]
        self.win = Tk()
        self.win.title('GROS')
        photo = PhotoImage(file="f:/0Desk/IBDP/ComputerScience/IA/code/GROS/src/gros/img\icon.png")
        self.win.iconphoto(False, photo)
        self.screenwidth = self.win.winfo_screenwidth()
        self.screenheight = self.win.winfo_screenheight()
        self.framewidth = 300
        self.frameheight = 630
        size = "%dx%d+%d+%d" % (self.framewidth, self.frameheight, (self.screenwidth - self.framewidth) / 2, (self.screenheight - self.frameheight) / 2.5)
        self.win.geometry(size)
        self.win.resizable(width=False, height=False)
        self.win.configure(bg='#b0b1b1')
        
        self.mode = StringVar()
        self.camera = StringVar()
    
    def configure(self):
        
        def push_mode():
            if len(self.mode.get()) != 0:
                self.log.insert(0, "Reset mode to " + self.mode.get() + ".\n")
            else:
                self.log.insert(0, "Mode not specified. Null reset.\n")
            label_log.insert(1.0, self.log[0])
            # modify interaction file
            file = open("./interact.txt", mode="r")
            data = file.readline().split(" ")
            data[0] = self.mode.get()
            file = open("./interact.txt", mode="w")
            file.write(' '.join(data))
            file.close()

        def push_camera(event):
            self.log.insert(0, "Set camera stream to camera at slot " + str(self.streams.get()) + ".\n")
            label_log.insert(1.0, self.log[0])
            # modify interaction file
            file = open("./interact.txt", mode="r")
            data = file.readline().split(" ")
            data[1] = str(self.streams.get())
            file = open("./interact.txt", mode="w")
            file.write(' '.join(data))
            file.close()
            
        
        resetbtn = Button(self.win,
                          text='Reset Mode',
                          width=29,
                          fg='white',
                          bg='#eea242',
                          font=('Microsoft YaHei', 12, BOLD),
                          relief=GROOVE,
                          activebackground='#b0b1b2',
                          activeforeground="grey",
                          command=push_mode)
        resetbtn.place(x=0, y=264)

        def print_selection():
            label.config(text=self.mode.get() + ' mode selected. \nClick RESET MODE to apply changes.')

        

        label = Label(self.win, 
                      bg='#eea242', 
                      width=30, 
                      height=3,
                      font=('Microsoft YaHei', 12),
                      text='Selecte a mode to activate.',
                      justify=CENTER)
        label.place(x=0, y=0)

        r1 = Radiobutton(self.win, 
                         width=34,
                         height=2,
                         bg='#b0b1b1',
                         font=('Microsoft YaHei', 10, BOLD),
                         text='Option A: OS mode',
                         variable=self.mode, value='OS',
                         command=print_selection,
                         relief=GROOVE,
                         anchor="w")
        r1.place(x=0, y=69)

        r2 = Radiobutton(self.win, 
                         width=34,
                         height=2,
                         bg='#b0b1b1',
                         font=('Microsoft YaHei', 10, BOLD),
                         text='Option B: DOC mode',
                         variable=self.mode, value='DOC',
                         command=print_selection,
                         relief=GROOVE,
                         anchor="w")
        r2.place(x=0, y=118)

        r3 = Radiobutton(self.win, 
                         width=34,
                         height=2,
                         bg='#b0b1b1',
                         font=('Microsoft YaHei', 10, BOLD),
                         text='Option C: Power Point mode',
                         variable=self.mode, value='PPT',
                         command=print_selection,
                         relief=GROOVE,
                         anchor="w")
        r3.place(x=0, y=167)

        r4 = Radiobutton(self.win, 
                         width=34,
                         height=2,
                         bg='#b0b1b1',
                         font=('Microsoft YaHei', 10, BOLD),
                         text='Option D: Virtual Desktop mode',
                         variable=self.mode, value='VD',
                         command=print_selection,
                         relief=GROOVE,
                         anchor="w")
        r4.place(x=0, y=216)

        label_camera = Label(self.win, 
                      bg='#b0b1b1',
                      fg="black",
                      width=37, 
                      height=2,
                      font=('Microsoft YaHei', 10),
                      text='Selected the camera stream in the droplist \nbelow that you will use as the input.',
                      justify=CENTER)
        label_camera.place(x=0, y=305)

        label_log = scrolledtext.ScrolledText(self.win,
                      bg='white',
                      fg="black",
                      width=32, 
                      height=9,
                      font=('Microsoft YaHei', 10))
        label_log.place(x=11, y=400)

        label_log.insert(1.0, "".join(self.log))

        def clearlog():
            label_log.delete(1.0, END)
            self.log = ["Logger cleared. Restart logging...\n"]
            label_log.insert("insert", self.log[0])

        resetbtn = Button(self.win,
                          text='Clear logger',
                          width=29,
                          fg='white',
                          bg='#eea242',
                          font=('Microsoft YaHei', 12, BOLD),
                          relief=GROOVE,
                          activebackground='#b0b1b2',
                          activeforeground="grey",
                          command=clearlog)
        resetbtn.place(x=0, y=590)

        label_camera = Label(self.win, 
                      bg='#b0b1b1',
                      fg="black",
                      width=15, 
                      height=1,
                      font=('Microsoft YaHei', 10),
                      text='Camera Stream ',
                      justify=LEFT,
                      anchor="w")
        label_camera.place(x=50, y=358)

        self.streams = ttk.Combobox(self.win, 
                               textvariable=self.camera.get(),
                               width=10
                               )
        self.streams.place(x=155, y=360)
        self.streams["value"] = (0, 1)
        self.streams.current(0)

        self.streams.bind("<<ComboboxSelected>>", push_camera)
    
    def GUImain(self):
        self.configure()
        self.win.mainloop()
        
gui = GUI()
gui.GUImain()
# restore interaction file
file = open("./interact.txt", mode="w")
file.write("OS 0")
file.close()
os.system("taskkill /F /IM python.exe")