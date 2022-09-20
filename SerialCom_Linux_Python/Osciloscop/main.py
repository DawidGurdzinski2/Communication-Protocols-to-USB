from tkinter import *
from tkinter import messagebox
from ButtonFrame import *

window = Tk() 
windowHeight=120
windowWidth=500

window.geometry(str(windowWidth)+"x"+str(windowHeight))
window.title("Main Window")
window.config(background="white")

frame=ButtonFrame(window,windowHeight,windowWidth)




def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        window.destroy()
window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop() 