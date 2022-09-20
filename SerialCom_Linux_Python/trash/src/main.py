from tkinter import *
from tkinter import messagebox
from OscilogramFrame import *


window = Tk() 
windowHeight=1000
windowWidth=1200

window.geometry(str(windowWidth)+"x"+str(windowHeight))
window.title("Bro Code first GUI program")
window.config(background="#2bf33f")
frame=OscilogramFrame(window)
frame.initOscilograms()
while(True):
    frame.updateData()
    window.update()
    time.sleep(0.01)







def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        window.destroy()
window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop() 