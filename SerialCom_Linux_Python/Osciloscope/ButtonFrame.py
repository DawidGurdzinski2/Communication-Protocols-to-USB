from tkinter import *

class ButtonFrame:


    def __init__(self,window):
        self.OscFlag=0
        self.window=window
        self.frame = Frame(window,bg="pink",bd=5,relief=SUNKEN)
        self.createButtons()
        self.frame.grid(row=0,column=0)
        
    def createButtons(self):
        self.photo = [PhotoImage(file='blue.png'),
                PhotoImage(file='blue.png'),
                PhotoImage(file='blue.png'),
                PhotoImage(file='blue.png'),]
        self.name =["Osciloscope","Generator","Modulator","Terminal"]
        self.FONT=10
        self.func=[self.clickOsciloscop,self.clickGenerator,self.clickModulator,self.clickTerminal]

        self.ButtonOsciloscop= Button(self.frame,
                text=self.name[0], 
                command=self.func[0],
                font=("Comic Sans",self.FONT),
                fg="#00FF00",
                bg="black",
                activeforeground="#00FF00",
                activebackground="black",
                state=ACTIVE,
                image=self.photo[0],
                compound='bottom')
        self.ButtonGenerator = Button(self.frame,
                text=self.name[1],
                command=self.func[1],
                font=("Comic Sans",self.FONT),
                fg="#00FF00",
                bg="black",
                activeforeground="#00FF00",
                activebackground="black",
                state=ACTIVE,
                image=self.photo[1],
                compound='bottom')
        self.ButtonModulator = Button(self.frame,
                text=self.name[2],
                command=self.func[2],
                font=("Comic Sans",self.FONT),
                fg="#00FF00",
                bg="black",
                activeforeground="#00FF00",
                activebackground="black",
                state=ACTIVE,
                image=self.photo[2],
                compound='bottom')
        self.ButtonTerminal = Button(self.frame,
                text=self.name[3],
                command=self.func[3],
                font=("Comic Sans",self.FONT),
                fg="#00FF00",
                bg="black",
                activeforeground="#00FF00",
                activebackground="black",
                state=ACTIVE,
                image=self.photo[3],
                compound='bottom')
        self.ButtonOsciloscop.grid(row=0,column=0)
        self.ButtonGenerator.grid(row=0,column=1)
        self.ButtonModulator.grid(row=0,column=2)
        self.ButtonTerminal.grid(row=0,column=3)
        


    def clickOsciloscop(self):
        Osciloscope=Toplevel()
        Osciloscope.title("Osciloscope")
        
        print("osciloscop")

    def clickModulator(self):
        Modulator=Toplevel()
        Modulator.title("Modulator")
        print("modulator")
    
    def clickGenerator(self):
        Generator=Toplevel()
        Generator.title("Generator")
        print("generator")
    def clickTerminal(self):
        Terminal=Toplevel()
        Terminal.title("Terminal")
        print("terminal") 