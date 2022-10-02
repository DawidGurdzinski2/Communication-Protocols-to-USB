
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


# Data
# Osciloscope input =  [[y,t,S,T],[y,t,S,T],...]-SIGNAL AND SOURCE INFO [T,T,T,T]-BUTTON STATE  [O]
#  setting input source to every  Waveform  S=0 Generator  S=1 Modulator  S=2 Terminal  T-output of source
#    
# Terminal input =   O   how many outputs
# Terminal Output =   [[y,t,2,T ],[y,t,2,T ],.... ]
#  
# Generator input =  0 how many outputs
# Generator Output =   [[y,t,0,T ],[y,t,0,T],.... ]
#
# Modulator input =  [[y,t,S,T],[y,t,S,T],...]
# Modulator Output =   [[y,t,1,T ],[y,t,1,T],.... ]

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


