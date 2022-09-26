
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




data=0
window.geometry(str(windowWidth)+"x"+str(windowHeight))
window.title("Main Window")
window.config(background="white")




frame=ButtonFrame(window)


def zabawa():
    nigga=0
    while True:
        nigga+=1
        niggas=[nigga,0]
        frame.setData(niggas, 0, 0, 0)
        frame.UpdateData()
        
        print(frame.getData())
        

x=threading.Thread(target=zabawa,daemon=True)
x.start()


def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        window.destroy()
        
window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop() 


