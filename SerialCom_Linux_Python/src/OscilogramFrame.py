from Oscilogram import *
from tkinter import *
from Terminal import *

class OscilogramFrame:


    def __init__(self,window):
        self.window=window
        self.frame = Frame(window,bg="pink",bd=5,relief=SUNKEN)
        self.oscilogram1 =Oscilogram(self.frame,500,400,0,0,0)
        self.oscilogram2 =Oscilogram(self.frame,500,400,1,0,0)
        self.frame.grid(row=0,column=0)
        self.terminal=Terminal()

    def updateDataArray(self):
        data=self.terminal.writeDataToArray(4)
        self.oscilogram1.writeDataToArray(data[0])
        self.oscilogram2.writeDataToArray(data[1])