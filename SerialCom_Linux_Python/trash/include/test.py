
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
import os
import tkinter as tk
import tkinter.ttk as ttk
 
 
root = tk.Tk()
root.title("Lanch my Programs")
 
 
class Button:
    """button1 = Button("Testo", "4ce", 0, 0)"""
    row = 0
    def __init__(self, text, func, image=""):
        image = tk.PhotoImage(file=image)
        tk.Grid.rowconfigure(root, Button.row, weight=1)
        tk.Grid.columnconfigure(root, 0, weight=1)
 
        self.button = tk.Button(
            root,
            text=text,
            image=image,
            compound = tk.LEFT,
            command=func)
        # self.button.pack()
        self.button.grid(sticky="nswe")
        self.button.image = image
        Button.row += 1
 
    def open(text):
        os.startfile(text)
 
 
data = [
    ["Text 1", lambda: Button.open("niga"), "blue.png"],
    ["Text 2", lambda: Button.open("giga"), "blue.png"],
]
 
for d in data:
    b = Button(*d)
 
root.mainloop()



self.ButtonOsciloscop= tk.Button(self.frame,
                text=self.name[0], 
                command=self.func[0],
                font=("Comic Sans",self.FONT),
                fg="#00FF00",
                bg="black",
                activeforeground="#00FF00",
                activebackground="black",
                state="active",
                image=self.photo[0],
                compound='bottom')
        self.ButtonGenerator =tk.Button(self.frame,
                text=self.name[1],
                command=self.func[1],
                font=("Comic Sans",self.FONT),
                fg="#00FF00",
                bg="black",
                activeforeground="#00FF00",
                activebackground="black",
                state="active",
                image=self.photo[1],
                compound='bottom')
        self.ButtonModulator = tk.Button(self.frame,
                text=self.name[2],
                command=self.func[2],
                font=("Comic Sans",self.FONT),
                fg="#00FF00",
                bg="black",
                activeforeground="#00FF00",
                activebackground="black",
                state="active",
                image=self.photo[2],
                compound='bottom')
        self.ButtonTerminal = tk.Button(self.frame,
                text=self.name[3],
                command=self.func[3],
                font=("Comic Sans",self.FONT),
                fg="#00FF00",
                bg="black",
                activeforeground="#00FF00",
                activebackground="black",
                state="active",
                image=self.photo[3],
                compound='bottom')
        self.ButtonOsciloscop.grid(row=0,column=0)
        self.ButtonGenerator.grid(row=0,column=1)
        self.ButtonModulator.grid(row=0,column=2)
        self.ButtonTerminal.grid(row=0,column=3)