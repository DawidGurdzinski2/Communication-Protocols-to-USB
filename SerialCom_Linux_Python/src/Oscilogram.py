from tkinter import *
from WaveForm import *
class Oscilogram:


    def __init__(self,frame,WIDTH,HEIGHT,ROW,COLUMN):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.frame=frame
        self.ROW=ROW
        self.COLUMN=COLUMN
        canvas = Canvas(frame,width=WIDTH,height=HEIGHT)
        wave=WaveForm(canvas)
        canvas.grid(row=ROW,column=COLUMN)
