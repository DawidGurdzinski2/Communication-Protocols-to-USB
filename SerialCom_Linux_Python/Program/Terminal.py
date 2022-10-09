import tkinter as tk
from tkinter import ttk
import serial
import time

class Terminal:


    def __init__(self,window,state):
        self.state=state
        self.dataout=[[0,0]]
        self.window=window
        self.frame=tk.Frame(window,bg="grey",bd=5)
        self.frame.grid(row=0,column=0,sticky="nswe")
        #self.createScrollBar()
        self.BandwidthList=(115200,6969,2323)
        self.currentBandwidth=115200
        self.PortList=("AWWD","PSS")
        self.currentPort="AWWD"
        self.numberOfSignals=1
        #self.createSourceSignal(self.numberOfSignals)
        self.state=False
        self.createButtons()
        self.createComboboxOfBandwidth()
        self.createComboboxOfPorts()
        self.createLabels()
        self.createLabelSignal()

    def createButtons(self):
        self.startButton=tk.Button(self.frame,
                                text="START",
                                state="normal",
                                command=self.changeState,
                                height=1,width=3,
                                bg="black",
                                foreground="white",
                                activeforeground="green",
                                activebackground="black")
        self.startButton.grid(row=0,column=0)
        self.buttonDown=tk.Button(self.frame,
                                text="DOWN",
                                state="normal",
                                command=self.ScaleDown,
                                height=1,width=3,
                                bg="black",
                                foreground="white",
                                activeforeground="green",
                                activebackground="black")
        self.buttonDown.grid(row=2,column=0)
        self.buttonUp=tk.Button(self.frame,
                                text="UP",
                                state="normal",
                                command=self.ScaleUp,
                                height=1,width=3,
                                bg="black",
                                foreground="white",
                                activeforeground="green",
                                activebackground="black")
        self.buttonUp.grid(row=1,column=0)

    def ScaleDown(self):
        if self.numberOfSignals >1:
            self.numberOfSignals-=1
        else:
            self.numberOfSignals=1
        self.destoryLabeSignal()
        self.createLabelSignal()

    def ScaleUp(self):
        self.numberOfSignals+=1
        self.destoryLabeSignal()
        self.createLabelSignal()

    def changeState(self):
        if(self.state):
            self.state=False
            self.startButton.config(text="START")
        else:
            self.state=True
            self.startButton.config(text="STOP")

    


    def createComboboxOfBandwidth(self):
        self.mysignalBd=tk.StringVar()
        self.combo=ttk.Combobox(self.frame,textvariable=self.mysignalBd)
        self.combo['values']=self.BandwidthList
        self.combo.grid(column=2,row=1,columnspan=3)
        self.combo['state']='readonly'
        self.combo.bind("<<ComboboxSelected>>", self.on_select_changedBd)

    def on_select_changedBd(self,event):
        self.currentBandwidth=self.mysignalBd.get()
        print(self.currentBandwidth)

    def createComboboxOfPorts(self):
        self.mysignalPort=tk.StringVar()
        self.combo=ttk.Combobox(self.frame,textvariable=self.mysignalPort)
        self.combo['values']=self.PortList
        self.combo.grid(column=2,row=3,columnspan=3)
        self.combo['state']='readonly'
        self.combo.bind("<<ComboboxSelected>>", self.on_select_changedPort)

    def on_select_changedPort(self,event):
        self.currentPort=self.mysignalPort.get()
        print(self.currentPort)

    def createLabels(self):
        self.bandwidthList=tk.Label(self.frame,text="Bandwidth List",bg="Grey")
        self.bandwidthList.grid(row=0,column=3)
        self.PortList=tk.Label(self.frame,text="Port List",bg="Grey")
        self.PortList.grid(row=2,column=3)
    
    def createLabelSignal(self):
        self.signaltype=tk.Label(self.frame,text="number od signals "+str(self.numberOfSignals),bg="Grey")
        self.signaltype.grid(row=0,column=1)

    def destoryLabeSignal(self):
        self.signaltype.destroy()


    def UpdateData(self):
        if self.state:
            #self.sendSignal()
            #print("zydzi")
            i=1


    

    def resetData(self):
        self.dataout=[[0,0]]
        self.state=False
    