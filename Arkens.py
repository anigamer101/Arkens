#Imports
import git
from tkinter import *
import os
from tkinter import messagebox



      
#GUI Init
win=Tk()
win.geometry("1028x1028")

#Text box 1(REPO)
def get_input1():
      global link
      link = Linkbox.get("1.0","end-1c")
Linkbox=Text(win, height=5, width=25)
Linkbox.pack()

Linkbut= Button(win, height=1, width=25, text="Cloned repo branch folder", command=lambda: get_input1())
Linkbut.pack()

#Text box 2(Token)
def get_input2():
      global Blink
      Blink = Blinkbox.get("1.0","end-1c")
      seti()
Blinkbox=Text(win, height=5, width=25)
Blinkbox.pack()

Blinkbut= Button(win, height=1, width=25, text="Token Name", command=lambda: get_input2())
Blinkbut.pack()


#Token Creation
def seti():
      File = [link,".txt"]
      Slink = " ".join(File)
      if not os.file.exists(link):
            f = open(Slink, "x")
            print(Slink)
      else : messagebox.showerror("Arkens","Error : Token exists")
      
win.mainloop()