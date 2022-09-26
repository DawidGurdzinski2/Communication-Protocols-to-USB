import tkinter as tk
from Signal import *

class Generator:


    def __init__(self,window,height,width,state):
        self.state=state
        self.window=window
        self.height=height
        self.width=width
        self.datain=[0]
        self.dataout=[[0,0],[0,0]]
        self.frame=tk.Frame(self.window,bg="pink",bd=5)
        tk.Grid.rowconfigure(self.window,0,weight=1)
        tk.Grid.columnconfigure(self.window,0,weight=1)
        self.frame.grid(row=0,column=0,sticky="nswe")
        self.createSourceSignal(2)
        self.Period=[100,1000]
        self.signalType=[0,0]

    def createSourceSignal(self,quantity):
        self.signalSource=[(Signal())for i in range(quantity)]
    
    def UpdateData(self):
        if self.state:
            self.sendSignal()

    def sendSignal(self):
        for i in range(len(self.dataout)):
            self.dataout[i]=self.signalSource[i].generateSignal(self.Period[i],self.signalType[i])

    def resetData(self):
        self.datain=0
        self.dataout=[[0,0],[0,0]]
        self.state=False
    