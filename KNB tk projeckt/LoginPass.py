from tkinter import *  
from webbrowser import *
import io
from KNB_tk_projeckt import *
from OmaMoodul import startwinKNB

users = {} 

def file():
    with io.open("database.txt", "r", encoding="utf-8") as file:
        for line in file:
            k, v=line.strip().split("-")
            users[k.strip()] = v.strip()
        file.close()
        return users

def file_add(i):
        users.update({regname.get():regpass2.get()})
        file=io.open("database.txt", "a")
        file.write(f"{i}\n")
        file.close()
        return users

#win=Tk()
#win.geometry("600x300")

def start():
    global win
    win=Tk()
    win.geometry("600x300")
    startwin()

def startwin():
    global win, c
    file()
    win.title("Rock-Paper-Scissors")
    c = Canvas(win, bg = "white", height = "550",width = "250")
    lbl=Label(c,text="Welcome", bg="lightblue",fg="black",font="Arial 50", width=15)
    btn1=Button(c, text="Login", font="Arial 22", bg="pink", fg="black", relief=RAISED, width=15, borderwidth=5, command=login)
    btn2=Button(c, text="Registreerimine", font="Arial 22", bg="green", fg="black", relief=RAISED, width=15, borderwidth=5, command=reg)
    btn3=Button(c, text="Exit", font="Arial 22", bg="red", fg="black", relief=RAISED, width=15, borderwidth=5, command=exit)

    c.grid()
    lbl.pack()
    btn1.pack(fill=BOTH, side=TOP)
    btn2.pack(fill=BOTH, side=TOP)
    btn3.pack(fill=BOTH, side=TOP)

def startreg():
    c1.grid_remove()
    startwin()

def reg():
    global regwin
    global regname
    global regpass
    global regpass2
    global reglabel
    global c1
    c.grid_remove()
    c1 = Canvas(win, bg = "white", height = "600",width = "600")
    win.title("Registreerimine")
    uname = Label(c1 ,text="Nimi : ", fg="red", font="Arial 24")
    regname = Entry(c1 ,width=32)
    pas = Label(c1 ,text="Salasõna : ", fg="lightblue", font="Arial 24")
    regpass = Entry(c1 ,width=32)
    pas2 = Label(c1 ,text="Korda salasõna : ", fg="blue", font="Arial 24")
    regpass2 = Entry(c1 ,width=32)
    exitb = Button(c1 ,text="TAGASI", bg="black", fg="red", font="Arial 20", command=startreg)
    regb = Button(c1 ,text="REGISTREERIMA", bg="black", fg="lightblue", font="Arial 20", command=regverifying)
    reglabel = Label(c1, fg="black", font="Arial 20")

    uname.pack(fill=BOTH, side=TOP)
    regname.pack(fill=BOTH, side=TOP)
    pas.pack(fill=BOTH, side=TOP)
    regpass.pack(fill=BOTH, side=TOP)
    pas2.pack(fill=BOTH, side=TOP)
    regpass2.pack(fill=BOTH, side=TOP)
    reglabel.pack(fill=BOTH, side=TOP)
    regb.pack(side=RIGHT)
    exitb.pack(side=LEFT)
    c1.grid()

def regverifying():
    rg = regpass.get()
    if regpass.get() == regpass2.get():
        if len(rg) >= 5:
            if regname.get() in users:
                reglabel["text"] = "Proovi teist"
            else:
                #users[regname.get()] = regpass2.get()
                file_add(f"{regname.get()}-{regpass2.get()}")
                startreg()
        else:
             reglabel["text"] = "Salasõnas peab olema vähemalt 6 sümbolist"
    else:
        reglabel["text"] = "Salasõna ei klapi" 

def startlog():
    c2.grid_remove()
    startwin()

def login():
        global loglabel
        global logname
        global logpass
        global logb
        global c2
        c.grid_remove()
        win.title("Login")
        c2 = Canvas(win, bg = "white", height = "600",width = "600")
        uname = Label(c2 ,text="Nimi : ", fg="red", font="Arial 24")
        logname = Entry(c2 ,width=80)
        pas = Label(c2 ,text="Sanalsõna : ", fg="lightblue", font="Arial 24")
        logpass = Entry(c2 ,show="*",  width=80)
        logpass.insert(0, "salasõna")
        def clear_all(event):
            logpass.delete(0,END)
        logpass.bind("<Button-1>",clear_all)
        exitb = Button(c2 ,text="TAGASI", bg="black", fg="red", font="Arial 20", command=startlog)
        logb = Button(c2 ,text="Logi sisse", bg="black", fg="lightblue", font="Arial 20", command=logverifying)
        loglabel = Label(c2, fg="black", font="Arial 20")

        uname.pack(fill=BOTH, side=TOP)
        logname.pack(fill=BOTH, side=TOP)
        pas.pack(fill=BOTH, side=TOP)
        logpass.pack(fill=BOTH, side=TOP)
        loglabel.pack(fill=BOTH, side=TOP)
        logb.pack(side=RIGHT)
        exitb.pack(side=LEFT)
        c2.grid()

def logverifying():
    loglabel.pack(fill=BOTH)
    if logname.get() in users.keys():
        if logpass.get() == users[logname.get()]: 
            c2.grid_remove()
            exitt()
        else:
            loglabel["text"] = "Vale nimi või salasõna ! "
    else:
        loglabel["text"] = "Vale nimi või salasõna ! "

def exitt():
    win.destroy()
    startwinKNB()

start()
win.mainloop()