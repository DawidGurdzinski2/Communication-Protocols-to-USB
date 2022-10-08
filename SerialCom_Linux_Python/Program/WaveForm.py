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
        self.printDivision()
        self.fpsCount=0
        self.Fps=10
        self.numberOfWave=0
        self.signalprint=True

# fpscounter=0 i Fps=0  daje 0101  1-print 0-no print
#   
# 100 pikseli =100ms
# div =2  -> 100pikseli = 50ms

    def writeDataToArray(self,data):
        #time1=time.time()
        if(self.signaliput):
            self.dataarray.rotate(-1)
            self.dataarray[self.width-1]=data[0]
        elif (self.one==0):
            self.dataarray.rotate(-1)
            self.dataarray[self.width-1]=data[0]
            self.one+=1
        elif data[1]>0:
            self.g=(self.oldtime+data[1]*self.division)
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
        #print("arraytime: "+str(time.time()-time1))

    def printData(self):
        time1=time.time()
        if(self.fpsCount>self.Fps):
            try:
                self.canvas.delete("plot")
                for i in range(len(self.dataarray)-1):
            
                    self.canvas.create_line(i,self.dataarray[i]+(self.height/2)+1,i+1,self.dataarray[i+1]+(self.height/2)+1,fill="red",tag="plot")
            except:
                pass 
            self.fpsCount=0
        else:
           self.fpsCount+=1 
        print("printtime: "+str(time.time()-time1))

    
           

       
    def printDivision(self):
        self.numberOfdivX=20
        self.numberOfdivY=10
        XpointArray=[(self.width/self.numberOfdivX)*i for i in range(self.numberOfdivX+1)]
        YpointArray=[(self.height/self.numberOfdivY)*i for i in range(self.numberOfdivY+1)]
        
        for i in range(self.numberOfdivX+1):
            self.canvas.create_line(XpointArray[i],0,XpointArray[i],self.height,fill="white")
        for i in range(self.numberOfdivY+1):
            self.canvas.create_line(0,YpointArray[i],self.width,YpointArray[i],fill="white")