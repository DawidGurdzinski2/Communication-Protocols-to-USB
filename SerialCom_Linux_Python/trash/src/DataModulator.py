import math
from SignalGenerator import *

class DataModulator:

    def __init__(self,height,resolution):
        self.SigG=SignalGenerator(resolution, 0)
        self.height=height


    def writeData(self,MaxAmplitude):
        return self.DigitalFilter(self.SigG.generateCOS(), MaxAmplitude)



    def DigitalFilter(self,signal,MaxAmplitude):
        return math.floor(signal*self.height/(2*MaxAmplitude))
        
        
    
    def getMaxAmplitudeCOS(self):
        array= [0 for i in range(self.SigG.getPeriodCOS())]
        for i in range(self.SigG.getPeriodCOS()):
            array[i]=self.SigG.generateCOS()
        MaxA=abs(max(array))
        MinA=abs(min(array))
        if MaxA>MinA:
            return MaxA
        elif MaxA<MinA:
            return MinA
        else:
            return MaxA
        

    def __del__(self):
        None