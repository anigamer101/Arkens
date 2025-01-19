#Imports
from tkinter import *
import os
from tkinter import messagebox
import tkinter as tk
import os.path
import subprocess

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
      exp = exbox.get("1.0","end-1c")
      expi = int(exp)
      seti()

#Text box 1 (Token)
linlabel = tk.Label(win, textvariable=lin, height=3, width=30, bd=3,)
linlabel.pack(pady=20)
Linkbox=Text(win, height=5, width=25)
Linkbox.pack()

#Text box 2 (Valid until)
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
      if not  os.path.exists(link):
            
            f = open(Slink, "x")
            subprocess.run(["git","add", Slink])
            subprocess.run(["git", "checkout", "main"])
            subprocess.run(["git", "commit", "https://github.com/anigamer101/Arkens.git", "-m", Slink])
            subprocess.run(["git", "push", "https://github.com/anigamer101/Arkens.git", "main"])
            win.destroy()
            #messagebox.showerror("Arkens","Error")
      
win.mainloop()