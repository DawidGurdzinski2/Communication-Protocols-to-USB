import tkinter as tk
from tkinter import ttk

from WaveForm import *
import threading
import math 
class Oscilogram:


    def __init__(self,frame,width,height,row):
        self.width = width
        self.height = height
        self.frame=frame
        self.row=row  
        self.buttonsStates=[True,True,True,True]
        canvas = tk.Canvas(frame,width=width,height=height+2)

        canvas.grid(row=row,column=0)
        self.wave=WaveForm(canvas,width,height)
        self.secondframe=tk.Frame(self.frame)
        self.secondframe.grid(row=row,column=1)
        self.scaleYTuple=(0.01,0.05,0.1,0.2,0.5,1,2,5,10,20,50)
        self.previousdData=0
        self.division=1
        self.firstindex=0
        self.secondindex=0
        self.scaleY=self.scaleYTuple.index(1)
        self.scaleYMultiplayer=1
        self.SourceList=[]
        self.createButtons()
        self.createListoOfSources()

    
    #do wyjebania 
    def adjustData(self,data):
        if(abs(data)>=abs(self.previousdData)):
            self.previousdData=abs(data)
        if(self.previousdData==0):
            return 0
        else:
            return math.floor(self.scaleYMultiplayer*data*self.height/2)

    



    def UpdateDataToArray(self,data):
        self.updateCombobox()
        try:
            wavedata=data[self.firstindex][self.secondindex]
        except:
            wavedata=data[0][0]
        self.wave.division=self.division
        #if na stopowanie zeby zmiejszyc pobor mocy obliczeniowej
        self.wave.signaliput=(self.buttonsStates[1] and self.buttonsStates[2] and self.buttonsStates[3])
        self.wave.writeDataToArray([self.adjustData(wavedata[0]),wavedata[1]])
        self.wave.printData()

    
    def setSourceList(self,SourceList):
        self.SourceList=SourceList
        
    def updateCombobox(self):
        try:
            self.combo['values']=self.SourceList
        except:
            pass

    def createListoOfSources(self):
        self.mysignal=tk.StringVar()
        self.combo=ttk.Combobox(self.secondframe,textvariable=self.mysignal)
        self.combo['values']=self.SourceList
        self.combo.grid(column=0,row=2)
        self.combo['state']='readonly'
        self.combo.bind("<<ComboboxSelected>>", self.on_select_changed)
    
    def createButtons(self):
        self.buttonUp=tk.Button(self.secondframe,text="Up",state="normal",command=self.ScaleUp)
        self.buttonUp.grid(row=0,column=0)
        self.buttonDown=tk.Button(self.secondframe,text="Down",state="normal",command=self.ScaleDown)
        self.buttonDown.grid(row=1,column=0)
        self.buttonLeft=tk.Button(self.secondframe,text="LEFT",state="normal",command=self.ScaleLeft)
        self.buttonLeft.grid(row=0,column=1)
        self.buttonRight=tk.Button(self.secondframe,text="RIGHT",state="normal",command=self.ScaleRight) 
        self.buttonRight.grid(row=1,column=1)

    def ScaleUp(self):
        self.scaleY+=1
        self.setScale()

    def ScaleDown(self):
        self.scaleY-=1
        self.setScale()

    def ScaleLeft(self):
        print("gugugaga") 

    def ScaleRight(self):
        print("gugugaga")

    def setScale(self):
        if self.scaleY<0 :
            self.scaleY=0
        elif self.scaleY>len(self.scaleYTuple)-1:
            self.scaleY=len(self.scaleYTuple)-1
        self.scaleYMultiplayer=self.scaleYTuple[self.scaleY]
        

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
