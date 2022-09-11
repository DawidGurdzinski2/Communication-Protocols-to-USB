from tkinter import *
class WaveForm:

    def __init__(self,canvas):
        self.canvas=canvas
        canvas.create_line(0,0,200,200,fill="red",width=5)
        

