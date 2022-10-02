import tkinter as tk
from Oscilogram import *
from tkinter import ttk
#from WaveForm import *
#from Button import *
class Osciloscope:


    def __init__(self,window,height,width,state,quantity):
        self.state=state
        self.quantity=quantity
        self.window=window
        
        self.height=height
        self.width=width
        self.datain=[[[0,0],[0,0]],[[0,0],[0,0]],[[0,0],[0,0]]]
        self.createScrollBar()
        
    

        self.numberOfOscilograms=0
        self.createOscilogram(self.numberOfOscilograms)
        self.createButton()


    def createScrollBar(self):
        self.scrollframe=tk.Frame(self.window,bg="pink",bd=5)
        tk.Grid.rowconfigure(self.window,0,weight=1)
        tk.Grid.columnconfigure(self.window,0,weight=1)
        self.scrollframe.grid(row=0,column=0,sticky="nswe")
        self.canvas=tk.Canvas(self.scrollframe)
        self.canvas.pack(side="left",fill="both",expand=1)
        self.scrollbar=ttk.Scrollbar(self.scrollframe,orient="vertical",command=self.canvas.yview)
        self.scrollbar.pack(side="right",fill="y")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind('<Configure>',lambda e:self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.frame=tk.Frame(self.canvas,bg="pink",bd=5)
        self.canvas.create_window((0,0),window=self.frame ,anchor="nw")


    def UpdateDataScrollbar(self):
        self.canvas.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))
        #self.canvas.update()
        #tk.Grid.rowconfigure(self.window,0,weight=1)
        #tk.Grid.columnconfigure(self.window,0,weight=1)
        #self.canvas.create_window((0,0),window=self.frame ,anchor="nw")

    def createOscilogram(self,quantity):
        self.Osci=[(Oscilogram(self.frame, self.width, self.height,i+1,0 ))for i in range(quantity)]
    
    def createButton(self):
        self.addbutton=tk.Button(self.frame,text="AddOscilogram",state="normal",command=self.addOscilogram)
        self.addbutton.grid(row=0)

    def addOscilogram(self):
        self.Osci.append(Oscilogram(self.frame, self.width, self.height, self.numberOfOscilograms+1, 0))
        self.numberOfOscilograms+=1    
        self.UpdateDataScrollbar()
    #add function to adding more oscilograms
    #add posibility to choosing inputs


    def UpdateData(self,buttonsStates):
        if self.state:
            for i in range(len(self.Osci)):
                self.Osci[i].buttonsStates=buttonsStates
                self.Osci[i].UpdateDataToArray(self.datain[0][0])
                

    def resetData(self):
        self.datain=[[[0,0],[0,0]],[[0,0],[0,0]],[[0,0],[0,0]]]
        self.state=False
    