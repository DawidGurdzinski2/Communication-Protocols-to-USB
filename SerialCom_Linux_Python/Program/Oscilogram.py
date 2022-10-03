import tkinter as tk
from tkinter import ttk

from WaveForm import *
import threading
import math 
class Oscilogram:


    def __init__(self,frame,width,height,row,column):
        self.width = width
        self.height = height
        self.frame=frame
        self.row=row
        self.column=column
        self.buttonsStates=[True,True,True,True]
        canvas = tk.Canvas(frame,width=width,height=height+2)
        self.wave=WaveForm(canvas,width,height)
        canvas.grid(row=row,column=column)
        self.previousdData=0
        self.division=1
        self.firstindex=0
        self.secondindex=0
        self.SourceList=[]
        self.createListoOfSources(row)

    
    
    def adjustData(self,data):
        if(abs(data)>=abs(self.previousdData)):
            self.previousdData=abs(data)
        if(self.previousdData==0):
            return 0
        else:
            return math.floor(data*self.height/(2*self.previousdData))

    #edytuj
    def UpdateDataToArray(self,data):
        self.updateCombobox()

        wavedata=data[self.firstindex][self.secondindex]
        self.wave.division=self.division
        self.wave.signaliput=self.buttonsStates[1]
        self.wave.writeDataToArray([self.adjustData(wavedata[0]),wavedata[1]])
        self.wave.printData()

 
    def setSourceList(self,SourceList):
        self.SourceList=SourceList
        
    def updateCombobox(self):
        self.combo['values']=self.SourceList
 
    def createListoOfSources(self,row):
        self.mysignal=tk.StringVar()
        self.combo=ttk.Combobox(self.frame,textvariable=self.mysignal)
        self.combo['values']=self.SourceList
        self.combo.grid(column=1,row=row)
        self.combo['state']='readonly'
        self.combo.bind("<<ComboboxSelected>>", self.on_select_changed)
    
    def on_select_changed(self,event):
        string=self.mysignal.get()
        if "Gen" in string:
            self.firstindex=0
            self.secondindex=int(string[3:])-1
        elif "Mod" in string:
            self.firstindex=1
            self.secondindex=int(string[3:])-1
        elif "Ter" in string:
            self.firstindex=2
            self.secondindex=int(string[3:])-1