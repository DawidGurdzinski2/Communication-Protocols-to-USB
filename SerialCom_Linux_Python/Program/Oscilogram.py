from tkinter import *
from WaveForm import *
import math 
class Oscilogram:


    def __init__(self,frame,WIDTH,HEIGHT,ROW,COLUMN,dataformat):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.frame=frame
        self.ROW=ROW
        self.COLUMN=COLUMN
        self.buttonsStates=[True,True,True,True]
        self.dataformat=dataformat
        canvas = Canvas(frame,width=WIDTH,height=HEIGHT)
        self.wave=WaveForm(canvas,WIDTH,HEIGHT,dataformat)
        canvas.grid(row=ROW,column=COLUMN)
        self.previousdData=0
        self.division=0

    def UpdateDataToArray(self,data):
        self.wave.division=self.division
        self.wave.signaliput=self.buttonsStates
        self.wave.writeDataToArray([self.adjustData(data[0]),data[1]])
        self.wave.printData()
    
    def adjustData(self,data):
        if(abs(data)>=abs(self.previousdData)):
            self.previousdData=abs(data)
        if(self.previousdData==0):
            return 0
        else:
            return math.floor(data*self.HEIGHT/(2*self.previousdData))
    
    