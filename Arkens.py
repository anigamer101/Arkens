#Imports
from tkinter import *
import os
from tkinter import messagebox
import tkinter as tk
import os.path
import subprocess
import shared

#GUI Init
win=Tk()
win.geometry("1028x1028")
win.title("Arkens")


#Label variables
lin = tk.StringVar()
rep = tk.StringVar()
blin = tk.StringVar()
ex = tk.StringVar()
rep.set("Git repository digital link")
blin.set("Name your token")
ex.set("Expire after (Textbox input) seconds from now")
lin.set("Name your token")

#Submit button execution code
def get_input():
      global repo, exp, Blink, link, expi, re
      link = Linkbox.get("1.0","end-1c")
      repo = rebox.get("1.0","end-1c")
      exp = exbox.get("1.0","end-1c")
      expi = int(exp)
      re = ["Repo", "(", repo,")"]
      repo == re
      seti()

#Text box 1 (Token)
linlabel = tk.Label(win, textvariable=lin, height=3, width=30, bd=3,)
linlabel.pack(pady=20)
Linkbox=Text(win, height=5, width=25)
Linkbox.pack()

#Text box 2 (Repo)
relabel = tk.Label(win, textvariable=rep, height=3, width=30, bd=3,)
relabel.pack(pady=20)
rebox=Text(win, height=5, width=25)
rebox.pack()

#Text box 3 (Valid until)
exlabel = tk.Label(win, textvariable=ex, height=3, width=40, bd=3,)
exlabel.pack(pady=20)
exbox =Text(win, height = 5, width = 25)
exbox.pack()

#Submit Button
subut= Button(win, height=1, width=25, text="Repo link", command=lambda: get_input())
subut.pack()

#Token Creation
def seti():
      global Slink, File
      File = link,".txt"
      Slink = " ".join(File)
      shared.value = (link)
      if not  os.path.exists(link):
            try :
                  f = open(Slink, "x")
                  subprocess.call(["git", "commit"])
                  subprocess.call(["git", "push"])
                  win.destroy()
            except:           
 
                  messagebox.showerror("Arkens","Error")
      
win.mainloop()