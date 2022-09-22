import tkinter as tk

class Osciloscope:


    def __init__(self,window,height,width):
        self.window=window
        self.height=height
        self.width=width
        self.data=0
        self.frame=tk.Frame(self.window,bg="black",bd=5)
        tk.Grid.rowconfigure(self.window,0,weight=1)
        tk.Grid.columnconfigure(self.window,0,weight=1)
        self.frame.grid(row=0,column=0,sticky="nswe")
    
    def setData(self,data):
        self.data=data
        print(self.data)
    def printnigga(self):
        print("nigga")
    def getData(self):
        return self.data+2


    