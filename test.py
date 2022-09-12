
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
    
   

class DataModulator:

    def __init__(self,height):
        self.SigG=SignalGenerator(1000, 0)
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

sw=DataModulator(400)

print(sw.writeData(sw.getMaxAmplitudeCOS()))