from Oscilogram import *
from tkinter import *
from DataModulator import *

class OscilogramFrame:


    def __init__(self,window):
        self.window=window
        self.frame = Frame(window,bg="pink",bd=5,relief=SUNKEN)
        self.oscilogram1 =Oscilogram(self.frame,500,400,0,0,0)
        self.oscilogram2 =Oscilogram(self.frame,500,400,1,0,0)
        self.frame.grid(row=0,column=0)
        
    def initOscilograms(self):
        self.datamod1=DataModulator(400,20)
        self.Amplitude1=self.datamod1.getMaxAmplitudeCOS()
        self.datamod2=DataModulator(400,500)
        self.Amplitude2=2*self.datamod2.getMaxAmplitudeCOS()

    def updateData(self):
        self.oscilogram1.UpdateDataToArray(-self.datamod1.writeData(self.Amplitude1))
        self.oscilogram2.UpdateDataToArray(-self.datamod2.writeData(self.Amplitude2))
