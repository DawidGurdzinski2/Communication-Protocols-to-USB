from tkinter import *
from collections import deque
import time

class WaveForm:


    def __init__(self,canvas,width,height,dataformat):
        self.canvas=canvas
        self.width=width
        self.height=height
        self.dataformat=dataformat
        self.dataarray= [0 for i in range(width)]
        self.dataarray= deque(self.dataarray)
        
        
        
    def writeDataToArray(self,data):
        self.dataarray.rotate(-1)
        self.dataarray[self.width-1]=data
        
        
    def printData(self):
        try:
            self.canvas.delete("all")
            for i in range(len(self.dataarray)-1):
            
                self.canvas.create_line(i,self.dataarray[i]+(self.height/2),i+1,self.dataarray[i+1]+(self.height/2),fill="red")
        except:
            pass   
            
       




