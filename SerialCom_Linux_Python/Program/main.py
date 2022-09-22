
from tkinter import messagebox
import tkinter as tk
from ButtonFrame import *
from multiprocessing import Process


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
    count = 0
    while True:
        count += 1
        frame.kabelekin(count)
        #print(frame.kabelekout())
x=Process(target=zabawa)
x.start()


def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        window.destroy()
        x.kill()
window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop() 


