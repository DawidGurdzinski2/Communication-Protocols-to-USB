from Oscilogram import *
from tkinter import *
class OscilogramFrame:


    def __init__(self,window):
        self.window=window
        frame = Frame(window,bg="pink",bd=5,relief=SUNKEN)
        oscilogram1 =Oscilogram(frame,500,400,0,0)
        oscilogram2 =Oscilogram(frame,500,400,1,0)
      
        frame.grid(row=0,column=0)