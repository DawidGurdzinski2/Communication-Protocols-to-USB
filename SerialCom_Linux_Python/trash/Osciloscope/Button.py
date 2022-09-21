import tkinter as tk

from tkinter import messagebox
class Button:
    """button1 = Button("Testo", "4ce", 0, 0)"""
    def __init__(self,frame, text, func,row,column, image=""):
        image = tk.PhotoImage(file=image)
        tk.Grid.rowconfigure(frame, row, weight=1)
        tk.Grid.columnconfigure(frame, column, weight=1)
          
        self.button = tk.Button(
            frame,
            text=text,
            state="normal",
            image=image,
            compound = tk.TOP,
            command=func
            )
        self.flag=0
        self.button.grid(row=row,column=column ,sticky="nswe")
        self.button.image = image
        #self.button['state']="disabled"
 
    def clickOsciloscop(self):
       # self.changeButtonState()
        
            
        self.Osciloscope=tk.Toplevel()
        self.Osciloscope.title("Osciloscope")
        print(Osciloscope.state())
        def on_closing():
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                self.Osciloscope.destroy()
                flag=0
        #self.but['state'] = "disabled"  
        #self.but.config(state="disabled")      
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