#Imports
from tkinter import *
import os
from tkinter import messagebox
from pathlib import Path
import subprocess

      
#Gui
win=Tk()
win.geometry("1028x1028")
#imag = PhotoImage(file="logo.jpg")
#imag.put(imag)
def get_input():
      global link
      link = Linkbox.get("1.0","end-1c")
      seti()
Linkbox=Text(win, height=5, width=25)
Linkbox.pack()

Linkbut= Button(win, height=1, width=25, text="Link", command=lambda: get_input)
Linkbut.pack()


#Link
def seti():
      subprocess.call("files.php")

win.mainloop()