import tkinter as tk
import math

class Signal:


    def __init__(self):
        self.counter=0
        self.oldcounter=0
        self.signaltypes=("cosinus","sinus")

    def generateSignal(self,Period,signalType):
        self.Period=Period
        if(signalType==0):
            return    self.generateCOS(self.Period)

    def generateCOS(self,Period):
        self.oldcounter=self.counter
        self.counter=self.counter+1.2
        if(self.counter==self.Period):
            self.counter=1
            self.oldcounter=0
        return [math.cos(2*self.counter*math.pi/self.Period), self.counter-self.oldcounter]
        