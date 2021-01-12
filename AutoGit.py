from tkinter import *
from PIL import ImageTk, Image
import pyautogui as pag
import os
import time

BG_COLOR = '#222222'

def pushChanges(event=""):
    gitpath = eGit.get()
    webpath = eWeb.get()
    commitMsg = eMsg.get()
    waittime = sc.get()
    os.startfile(gitpath)
    f = open("AG-savedata.txt","w")
    f.write(str(eGit.get()))
    j = open("AG-savedata2.txt","w")
    j.write(str(eWeb.get()))
    time.sleep(2)
    pag.write("cd "+webpath+"\n")
    time.sleep(2)
    pag.write("git add .\n")
    time.sleep(waittime)
    pag.write('git commit -m "'+commitMsg+'"\n')
    time.sleep(waittime)
    pag.write('git push\n')
    time.sleep(10)
    pag.write('exit\n')
    root.destroy()



# Setup
root = Tk()
root.geometry("720x840")
root.title("AutoGit by WalleNet")
root.iconphoto(False, PhotoImage(file = 'logo.png'))
root.configure(background=BG_COLOR)



# Logos
logo = Label(root,text="AutoGit",font="Bahnschrift 24",bg=BG_COLOR,fg="#ffffff")
logo.place(relx=0.5,rely=0.1,anchor=CENTER)
sublogo = Label(root,text="by WalleNet",font="Bahnschrift 12",fg="#003489",bg=BG_COLOR)
sublogo.place(relx=0.5,rely=0.17,anchor=CENTER)
image = Image.open('logo.png')
img = ImageTk.PhotoImage(Image.open("logo.png").resize((120,120),resample=0))
imgLabel = Label(root, image = img,bg=BG_COLOR)
imgLabel.place(relx=0.5,rely=0.35,anchor=CENTER)



# Git Location Entry
eGit = Entry(root,width=40,bd=3,font="Bahnschrift 10",bg="#303030",fg="#ffffff")
eGit.config(relief=FLAT,insertbackground="#ffffff")
try:
    s = open("AG-savedata.txt","r")
    savedtext = s.read()
except:
    savedtext = "Path to Git Bash"
eGit.insert(0,savedtext)
eGit.place(relx=0.5,rely=0.5,anchor=CENTER)



# Website Location Entry
eWeb = Entry(root,width=40,font="Bahnschrift 10",bg="#303030",fg="#ffffff")
eWeb.config(relief=FLAT,insertbackground="#ffffff")
try:
    k = open("AG-savedata2.txt","r")
    savedtext = k.read()
except:
    savedtext = "Website Directory"
eWeb.insert(0,savedtext)
eWeb.place(relx=0.5,rely=0.57,anchor=CENTER)



# Commit Message Entry
eMsg = Entry(root,width=40,font="Bahnschrift 10",bg="#303030",fg="#ffffff")
eMsg.config(relief=FLAT,insertbackground="#ffffff")
eMsg.insert(0,"Commit Message")
eMsg.focus_set()
eMsg.bind("<FocusIn>", eMsg.selection_range(0,END))
eMsg.place(relx=0.5,rely=0.64,anchor=CENTER)




# Commit Message Entry
scLabel = Label(root,text="COMMIT WAIT TIME",bg=BG_COLOR,fg="#ffffff")
scLabel.place(relx=0.5,rely=0.71,anchor=CENTER)
sc = Scale(root,from_=2,to=10,length=100,orient=HORIZONTAL,bg=BG_COLOR,fg="#ffffff",troughcolor="#ffffff",highlightbackground=BG_COLOR)
sc.place(relx=0.5,rely=0.78,anchor=CENTER)



# Commit Button
bCommit = Button(root,text="Commit & Push",command=pushChanges)
root.bind('<Return>',pushChanges)
bCommit.place(relx=0.5,rely=0.9,anchor=CENTER)



# Start Program
root.mainloop()