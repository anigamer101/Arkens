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
subut= Button(win, height=1, width=25, text="check", command=lambda: yeti())
subut.pack()

#Github
global contents
g = Github("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")
repo = g.get_repo("anigamer101/Arkens")
contents = repo.get_contents("")


#Check if a file is present
def yeti() :
    global sr
    var =  Tbox.get("1.0", "end-1c")
    for content in contents :
        if content.name in var:
            sr = 1
    if sr == 1 :
        print("yes!")
    else: 
        print("no!")
win.mainloop()