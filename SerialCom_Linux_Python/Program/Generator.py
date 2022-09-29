import tkinter as tk
from tkinter import ttk
from SignalSource import *

class Generator:


    def __init__(self,window,height,width,state):
        self.state=state
        self.datain=[0]
        self.dataout=[[0,0,0,0],[0,0,0,0]]

        self.window=window
        self.frame=tk.Frame(self.window,bg="pink",bd=5)
        tk.Grid.rowconfigure(self.window,0,weight=1)
        tk.Grid.columnconfigure(self.window,0,weight=1)
        self.frame.grid(row=0,column=0,sticky="nswe")

        self.numberOfSources=2
        self.createSourceSignal(2)

        


    def createSourceSignal(self,quantity):
        self.signalSources=[(SignalSource(self.frame, i,0 ))for i in range(quantity)]

    def UpdateData(self):
        if self.state:
            self.sendSignal()

    def sendSignal(self):
        for i in range(self.numberOfSources):
            data=self.signalSources[i].sendSignal()
            self.dataout[i]=[data[0],data[1],0,i]


    def resetData(self):
        self.datain=0
        self.dataout=[[0,0],[0,0]]
        self.state=False
    