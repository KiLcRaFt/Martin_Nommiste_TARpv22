from tkinter import *  
from webbrowser import *

users = {"username":"password"}  

def startwin():
    global win
    win=Tk()
    win.geometry("350x270")
    win.title("Login or Registreerimine")
    lbl=Label(win,text="Welcome", bg="lightblue",fg="black",font="Arial 50", width=15)
    btn1=Button(win, text="Login", font="Arial 22", bg="pink", fg="black", relief=RAISED, width=15, borderwidth=5, command=login)
    btn2=Button(win, text="Registreerimine", font="Arial 22", bg="green", fg="black", relief=RAISED, width=15, borderwidth=5, command=reg)
    btn3=Button(win, text="Exit", font="Arial 22", bg="red", fg="black", relief=RAISED, width=15, borderwidth=5, command=exit)

    lbl.pack()
    btn1.pack(fill=BOTH, side=TOP)
    btn2.pack(fill=BOTH, side=TOP)
    btn3.pack(fill=BOTH, side=TOP)

def reg():
    global regwin
    global regname
    global regpass
    global regpass2
    global reglabel
    regwin=Tk()
    regwin.title("Registreerimine")
    regwin.geometry("600x250")
    uname = Label(regwin ,text="Username : ", fg="red", font="Arial 24")
    regname = Entry(regwin ,width=32)
    pas = Label(regwin ,text="Password : ", fg="lightblue", font="Arial 24")
    regpass = Entry(regwin ,width=32)
    pas2 = Label(regwin ,text="Repeat password : ", fg="blue", font="Arial 24")
    regpass2 = Entry(regwin ,width=32)
    exitb = Button(regwin ,text="BACK", bg="black", fg="red", font="Arial 20", command=startwin)
    regb = Button(regwin ,text="REGISTER", bg="black", fg="lightblue", font="Arial 20", command=regverifying)
    reglabel = Label(regwin, fg="black", font="Arial 20")

    uname.pack(fill=BOTH, side=TOP)
    regname.pack()
    pas.pack(fill=BOTH, side=TOP)
    regpass.pack()
    pas2.pack(fill=BOTH, side=TOP)
    regpass2.pack()
    reglabel.pack()
    regb.pack(side=RIGHT)
    exitb.pack(side=LEFT)

def regverifying():
    if regpass.get() == regpass2.get():
        if regname.get() in users:
            reglabel["text"] = "Try another"
        else:
            users[regname.get()] = regpass2.get()
            startwin()
    else:
        reglabel["text"] = "Passwords does not match" 

def login():
        global loglabel
        global logname
        global logpass
        global logb
        logwin=Tk()
        logwin.title("Login")
        logwin.geometry("600x250")
        uname = Label(logwin ,text="Username : ", fg="red", font="Arial 24")
        logname = Entry(logwin ,width=32)
        pas = Label(logwin ,text="Password : ", fg="lightblue", font="Arial 24")
        logpass = Entry(logwin ,show="*",  width=32)
        logpass.insert(0, "password")
        def clear_all(event):
            logpass.delete(0,END)
        logpass.bind("<Button-1>",clear_all)
        exitb = Button(logwin ,text="BACK", bg="black", fg="red", font="Arial 20", command=startwin)
        logb = Button(logwin ,text="Sign in", bg="black", fg="lightblue", font="Arial 20", command=logverifying)
        loglabel = Label(logwin, fg="black", font="Arial 20")

        uname.pack(fill=BOTH, side=TOP)
        logname.pack()
        pas.pack(fill=BOTH, side=TOP)
        logpass.pack()
        loglabel.pack()
        logb.pack(side=RIGHT)
        exitb.pack(side=LEFT)

def logverifying():
    loglabel.pack(fill=BOTH)
    if logname.get() in users.keys():
        if logpass.get() == users[logname.get()]: 
            loglabel["text"] = "Login Successful ! "
        else:
            loglabel["text"] = "Invalid username or password ! "
    else:
        loglabel["text"] = "Invalid username or password ! "

startwin()
win.mainloop()