from tkinter import *
from tkinter import messagebox
from PIL import *

class ButtonFrame:


    def __init__(self,window,height,width):
        self.window=window
        self.height=height
        self.width=width
        self.frame = Frame(window,bg="pink",bd=5,relief=SUNKEN)
        #self.photo = PhotoImage(file='blue.png')
        self.photoImages = [Image.open("blue.png"),Image.open("blue.png"),Image.open("blue.png"),Image.open("blue.png")]
        self.resizeFrame()
        
        
    def clickOsciloscop(self):
    
        print("osciloscop")

    def clickModulator(self):
    
        print("modulator")
    
    def clickGenerator(self):
    
        print("generator")
    def clickTerminal(self):
    
        print("terminal") 

    
    
    def resizeFrame(self):
        resizedImage= [self.photoImages[0].resize((self.winndow.winfo_screenheight(),self.window.winfo_screenwidth()), Image.ANTIALIAS),
                        self.photoImages[1].resize((self.winndow.winfo_screenheight(),self.window.winfo_screenwidth()), Image.ANTIALIAS),
                        self.photoImages[2].resize((self.winndow.winfo_screenheight(),self.window.winfo_screenwidth()), Image.ANTIALIAS),
                        self.photoImages[3].resize((self.winndow.winfo_screenheight(),self.window.winfo_screenwidth()), Image.ANTIALIAS)]
        self.Osciloscope = Button(self.frame,
                text="click me!",
                command=self.clickOsciloscop,
                font=("Comic Sans",20),
                fg="#00FF00",
                bg="black",
                activeforeground="#00FF00",
                activebackground="black",
                state=ACTIVE,
                image=resizedImage[0],
                compound='bottom')
        self.Modulator = Button(self.frame,
                text="click me!",
                command=self.clickModulator,
                font=("Comic Sans",20),
                fg="#00FF00",
                bg="black",
                activeforeground="#00FF00",
                activebackground="black",
                state=ACTIVE,
                image=resizedImage[1],
                compound='bottom')
        self.Generator = Button(self.frame,
                text="click me!",
                command=self.clickGenerator,
                font=("Comic Sans",20),
                fg="#00FF00",
                bg="black",
                activeforeground="#00FF00",
                activebackground="black",
                state=ACTIVE,
                image=resizedImage[2],
                compound='bottom')
        self.Terminal= Button(self.frame,
                text="click me!",
                command=self.clickTerminal,
                font=("Comic Sans",20),
                fg="#00FF00",
                bg="black",
                activeforeground="#00FF00",
                activebackground="black",
                state=ACTIVE,
                image=resizedImage[3],
                compound='bottom')
        self.Osciloscope.grid(row=0,column=0)
        self.Modulator.grid(row=0,column=1)
        self.Generator.grid(row=0,column=2)
        self.Terminal.grid(row=0,column=3)
        self.frame.grid(row=0,column=0)
        
       
    
