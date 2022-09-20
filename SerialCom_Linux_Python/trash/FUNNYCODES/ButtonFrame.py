from tkinter import *
import os
import tkinter as tk
import tkinter.ttk as ttk
from Button import *

class ButtonFrame:


    def __init__(self,window,height,width):
        self.window=window
        self.height=height
        self.width=width
        tk.Grid.rowconfigure(self.window,0,weight=1)
        tk.Grid.columnconfigure(self.window,0,weight=1)
        self.frame = tk.Frame(self.window)
        self.frame.grid(row=0,column=0,sticky="nsew")
        #self.photo = PhotoImage(file='blue.png')
        self.photoImages = [PhotoImage(file='blue.png'),PhotoImage(file='blue.png'),PhotoImage(file='blue.png'),PhotoImage(file='blue.png')]
        self.createButtons()
        
    def createButtons(self):
        data = [[self.frame,"Osciloscope", lambda: Button.clickOsciloscop, "blue.png"],
                [self.frame,"Generator", lambda: Button.clickGenerator, "blue.png"],
                [self.frame,"Modulator", lambda: Button.clickModulator, "blue.png"],
                [self.frame,"Terminal", lambda: Button.clickTerminal, "blue.png"]]
        for d in data:
             b = Button(*d)
        
    
