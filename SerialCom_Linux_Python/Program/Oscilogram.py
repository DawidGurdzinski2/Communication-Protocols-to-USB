from tkinter import *
from WaveForm import *
import math 
class Oscilogram:


    def __init__(self,frame,width,height,row,column):
        self.width = width
        self.height = height
        self.frame=frame
        self.row=row
        self.column=column
        self.buttonsStates=[True,True,True,True]
        canvas = Canvas(frame,width=width,height=height+4)
        self.wave=WaveForm(canvas,width,height)
        canvas.grid(row=row,column=column)
        self.previousdData=0
        self.division=1

    def UpdateDataToArray(self,data):
        self.wave.division=self.division
        self.wave.signaliput=self.buttonsStates[1]
        self.wave.writeDataToArray([self.adjustData(data[0]),data[1]])
        self.wave.printData()
    
    def adjustData(self,data):
        if(abs(data)>=abs(self.previousdData)):
            self.previousdData=abs(data)
        if(self.previousdData==0):
            return 0
        else:
            return math.floor(data*self.height/(2*self.previousdData))
    
    