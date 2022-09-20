from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
 

class Button:
    column=0
    def __init__(self,frame, text,columns, func, image):
        photo=PhotoImage(file=image)
        self.button=tk.Button(frame,
                text=text,
                command=func,
                font=("Comic Sans",5),
                fg="#00FF00",
                bg="black",
                activeforeground="#00FF00",
                activebackground="black",
                state=ACTIVE,
                image=photo,
                compound='bottom')
        self.button.grid(row=0,column=columns)
    def clickOsciloscop(self):
        print("osciloscop")

    def clickModulator(self):
    
        print("modulator")
    
    def clickGenerator(self):
    
        print("generator")
    def clickTerminal(self):
    
        print("terminal") 