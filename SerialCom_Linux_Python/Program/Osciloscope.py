import tkinter as tk
from Oscilogram import *

class Osciloscope:


    def __init__(self,window,height,width,state,quantity):
        self.state=state
        self.quantity=quantity
        self.window=window
        self.height=height
        self.width=width
        self.datain=0
        self.dataout=0
        self.frame=tk.Frame(self.window,bg="pink",bd=5)
        tk.Grid.rowconfigure(self.window,0,weight=1)
        tk.Grid.columnconfigure(self.window,0,weight=1)
        self.frame.grid(row=0,column=0,sticky="nswe")
       # self.createOscilogram(0)

    
    #def createOscilogram(self,quantity):
     #   for i in range(quantity):
      #      self.Osci[i]=Oscilogram(self.frame, self.width, self.height,i,0 ,0 )
            

    


    def UpdateData(self):
        if self.state:
            self.dataout=self.datain+2

    def resetData(self):
        self.datain=0
        self.dataout=0
        self.state=False
    