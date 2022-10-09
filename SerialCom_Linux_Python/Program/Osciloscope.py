import tkinter as tk
from Oscilogram import *
from tkinter import ttk
import threading


class Osciloscope:


    def __init__(self,window,height,width,state,quantity):
        self.state=state
        self.quantity=quantity
        self.window=window
        self.time2=0
        self.height=height
        self.width=width
        self.datain=[[[0,0],[0,0]],[[0,0],[0,0]],[[0,0],[0,0]]]
        self.createScrollBar()
        
    

        self.numberOfOscilograms=0
        self.createOscilogram(self.numberOfOscilograms)
        self.createButtons()


    def createScrollBar(self):
        self.scrollframe=tk.Frame(self.window,bg="black",bd=5)
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
        

    def createOscilogram(self,quantity):
        self.Osci=[(Oscilogram(self.frame, self.width, self.height,2*i+1,0 ))for i in range(quantity)]
        self.Labels=[tk.Label(self.grame,text="Osciloscope"+str(i+1))for i in range(quantity)]

    def createButtons(self):
        self.addbutton=tk.Button(self.frame,text="AddOscilogram",state="normal",command=self.addOscilogram)
        
        self.addbutton.grid(row=0,column=0)
        

    def addOscilogram(self):
        self.Osci.append(Oscilogram(self.frame, self.width, self.height, 2*self.numberOfOscilograms+2))
        self.numberOfOscilograms+=1    
        self.Labels.append(tk.Label(self.frame,text="Osciloscope"+str(self.numberOfOscilograms),bg="grey",font=('Arial',15,'bold')))
        self.Labels[self.numberOfOscilograms-1].grid(row=1+(self.numberOfOscilograms-1)*2)
        self.UpdateDataScrollbar()


    def createThreads(self):
        self.threads=[threading.Thread(target=self.writeData, args=(i,)) for i in range(len(self.Osci))]


    def startThreads(self):
        for i in range(len(self.Osci)):
            self.threads[i].start()
            

    def writeData(self,i):
        #time1=time.time()######################################################
        self.Osci[i].setNumberOfOscilograms(self.numberOfOscilograms)
        self.Osci[i].setSourceList(self.sourceList)
        self.Osci[i].buttonsStates=self.buttonsStates
        self.Osci[i].UpdateDataToArray(self.datain)
        #print("oneOSctime: "+str(time.time()-time1))######################################################


    def UpdateData(self,buttonsStates):
        self.buttonsStates=buttonsStates
        self.sourceList=self.createSourceList(self.datain)
        if self.state:
            #time3=time.time()######################################################
            self.createThreads()
            self.startThreads()
            for i in range(len(self.Osci)):
                self.threads[i].join()
            #print("AllOsc: "+str(time.time()-time3))######################################################
    


    
    def createSourceList(self,data):
        List=[]
        for i in range(len(data[0])-1):
            List.append("Gen"+str(i+1))
        for i in range(len(data[1])-1):
            List.append("Mod"+str(i+1))
        for i in range(len(data[2])-1):
            List.append("Ter"+str(i+1))
        return List

    def resetData(self):
        self.datain=[[[0,0],[0,0]],[[0,0],[0,0]],[[0,0],[0,0]]]
        self.state=False
    


