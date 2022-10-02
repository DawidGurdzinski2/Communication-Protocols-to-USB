from tkinter import *
from collections import deque
import time
import math
import numpy as np

class WaveForm:


    def __init__(self,canvas,width,height):
        self.canvas=canvas
        self.width=width
        self.signaliput=True
        self.height=height
        self.dataarray= [0 for i in range(width)]
        self.dataarray= deque(self.dataarray)
        self.oldtime=0
        self.one=0
        self.division=1

# 100 pikseli =100ms
# div =2  -> 100pikseli = 50ms

    def writeDataToArray(self,data):
        if(self.signaliput):
            self.dataarray.rotate(-1)
            self.dataarray[self.width-1]=data[0]
        elif (self.one==0):
            self.dataarray.rotate(-1)
            self.dataarray[self.width-1]=data[0]
            self.one+=1
        elif data[1]>0:
            self.g=(self.oldtime+data[1])*self.division
            if(self.g>=1):
                
                if(math.floor(self.g)<2):
                    x=[data[0]]
                else:
                    x=np.linspace(self.dataarray[self.width-1],data[0],math.floor(self.g))
            
                for i in x:    
                    self.dataarray.rotate(-1)
                    self.dataarray[self.width-1]=i
            self.g=self.g-math.floor(self.g)
            self.oldtime=self.g

        
    def printData(self):
        try:
            self.canvas.delete("all")
            for i in range(len(self.dataarray)-1):
            
                self.canvas.create_line(i,self.dataarray[i]+(self.height/2),i+1,self.dataarray[i+1]+(self.height/2),fill="red")
        except:
            pass   
            
       




