
from tkinter import messagebox
import tkinter as tk
from ButtonFrame import *

window =tk.Tk() 
windowHeight=120
windowWidth=440
#window.resizable(False,False)

window.geometry(str(windowWidth)+"x"+str(windowHeight))
window.title("Main Window")
window.config(background="white")

frame=ButtonFrame(window)




def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        window.destroy()
window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop() 