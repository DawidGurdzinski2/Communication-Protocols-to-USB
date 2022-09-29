import tkinter as tk
from tkinter import ttk
from Signal import *

class SignalSource:


    def __init__(self,frame,row,column):
        self.frame=tk.Frame(frame,bg="pink",bd=5)
        tk.Grid.rowconfigure(frame,0,weight=1)
        tk.Grid.columnconfigure(frame,0,weight=1)
        self.frame.grid(row=row,column=column,sticky="nswe")
        self.signal=Signal()
        self.createListoOfSignals()
        self.createButtons()
        #signal parameters
        self.Period=100
        self.signalType=0



    def sendSignal(self):
        return self.signal.generateSignal(self.Period,self.signalType)

    
    def createListoOfSignals(self):
        self.mysignal=tk.StringVar()
        self.combo=ttk.Combobox(self.frame,textvariable=self.mysignal)
        self.combo['values']=self.signal.signaltypes
        self.combo.grid(column=1,row=0)
        

    def createButtons(self):
        self.buttonSet=tk.Button(self.frame,text="Setsignal",state="normal",command=self.setSignal)
        self.buttonStart=tk.Button(self.frame,text="Startsignal",state="normal",command=self.startSignal)
        self.buttonStart.grid(row=1,column=0,sticky="nswe")
        self.buttonSet.grid(row=1,column=1,sticky="nswe")



    def setSignal(self):
        print(self.mysignal.get())
    def startSignal(self):
        print(self.mysignal.get()+"nigga")