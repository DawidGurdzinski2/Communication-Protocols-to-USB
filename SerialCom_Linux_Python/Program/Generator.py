import tkinter as tk
from tkinter import ttk
from SignalSource import *

class Generator:


    def __init__(self,window,state):
        self.state=state
        
        self.dataout=[[0,0],[0,0]]

        self.window=window
        self.frame=tk.Frame(self.window,bg="pink",bd=5)
        tk.Grid.rowconfigure(self.window,0,weight=1)
        tk.Grid.columnconfigure(self.window,0,weight=1)
        self.frame.grid(row=0,column=0,sticky="nswe")

        self.numberOfSources=2
        self.createSourceSignal(self.numberOfSources)
        self.createButton()

    def createButton(self):
        self.addbutton=tk.Button(self.frame,text="AddSource",state="normal",command=self.addSiganlSource)
        self.addbutton.grid(row=0)

    def addSiganlSource(self):
        self.dataout.append([0,0])
        self.signalSources.append(SignalSource(self.frame,self.numberOfSources+1, 0))
        self.numberOfSources+=1
        


    def createSourceSignal(self,quantity):
        self.signalSources=[(SignalSource(self.frame, i+1,0 ))for i in range(quantity)]

    def UpdateData(self):
        if self.state:
            self.sendSignal()

    def sendSignal(self):
        try:
            for i in range(self.numberOfSources):
                data=self.signalSources[i].sendSignal()
                self.dataout[i]=[data[0],data[1]]
            
        except:
            pass

    def resetData(self):
        
        self.dataout=[[0,0],[0,0]]
        self.state=False
    