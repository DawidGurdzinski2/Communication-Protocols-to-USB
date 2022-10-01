import tkinter as tk
import math

class Signal:


    def __init__(self):
        self.counter=0
        self.oldcounter=0
        self.signalContinue=False
        self.signaltypes=("cosinus","sinus","square")

    def generateSignal(self,signalType,Period,Amplitude,Duty):
        self.Period=Period
        self.Amplitude=-Amplitude
        self.Duty=Duty
        if self.signalContinue:
            if(signalType==0 ):
                return    self.generateCOS()
            elif(signalType==1):
                return    self.generateSIN()
            elif(signalType==2):
                return self.generateSQUR()



    def resetCounter(self):
        self.counter=1
        self.oldcounter=0


    def generateCOS(self):
        self.oldcounter=self.counter
        self.counter=self.counter+1.2
        if(self.counter>=self.Period):
            self.resetCounter()
            
        return [self.Amplitude*math.cos(2*self.counter*math.pi/self.Period), self.counter-self.oldcounter]
        
    def generateSIN(self):
        self.oldcounter=self.counter
        self.counter=self.counter+1.2
        if(self.counter>=self.Period):
            self.resetCounter()
        return [self.Amplitude*math.sin(2*self.counter*math.pi/self.Period), self.counter-self.oldcounter]
    
    def generateSQUR(self):
        self.oldcounter=self.counter
        self.counter=self.counter+1.2
        if(self.counter>=self.Period):
            self.resetCounter()
        if(self.counter>=(self.Duty/100)*self.Period):
            return [0,self.counter-self.oldcounter]
        else:
            return [self.Amplitude,self.counter-self.oldcounter]