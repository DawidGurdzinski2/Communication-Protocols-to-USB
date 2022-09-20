from tkinter import *
from WaveForm import *
class Oscilogram:


    def __init__(self,frame,WIDTH,HEIGHT,ROW,COLUMN,dataformat):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.frame=frame
        self.ROW=ROW
        self.COLUMN=COLUMN
        self.dataformat=dataformat
        canvas = Canvas(frame,width=WIDTH,height=HEIGHT)
        self.wave=WaveForm(canvas,WIDTH,HEIGHT,dataformat)
        canvas.grid(row=ROW,column=COLUMN)

    def UpdateDataToArray(self,data):
        self.wave.writeDataToArray(data)
        self.wave.printData()