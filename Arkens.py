#Imports
from tkinter import *
import os
from tkinter import messagebox

#Gui
win=Tk()
win.geometry("1028x1028")
def get_input():
   global link
   link = Linkbox.get("1.0","end-1c")
   print(link)
Linkbox=Text(win, height=5, width=25)
Linkbox.pack()
Linkbut= Button(win, height=5, width=25, text="Link", command=lambda: get_input())
Linkbut.pack()

#Error management
path = os.access(link,os.F_OK)
if path == "false":
    messagebox.showerror('Arkens', 'Error : Path not valid')
else:
    path = os.access(link, )

win.mainloop()