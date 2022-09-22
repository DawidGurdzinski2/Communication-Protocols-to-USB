import tkinter as tk
from Button import *
from Osciloscope import *
from multiprocessing import Process
import time 
class ButtonFrame:


    def __init__(self,window):
        self.window=window
        self.data1=0
        self.data2=0
        self.frame = tk.Frame(self.window,bg="black",bd=5)
        tk.Grid.rowconfigure(self.window,0,weight=1)
        tk.Grid.columnconfigure(self.window,0,weight=1)
        self.createButtons()
        self.frame.grid(row=0,column=0,sticky="nswe")
       
    

    def createButtons(self):
        data = [[self.frame,"Osciloscope", lambda: self.clickOsciloscop(), 0,0,"blue.png"],
                    [self.frame,"Generator", lambda: self.clickGenerator() ,0,1,"blue.png"],
                    [self.frame,"Modulator", lambda: self.clickModulator(), 0,2,"blue.png"],
                    [self.frame,"Terminal", lambda: self.clickTerminal(), 0,3,"blue.png"],]
        self.button=[Button(*data[i])for i in range(len(data))]


    def clickOsciloscop(self):
        self.button[0].changeButtonState(False) 
        self.OSCILOSCOPE=tk.Toplevel()
        self.OSCILOSCOPE.title("Osciloscope")
        self.OSCILOSCOPE.geometry(str(400)+"x"+str(400))
        self.OSCILOSCOPE.config(background="white")
        self.Osc=Osciloscope(self.OSCILOSCOPE,400,400)
        
        def chujdawajdane(self,data):
            
            while True:
                self.Osc.setData(data)
                print(self.Osc.getData())


        self.x = Process(target=self.chujdawajdane,args=3)
        self.x.start()

        def on_closing():
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                self.OSCILOSCOPE.destroy()
                self.button[0].changeButtonState(True)   
                self.x.kill()
                
        self.OSCILOSCOPE.protocol("WM_DELETE_WINDOW", on_closing)
        
        

    def clickModulator(self):
        self.button[2].changeButtonState(False) 
        Modulator=tk.Toplevel()
        Modulator.title("Modulator")

        
        

        def on_closing():
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                Modulator.destroy()
        Modulator.protocol("WM_DELETE_WINDOW", on_closing)
        print("modulator")
    
    def clickGenerator(self):
        Generator=tk.Toplevel()
        Generator.title("Generator")
        def on_closing():
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                Generator.destroy()
        Generator.protocol("WM_DELETE_WINDOW", on_closing)
        print("generator")
    def clickTerminal(self):
        Terminal=tk.Toplevel()
        Terminal.title("Terminal")
        def on_closing():
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                Terminal.destroy()
        Terminal.protocol("WM_DELETE_WINDOW", on_closing)
        print("terminal") 
    
    def funkcjacostam(self):
        if(self.button[0].getButtonState()=='disabled' and self.button[2].getButtonState()=='disabled'  ):
            self.OSCILOSCOPE.printnigga()


        #try:
          #  variable
        #except NameError:
         #   return Flase
        #else:
         #   return True
    
    def timer(self):
        print()
        count = 0
        while True:
            time.sleep(1)
            count += 1
            print("logged in for: ", count, "seconds")   
    
    def kabelekin(self,data):
        self.data1=data
        
        
    def kabelekout(self):
        return self.data2