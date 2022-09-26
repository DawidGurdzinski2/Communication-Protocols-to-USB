import tkinter as tk
from Oscilogram import *
#from WaveForm import *
#from Button import *
class Osciloscope:


    def __init__(self,window,height,width,state,quantity):
        self.state=state
        self.quantity=quantity
        self.window=window
        self.height=height
        self.width=width
        self.datain=[[0,0],[0,0]]
        self.dataout=[0]
        self.frame=tk.Frame(self.window,bg="pink",bd=5)
        tk.Grid.rowconfigure(self.window,0,weight=1)
        tk.Grid.columnconfigure(self.window,0,weight=1)
        self.frame.grid(row=0,column=0,sticky="nswe")
        self.createOscilogram(2)

    
    def createOscilogram(self,quantity):
        self.Osci=[(Oscilogram(self.frame, self.width, self.height,i,0 ,0 ))for i in range(quantity)]
        


    def UpdateData(self):
        if self.state:
            for i in range(len(self.Osci)):
                self.Osci[i].UpdateDataToArray(self.datain[i])

    def resetData(self):
        self.datain=[[0,0],[0,0]]
        self.dataout=0
        self.state=False
    