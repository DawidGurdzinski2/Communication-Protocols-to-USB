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
        canvas = tk.Canvas(frame,width=width,height=height+2,bg="black")

        canvas.grid(row=row,column=0)
        self.wave=WaveForm(canvas,width,height)
        self.secondframe=tk.Frame(self.frame,background="grey",highlightbackground="green")
        self.secondframe.grid(row=row,column=1)


        self.scaleYTuple=(0.01,0.05,0.1,0.2,0.5,1,2,5,10,20,50)
        self.scaleXTuple=(0.0625,0.125,0.25,0.5,1,2,4,8,16)
        
        self.scaleY=self.scaleYTuple.index(1)
        self.scaleX=self.scaleXTuple.index(1)
        self.scaleYMultiplayer=1
        

        self.previousdData=0
        self.firstindex=0
        self.secondindex=0
        self.state=True
        self.NumberOfOscilograms=0

        self.SourceList=[]
        self.createLabels()
        self.createButtons()
        self.createListoOfSources()

    def setNumberOfOscilograms(self,numberOfOscilograms):
        self.NumberOfOscilograms=numberOfOscilograms
    
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
        if(self.state):
            self.wave.numberOfWave=self.NumberOfOscilograms
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
        self.combo.grid(column=1,row=3,columnspan=3)
        self.combo['state']='readonly'
        self.combo.bind("<<ComboboxSelected>>", self.on_select_changed)
    
    def createButtons(self):
        self.buttonUp=tk.Button(self.secondframe,
                                text="UP",
                                state="normal",
                                command=self.ScaleUp,
                                height=1,width=3,
                                bg="black",
                                foreground="white",
                                activeforeground="green",
                                activebackground="black")
        self.buttonUp.grid(row=0,column=2)
        self.buttonDown=tk.Button(self.secondframe,
                                text="DOWN",
                                state="normal",
                                command=self.ScaleDown,
                                height=1,width=3,
                                bg="black",
                                foreground="white",
                                activeforeground="green",
                                activebackground="black")
        self.buttonDown.grid(row=2,column=2)
        self.buttonLeft=tk.Button(self.secondframe,
                                text="LEFT",
                                state="normal",
                                command=self.ScaleLeft,
                                height=1,width=3,
                                bg="black",
                                foreground="white",
                                activeforeground="green",
                                activebackground="black")
        self.buttonLeft.grid(row=1,column=1)
        self.buttonRight=tk.Button(self.secondframe,
                                text="RIGHT",
                                state="normal",
                                command=self.ScaleRight,
                                height=1,width=3,
                                bg="black",
                                foreground="white",
                                activeforeground="green",
                                activebackground="black") 
        self.buttonRight.grid(row=1,column=3)
        self.buttonStop=tk.Button(self.secondframe,
                                text="STOP",
                                state="normal",
                                command=self.changeState,
                                height=1,width=3,
                                bg="black",
                                foreground="white",
                                
                                activeforeground="green",
                                activebackground="black")
        self.buttonStop.grid(row=1,column=2)
    
    def changeState(self):
        if(self.state):
            self.state=False
            self.buttonStop.config(text="START")
        else:
            self.state=True
            self.buttonStop.config(text="STOP")

    def ScaleUp(self):
        self.scaleY+=1
        self.setScaleY()
        self.uptadeScaleLabels()

    def ScaleDown(self):
        self.scaleY-=1
        self.setScaleY()
        self.uptadeScaleLabels()

    def ScaleLeft(self):
        self.scaleX-=1
        self.setScaleX()
        self.uptadeScaleLabels()

    def ScaleRight(self):
        self.scaleX+=1
        self.setScaleX()
        self.uptadeScaleLabels()

    def createLabels(self):
        self.valueScaleLabel = tk.Label(self.secondframe,
              text="div:"+str(0.2/self.scaleYTuple[self.scaleY])+"V/div",
              fg='green',
              bg='black',
              font=('Arial',15,'bold')
              
              )
        self.valueScaleLabel.grid(row=0,column=0)
        self.timeScaleLabel = tk.Label(self.secondframe,
              text="div:"+str(40/self.scaleXTuple[self.scaleX])+"ms/div",
              fg='green',
              bg='black',
              font=('Arial',15,'bold')
              
              )
        self.timeScaleLabel.grid(row=1,column=0)
    
    def uptadeScaleLabels(self):
        self.timeScaleLabel.config(text="div:"+str(40/self.scaleXTuple[self.scaleX])+"ms/div")
        self.valueScaleLabel.config(text="div:"+str(0.2/self.scaleYTuple[self.scaleY])+"V/div")

    def setScaleY(self):
        if self.scaleY<0 :
            self.scaleY=0
        elif self.scaleY>len(self.scaleYTuple)-1:
            self.scaleY=len(self.scaleYTuple)-1
        self.scaleYMultiplayer=self.scaleYTuple[self.scaleY]
    
    def setScaleX(self):
        if self.scaleX<0 :
            self.scaleX=0
        elif self.scaleX>len(self.scaleXTuple)-1:
            self.scaleX=len(self.scaleXTuple)-1
        self.wave.division=self.scaleXTuple[self.scaleX]

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
