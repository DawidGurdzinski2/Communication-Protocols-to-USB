
from tkinter import messagebox
import tkinter as tk
from ButtonFrame import *
from multiprocessing import Process
import threading
import time 

window =tk.Tk() 
windowHeight=120
windowWidth=440
#window.resizable(False,False)





window.geometry(str(windowWidth)+"x"+str(windowHeight))
window.title("Main Window")
window.config(background="white")




frame=ButtonFrame(window)


def zabawa():
    nigga=0
    while True:
        frame.UpdateData()
        data=frame.getData()
        
        frame.setData(data[1], 0, 0, 0)
        
        
        

x=threading.Thread(target=zabawa,daemon=True)
x.start()


def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        window.destroy()
        
window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop() 


