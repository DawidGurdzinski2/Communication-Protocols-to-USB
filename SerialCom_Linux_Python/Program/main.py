
from tkinter import messagebox
import tkinter as tk
from ButtonFrame import *

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
# Terminal Output =   [[y,t ],[y,t ],.... ]
#  
# Generator input =  0 how many outputs
# Generator Output =   [[y,t],[y,t],.... ]
#
# Modulator input =  [[y,t],[y,t],...]
# Modulator Output =   [[y,t ],[y,t],.... ]


#data [Generator,Modulator,Terminal]
# Generator=[[y1,x1],[y2,x2],....,[yn,xn]]
# Modulator=[[y1,x1],[y2,x2],....,[yn,xn]]
# Terminal=[[y1,x1],[y2,x2],....,[yn,xn]]

    # convert a time expressed in seconds since epoch to a readable string
#                                        epoch = when your computer thinks time began (reference point)


#(y1,x1)(y2,x2)(y3,x3) x punkty w czasie
#data[x,y]
# [y1,x1=0][y2,x2-x1][y3,x3-x2]
def dataStream():
    while True:
        frame.UpdateData()
        data=frame.getData()
        frame.setData(data)
        
        
        

x=threading.Thread(target=dataStream,daemon=True)
x.start()


def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        window.destroy()
        
window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop() 

