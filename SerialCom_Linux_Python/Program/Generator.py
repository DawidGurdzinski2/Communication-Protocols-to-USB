import tkinter as tk
from tkinter import ttk
from SignalSource import *

class Generator:


    def __init__(self,window,state):
        self.state=state
        self.dataout=[[0,0]]
        self.window=window
        self.createScrollBar()
        self.numberOfSources=0
        self.createSourceSignal(self.numberOfSources)
        self.createButton()

    def createScrollBar(self):
        self.scrollframe=tk.Frame(self.window,bg="grey",bd=5)
        tk.Grid.rowconfigure(self.window,0,weight=1)
        tk.Grid.columnconfigure(self.window,0,weight=1)
        self.scrollframe.grid(row=0,column=0,sticky="nswe")
        self.canvas=tk.Canvas(self.scrollframe,bg="grey")
        self.canvas.pack(side="left",fill="both",expand=1)
        self.scrollbar=ttk.Scrollbar(self.scrollframe,orient="vertical",command=self.canvas.yview)
        self.scrollbar.pack(side="right",fill="y")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind('<Configure>',lambda e:self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.frame=tk.Frame(self.canvas,bg="grey",bd=5)
        self.canvas.create_window((0,0),window=self.frame ,anchor="nw")

    def UpdateDataScrollbar(self):
        self.canvas.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

    def createButton(self):
        self.addbutton=tk.Button(self.frame,text="AddSource",state="normal",command=self.addSiganlSource)
        self.addbutton.grid(row=0)

    def addSiganlSource(self):
        self.dataout.append([0,0])
        self.signalSources.append(SignalSource(self.frame,2*self.numberOfSources+2, 0))
        self.numberOfSources+=1
        self.Labels.append(tk.Label(self.frame,text="Signal Source"+str(self.numberOfSources),bg="grey",font=('Arial',15,'bold')))
        self.Labels[self.numberOfSources-1].grid(row=1+(self.numberOfSources-1)*2)
        self.UpdateDataScrollbar()

        self.UpdateDataScrollbar()


    def createSourceSignal(self,quantity):
        self.signalSources=[(SignalSource(self.frame, i+1,0 ))for i in range(quantity)]
        self.Labels=[tk.Label(self.grame,text="Signal Source"+str(i+1))for i in range(quantity)]

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
        
        self.dataout=[[0,0]]
        self.state=False
    