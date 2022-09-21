import tkinter as tk
from Button import *
class ButtonFrame:


    def __init__(self,window):
        self.OscFlag=0
        self.window=window
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
        self.Osciloscope=tk.Toplevel()
        self.Osciloscope.title("Osciloscope")
        def on_closing():
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                self.Osciloscope.destroy()
                self.button[0].changeButtonState(True)   
        self.Osciloscope.protocol("WM_DELETE_WINDOW", on_closing)
        print("osciloscop")

    def clickModulator(self):
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
    
    def changeButtonState(self):
        self.button.config(state="disabled")

    def checkExist(self,variable):
        try:
            variable
        except NameError:
            return Flase
        else:
            return True
