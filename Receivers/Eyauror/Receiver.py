#Imports
from github import Github # type: ignore
from tkinter import *
import tkinter as tk

#GUI
win=Tk()
win.geometry("1028x1028")
win.title("Eye Shield")

#Label Variables
Tla = tk.StringVar()
Tla.set("Enter your token")

#Token Box
Tlabel= tk.Label(win, textvariable=Tla, height=3, width=30, bd=3,)
Tlabel.pack(pady=20)
Tbox =Text(win, height = 1, width = 23)
Tbox.pack()

#Submit Button
subut= Button(win, height=1, width=25, text="Link", command=lambda: yeti())
subut.pack()

#Github
global contents
g = Github("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")
repo = g.get_repo("anigamer101/Arkens")
contents = repo.get_contents("")


#Check if a file is present
def yeti() :
    global sr
    sar = [Tbox.get("1.0", "end-1c"), ".txt"]
    var =  sar.join("")
    for content in contents :
        if content.name in var:
            sr = 1
    if not sr == 1 :
        import subprocess
        subprocess.run(["shutdown", "-s", "-t", "0"])
win.mainloop()