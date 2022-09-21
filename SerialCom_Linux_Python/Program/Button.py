import tkinter as tk

from tkinter import messagebox
class Button:
    
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
 
    def changeButtonState(self,state):
        if state:
            self.button.config(state="normal")
        else:
            self.button.config(state="disabled")

    