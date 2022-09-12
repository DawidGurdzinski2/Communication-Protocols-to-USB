import math
class SignalGenerator:

    def __init__(self,resolution,signaltype):
        self.counter=0
        self.resolution=resolution
        self.signaltype=signaltype
    
    
    def resetSignal(self):
        self.counter=0

    def getPeriodCOS(self):
        return 2*self.resolution

    def generateCOS(self):
        self.counter=self.counter+1
        if(self.counter==self.getPeriodCOS()):
            self.counter=0
        return math.cos(self.counter*math.pi/self.resolution)
    
    