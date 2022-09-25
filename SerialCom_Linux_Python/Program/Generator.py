import tkinter as tk

class Generator:


    def __init__(self,window,height,width,state):
        self.state=state
        self.window=window
        self.height=height
        self.width=width
        self.datain=0
        self.dataout=0
        self.frame=tk.Frame(self.window,bg="pink",bd=5)
        tk.Grid.rowconfigure(self.window,0,weight=1)
        tk.Grid.columnconfigure(self.window,0,weight=1)
        self.frame.grid(row=0,column=0,sticky="nswe")
    
    def UpdateData(self):
        if self.state:
            self.dataout=self.datain+2

    def resetData(self):
        self.datain=0
        self.dataout=0
        self.state=False
    