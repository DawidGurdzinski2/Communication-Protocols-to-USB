from tkinter import *
from collections import deque
class WaveForm:


    def __init__(self,canvas,width,height,dataformat):
        self.canvas=canvas
        self.width=width
        self.height=height
        self.dataformat=dataformat
        canvas.create_line(0,0,200,200,fill="red",width=5)
        #dataarray= [[0 for i in range(3)] for j in range(6)]    #[[0,0,0],[0,0,0]....] 
        self.dataarray= [0 for i in range(width)]
        self.dataarray= deque(self.dataarray)
        
        
    def writeDataToArray(self,data):
        self.dataarray.rotate(-1)
        self.dataarray[self.width-1]=data
        print(self.dataarray)



