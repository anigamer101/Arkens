#Imports
import git
from tkinter import *
import os
from tkinter import messagebox



      
#GUI Init
win=Tk()
win.geometry("1028x1028")

#Text box 1(Clone)
def get_input1():
      global link
      link = Linkbox.get("1.0","end-1c")
Linkbox=Text(win, height=5, width=25)
Linkbox.pack()

Linkbut= Button(win, height=1, width=25, text="Cloned repo folder", command=lambda: get_input1())
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

#Text box 3(Repo)
def get_input3():
      global repo
      repo = rebox.get("1.0","end-1c")
rebox=Text(win, height=5, width=25)
rebox.pack()

Rebut= Button(win, height=1, width=25, text="Repo link", command=lambda: get_input3())
Rebut.pack()


#Token Creation
def seti():
      File = [link,".txt"]
      Slink = " ".join(File)
      if not os.file.exists(link):
            f = open(Slink, "x")
            print(Slink)
            repo.index.add([Slink]) 
            print('Files Added Successfully') 
            repo.index.commit(Slink) 
            print('Commited successfully')
      else : 
            messagebox.showerror("Arkens","Error : Token exists")
      
win.mainloop()