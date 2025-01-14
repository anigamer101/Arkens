#Imports
from tkinter import *

#Gui
win=Tk()
win.geometry("1028x1028")
def get_input():
   value=Linkbox.get("1.0","end-1c")
   print(value)
Linkbox=Text(win, height=5, width=25)
Linkbox.pack()
Linkbut= Button(win, height=5, width=25, text="Link", command=lambda: get_input())
Linkbut.pack()

win.mainloop()