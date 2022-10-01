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
        ###########
        #signal parameters
        self.Period=100
        self.signalType=0
        self.Amplitude=1
        self.Duty=0
        ###########
        self.createParameterFrame(self.signalType)
        

    def createListoOfSignals(self):
        self.mysignal=tk.StringVar()
        self.combo=ttk.Combobox(self.frame,textvariable=self.mysignal)
        self.combo['values']=self.signal.signaltypes
        self.combo.grid(column=1,row=0)
        self.combo.current(0) 
        self.combo['state']='readonly'
        self.combo.bind("<<ComboboxSelected>>", self.on_select_changed)

    
    
    
    def createButtons(self):
        self.buttonSet=tk.Button(self.frame,text="Setsignal",state="normal",command=self.setSignal)
        self.buttonStart=tk.Button(self.frame,text="Start",state="normal",command=self.startSignal)
        self.buttonStart.grid(row=1,column=0,sticky="nswe")
        self.buttonSet.grid(row=1,column=1,sticky="nswe")

    
    def startSignal(self):
        if self.buttonStart['text']=="Start":
            self.buttonStart.config(text="Stop")
        else:
            self.buttonStart.config(text="Start")

   
    
    

    
               

    

   

    

    #FUNCIONT WHICH YOU NEED CHANGE TO ADD NEW SIGNAL 
    def sendSignal(self):
        if self.buttonStart['text']=="Start":
            self.signal.signalContinue=False
            return [0,0]
        else:
            self.signal.signalContinue=True
            return self.signal.generateSignal(self.signalType,self.Period,self.Amplitude,self.Duty)
    
    
    def deleteParameters(self,signaltype):
        if signaltype==0 or signaltype==1:
            self.destoryCosPar()
        elif signaltype==2:
            self.destorySQRPar()
    
    def createParameterFrame(self,value):
        if value==0:
            self.createCosPar()
        elif value==1:
            self.createCosPar()
        elif value==2:
            self.createSQRPar()
            
    def on_select_changed(self,event):
        self.signal.resetCounter()
        if self.mysignal.get()==self.signal.signaltypes[0]:
            self.deleteParameters(self.signalType)
            self.signalType=0
            self.createParameterFrame(self.signalType)
        elif self.mysignal.get()==self.signal.signaltypes[1]:
            self.deleteParameters(self.signalType)
            self.signalType=1
            self.createParameterFrame(self.signalType)
        elif self.mysignal.get()==self.signal.signaltypes[2]:
            self.deleteParameters(self.signalType)
            self.signalType=2
            self.createParameterFrame(self.signalType)

    def setPeriod(self):
        try:
            self.Period=float(self.varPeriod.get())
            self.labelPeriod.config(text="Period: "+str(self.Period))
            self.varPeriod.set("")
        except:
            pass
    def setAmplitude(self):
        try:
            self.Amplitude=float(self.varAmplitude.get())
            self.labelAmplitude.config(text="Amplitude: "+str(self.Amplitude))
            self.varAmplitude.set("")
        except:
            pass
    def setDuty(self):
        try:
            self.Duty=float(self.varDuty.get())
            self.labelDuty.config(text="Duty: "+str(self.Duty))
            self.varDuty.set("")
        except:
            pass

    def setSignal(self): 
        self.signal.resetCounter()
        self.setPeriod()
        self.setAmplitude()
        self.setDuty()  
    
    #DESTROYERS AND CREATORS FOR NEW FUNCTION/PARAMETERS
    def createSQRPar(self):
        self.varPeriod =tk.StringVar()
        self.labelPeriod=tk.Label(self.frame,text="Period: "+str(self.Period))
        self.labelPeriod.grid(row=0,column=2)
        self.textboxPeriod=tk.Entry(self.frame,width=15,textvariable=self.varPeriod )
        self.textboxPeriod.grid(column=2,row=1)

        self.varAmplitude =tk.StringVar()
        self.labelAmplitude=tk.Label(self.frame,text="Amplitude: "+str(self.Amplitude))
        self.labelAmplitude.grid(row=0,column=3)
        self.textboxAmplitude=tk.Entry(self.frame,width=15,textvariable=self.varAmplitude )
        self.textboxAmplitude.grid(column=3,row=1)

        self.varDuty =tk.StringVar()
        self.labelDuty=tk.Label(self.frame,text="Duty: "+str(self.Duty))
        self.labelDuty.grid(row=0,column=4)
        self.textboxDuty=tk.Entry(self.frame,width=15,textvariable=self.varDuty )
        self.textboxDuty.grid(column=4,row=1)

    def createCosPar(self):
        self.varPeriod =tk.StringVar()
        self.labelPeriod=tk.Label(self.frame,text="Period: "+str(self.Period))
        self.labelPeriod.grid(row=0,column=2)
        self.textboxPeriod=tk.Entry(self.frame,width=15,textvariable=self.varPeriod )
        self.textboxPeriod.grid(column=2,row=1)

        self.varAmplitude =tk.StringVar()
        self.labelAmplitude=tk.Label(self.frame,text="Amplitude: "+str(self.Amplitude))
        self.labelAmplitude.grid(row=0,column=3)
        self.textboxAmplitude=tk.Entry(self.frame,width=15,textvariable=self.varAmplitude )
        self.textboxAmplitude.grid(column=3,row=1)
    
    
    def destoryCosPar(self):
        self.labelAmplitude.destroy()
        self.labelPeriod.destroy()
        self.textboxAmplitude.destroy()
        self.textboxPeriod.destroy()
        
    def destorySQRPar(self):
        self.labelAmplitude.destroy()
        self.labelPeriod.destroy()
        self.labelDuty.destroy()
        self.textboxAmplitude.destroy()
        self.textboxPeriod.destroy()
        self.textboxDuty.destroy()
