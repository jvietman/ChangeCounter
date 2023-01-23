from tkinter import *
from PIL import Image, ImageTk
from functools import partial
import os, webbrowser, urllib.request

root = Tk()

creator = "jvietman"

# Configuration
root.title("Change Counter")
root.geometry("600x500")
root.iconbitmap(default="imgs/icon.ico")

# Functions
def loadimage(file, size):
    return ImageTk.PhotoImage(Image.open(file).resize(size))

def about():
    global small

    sub = Toplevel(root)
    sub.geometry("300x450")
    sub.resizable(False, False)

    if os.path.exists("imgs/avatar.jpg"): os.remove("imgs/avatar.jpg")
    urllib.request.urlretrieve("https://avatars.githubusercontent.com/u/77661493?v=4", 'imgs/avatar.jpg')
    while not os.path.exists("imgs/avatar.jpg"):
        pass

    icon = loadimage("imgs/avatar.jpg", (200, 200))
    github = loadimage("imgs/github.png", small)

    logo = Label(sub, image=icon)
    logo.image = icon
    logo.place(anchor=CENTER, relx=0.5, rely=0.3)

    info = Label(sub, text="Change Counter", font=("", 15))
    info.place(anchor=CENTER, relx=0.5, rely=0.6)
    author = Label(sub, text="Made by "+creator, font=("", 10))
    author.place(anchor=CENTER, relx=0.5, rely=0.65)

    linkbtn = Button(sub, image=github, command=lambda: webbrowser.open("https://github.com/"+creator))
    linkbtn.image = github
    linkbtn.place(anchor=CENTER, relx=0.5, rely=0.9, relwidth=0.8, relheight=0.1)

def key(e):
    try:
        if int(e.keysym) >= 1 and int(e.keysym) <= 9:
            add(int(e.keysym)*1000)
    except:
        if e.keysym == "Escape":
            about()
        elif e.keysym == "Delete":
            fullclear()
        elif e.keysym == "BackSpace":
            rm()

def clear():
    global logbox
    
    logbox.delete(0, END)

def fullclear():
    global logs
    
    logs = [0]
    add(0)

def add(m):
    global logbox, logs

    z = logs[len(logs)-1] + m/100
    result = round(z, 2)
    
    logs.append(result)
    clear()
    for l in range(1, len(logs)):
        logbox.insert(l+1, logs[l])
    logbox.see(END)

def rm():
    global logbox, logs

    if not len(logs) <= 2: logs.pop()
    clear()
    for l in range(1, len(logs)):
        logbox.insert(l+1, logs[l])
    logbox.see(END)

# Create listbox for logs
logs = [0]

logbox = Listbox(root, font=("", 15))
logbox.place(anchor=N, relx=0.5, rely=0.7, relwidth=0.8, relheight=0.25)
add(0)

# Load images
coins = [200, 100, 50, 20, 10, 5, 2, 1]
imgs = []
btns = []

size = (100, 100)
small = (40, 40)

delimg = loadimage("imgs/0.png", small)

clearimg = loadimage("imgs/clear.png", small)

aboutimg = loadimage("imgs/about.png", small)

for i in coins:
    imgs.append(loadimage("imgs/"+str(i)+".png", size))

# Add buttons
posx = 0.05
posy = 0.05

for i in range(len(imgs)):
    add_i = partial(add, coins[i])
    btns.append(Button(root, image=imgs[i], command=add_i))
    btns[i].place(relx=posx, rely=posy)
    posx += 0.24
    if posx > 0.95:
        posx = 0.05
        posy += 0.25

delbtn = Button(root, image=delimg, command=rm)
delbtn.place(anchor=CENTER, relx=0.25, rely=0.6, relwidth=0.4, relheight=0.1)

clearbtn = Button(root, image=clearimg, command=fullclear)
clearbtn.place(anchor=CENTER, relx=0.65, rely=0.6, relwidth=0.35, relheight=0.1)

aboutbtn = Button(root, image=aboutimg, command=about)
aboutbtn.place(anchor=CENTER, relx=0.9, rely=0.6, relwidth=0.1, relheight=0.1)

root.bind("<Key>", key)
root.mainloop()
