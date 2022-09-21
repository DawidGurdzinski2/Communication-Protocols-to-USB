import tkinter as tk
from Button import *
class ButtonFrame:


    def __init__(self,window):
        self.OscFlag=0
        self.window=window
        self.frame = tk.Frame(self.window,bg="black",bd=5)
        tk.Grid.rowconfigure(self.window,0,weight=1)
        tk.Grid.columnconfigure(self.window,0,weight=1)
        self.createButtons()
        self.frame.grid(row=0,column=0,sticky="nswe")
        
    def createButtons(self):
        data = [[self.frame,"Osciloscope", lambda: Button.clickOsciloscop(self), 0,0,"blue.png"],
                    [self.frame,"Generator", lambda: Button.clickGenerator(self) ,0,1,"blue.png"],
                    [self.frame,"Modulator", lambda: Button.clickModulator(self), 0,2,"blue.png"],
                    [self.frame,"Terminal", lambda: Button.clickTerminal(self), 0,3,"blue.png"],]
        data1 = [[self.frame,"Osciloscope", lambda: Button.clickOsciloscop(self), 0,5,"blue.png"],
                    [self.frame,"Generator", lambda: Button.clickGenerator(self) ,0,1,"blue.png"],
                    [self.frame,"Modulator", lambda: Button.clickModulator(self), 0,2,"blue.png"],
                    [self.frame,"Terminal", lambda: Button.clickTerminal(self), 0,3,"blue.png"],]
        for d in data:
            self.b = Button(*d)
        self.but=Button(*data1[0])
        #self.b.changeButtonState()
      
