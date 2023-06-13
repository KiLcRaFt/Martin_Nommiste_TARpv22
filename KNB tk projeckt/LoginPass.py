from webbrowser import *
import io
from OmaMoodul import *
from email.mime import image
from random import *
import tkinter as ttk
from tkinter import *
from math import *
from time import sleep
from LoginPass import *
from PIL import Image, ImageTk

users = {} 

def file():
    with io.open(r"database.txt", "r", encoding="utf-8") as file:
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
    win.geometry("550x550")
    startwin()

def startwin():
    global win, c
    file()
    win.title("Rock-Paper-Scissors")
    c = Canvas(win, bg = "white", height = "550",width = "550")
    lbl=Label(c,text="Welcome", bg="lightblue",fg="black",font="Arial 50", width=15, height=2);
    btn1=Button(c, text="Login", font="Arial 22", bg="pink", fg="black", relief=RAISED, width=15, height=3, borderwidth=5, command=login)
    btn2=Button(c, text="Registreerimine", font="Arial 22", bg="green", fg="black", relief=RAISED, width=15, height=3, borderwidth=5, command=reg)
    btn3=Button(c, text="Exit", font="Arial 22", bg="red", fg="black", relief=RAISED, width=15, borderwidth=5, height=3, command=exit)

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
    c1 = Canvas(win, bg = "white", height = "550",width = "550")
    win.title("Registreerimine")
    uname = Label(c1 ,text="Nimi : ", fg="red", font="Arial 24", height=2, width=17)
    regname = Entry(c1 ,width=32)
    pas = Label(c1 ,text="Salasõna : ", fg="lightblue", font="Arial 24", height=2, width=17)
    regpass = Entry(c1 ,width=32)
    pas2 = Label(c1 ,text="Korda salasõna : ", fg="blue", font="Arial 24", height=2, width=17)
    regpass2 = Entry(c1 ,width=32)
    exitb = Button(c1 ,text="TAGASI", bg="black", fg="red", font="Arial 20", height=5, width=17, command=startreg)
    regb = Button(c1 ,text="REGISTREERIMA", bg="black", fg="lightblue", font="Arial 20", height=5, width=17, command=regverifying)
    reglabel = Label(c1, fg="black", font="Arial 20", height=2, width=17)

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
        c2 = Canvas(win, bg = "white", height = "550",width = "550")
        lbl2=Label(c2,bg="white",fg=fg,height=5, width=20)
        uname = Label(c2 ,text="Nimi : ", fg="red", font="Arial 24", height=2, width=17)
        logname = Entry(c2 ,width=80)
        pas = Label(c2 ,text="Sanalsõna : ", fg="lightblue", font="Arial 24", height=2, width=17)
        logpass = Entry(c2 ,show="*",  width=80)
        logpass.insert(0, "salasõna")
        def clear_all(event):
            logpass.delete(0,END)
        logpass.bind("<Button-1>",clear_all)
        exitb = Button(c2 ,text="TAGASI", bg="black", fg="red", font="Arial 20", height=2, width=17, command=startlog)
        logb = Button(c2 ,text="Logi sisse", bg="black", fg="lightblue", font="Arial 20", height=2, width=17, command=logverifying)
        loglabel = Label(c2, fg="black", height=2, width=17, font="Arial 20")

        lbl2.pack(fill=BOTH, side=TOP)
        uname.pack(fill=BOTH, side=TOP)
        logname.pack(fill=BOTH, side=TOP)
        pas.pack(fill=BOTH, side=TOP)
        logpass.pack(fill=BOTH, side=TOP)
        loglabel.pack(fill=BOTH, side=TOP)
        logb.pack(fill=Y, side=RIGHT)
        exitb.pack(fill=Y, side=LEFT)
        c2.grid()

def logverifying():
    loglabel.pack(fill=BOTH)
    if logname.get() in users.keys():
        if logpass.get() == users[logname.get()]: 
            c2.grid_remove()
            imagee()
        else:
            loglabel["text"] = "Vale nimi või salasõna ! "
    else:
        loglabel["text"] = "Vale nimi või salasõna ! "


bg = "white"
fg = "black"

def imagee():
    global rockimage, paperimage, scissorsimage
    rock = PhotoImage(file = r"rock.png")
    rockimage = rock.subsample(4, 4)
    paper = PhotoImage(file = r"paper.png")
    paperimage = paper.subsample(4, 4)
    scissors = PhotoImage(file = r"scissors.png")
    scissorsimage = scissors.subsample(4, 4)
    startwinKNB()

def startwinKNB():
    global c, menubar, win, robot
    #win.iconbitmap("logo.ico")
    #win=ttk.Toplevel()
    #win.geometry("600x300")
    robot = False
    c = Canvas(win, bg = bg, height = "550",width = "550")
    menubar = Menu(win)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Valge", command=white)
    filemenu.add_command(label="Must", command=black)
    filemenu.add_separator()
    menubar.add_cascade(label="Teema", menu=filemenu)
    lbl=Label(c,text="Kivi/Paber/Käärid", bg=bg,fg=fg,font="Arial 35", height=3, width=20)
    btn1=Button(c, text="Inimesega", fg="Black", font="Arial 22", relief=RAISED, height=3, width=20, borderwidth=5, command=p1)
    btn2=Button(c, text="Arvutiga", fg="Black", font="Arial 22", relief=RAISED, height=3, width=20, borderwidth=5, command=p1com)
    ex=Button(c, text="Välju", fg="red", font="Arial 10", relief=RAISED, height=7, width=20, borderwidth=3, command=exit)

    win.config(menu=menubar)
    c.grid()
    lbl.pack(fill=X, side=TOP)
    btn1.pack(fill=Y, side=TOP)
    btn2.pack(fill=Y, side=TOP)
    ex.pack(fill=Y, side=BOTTOM)

def p1():
    global cp1, choisee
    c.grid_remove()
    choisee = 1
    cp1 = Canvas(win, bg = bg, height = "550",width = "550")
    lbl=Label(cp1,text="1 inimese valik on:", bg=bg,fg=fg,font="Arial 35", height=1, width=20)
    lbl2=Label(cp1,bg=bg,fg=fg,height=2, width=20)
    btnRock1=Button(cp1, image=rockimage, fg="Black", relief=RAISED, width=15, borderwidth=5, command=rockp1)
    btnPaper1=Button(cp1, image=paperimage, fg="Black", font="Arial 22", relief=RAISED, width=16, borderwidth=5, command=paperp1)
    btnScissors1=Button(cp1, image=scissorsimage, fg="Black", font="Arial 22", relief=RAISED, width=16, borderwidth=5, command=scissorsp1)
    ex=Button(cp1, text="Välju", fg="red", font="Arial 10", relief=RAISED, width=6, borderwidth=3, command=exit)

    cp1.grid()
    lbl.pack(fill=BOTH, side=TOP)
    btnRock1.pack(fill=BOTH, side=TOP)
    btnPaper1.pack(fill=BOTH, side=TOP)
    btnScissors1.pack(fill=BOTH, side=TOP)
    ex.pack(fill=Y, side=BOTTOM)
    lbl2.pack(fill=BOTH, side=BOTTOM)

def p1com():
    global cp1, choisee, robot
    c.grid_remove()
    choisee = 2
    robot = True
    cp1 = Canvas(win, bg = bg, height = "550",width = "550")
    lbl=Label(cp1,text="Inimene 1 valik on:", bg=bg,fg=fg,font="Arial 35", height=1, width=20)
    lbl2=Label(cp1,bg=bg,fg=fg,height=2, width=20)
    btnRock1=Button(cp1, image=rockimage, fg="Black", font="Arial 22", relief=RAISED, width=15, borderwidth=5, command=rockp1com)
    btnPaper1=Button(cp1, image=paperimage, fg="Black", font="Arial 22", relief=RAISED, width=15, borderwidth=5, command=paperp1com)
    btnScissors1=Button(cp1, image=scissorsimage, fg="Black", font="Arial 22", relief=RAISED, width=15, borderwidth=5, command=scissorsp1com)
    ex=Button(cp1, text="Väljuda", fg="red", font="Arial 10", relief=RAISED, width=6, borderwidth=3, command=exit)

    cp1.grid()
    lbl.pack(fill=BOTH, side=TOP)
    btnRock1.pack(fill=BOTH, side=TOP)
    btnPaper1.pack(fill=BOTH, side=TOP)
    btnScissors1.pack(fill=BOTH, side=TOP)
    ex.pack(fill=Y, side=BOTTOM)
    lbl2.pack(fill=BOTH, side=BOTTOM)

def rockp1com():
    global p1rock, p1paper, p1scissors
    p1rock = True
    p1paper = False
    p1scissors = False
    cp1.grid_remove()
    p2com()
   
def paperp1com():
    global p1rock, p1paper, p1scissors
    p1rock = False
    p1paper = True
    p1scissors = False
    cp1.grid_remove()
    p2com()
    
def scissorsp1com():
    global p1rock, p1paper, p1scissors
    p1rock = False
    p1paper = False
    p1scissors = True
    cp1.grid_remove()
    p2com()

def rockp1():
    global p1rock, p1paper, p1scissors
    p1rock = True
    p1paper = False
    p1scissors = False
    cp1.grid_remove()
    p2()
   
def paperp1():
    global p1rock, p1paper, p1scissors
    p1rock = False
    p1paper = True
    p1scissors = False
    cp1.grid_remove()
    p2()
    
def scissorsp1():
    global p1rock, p1paper, p1scissors
    p1rock = False
    p1paper = False
    p1scissors = True
    cp1.grid_remove()
    p2()

def p2():
    global cp2
    win.title("Rock-Paper-Scissors")
    cp2 = Canvas(win, bg = bg, height = "550",width = "550")
    lbl=Label(cp2,text="Inimene 2 valik on:", bg=bg,fg=fg,font="Arial 35", height=1, width=20)
    lbl2=Label(cp2,bg=bg,fg=fg,height=2, width=20)
    btnRock2=Button(cp2, image=rockimage, fg="Black", font="Arial 22", relief=RAISED, width=15, borderwidth=5, command=rockp2)
    btnPaper2=Button(cp2, image=paperimage, fg="Black", font="Arial 22", relief=RAISED, width=15, borderwidth=5, command=paperp2)
    btnScissors2=Button(cp2, image=scissorsimage, fg="Black", font="Arial 22", relief=RAISED, width=15, borderwidth=5, command=scissorsp2)
    ex=Button(cp2, text="Väljuda", fg="red", font="Arial 10", relief=RAISED, width=6, borderwidth=3, command=exit)

    cp2.grid()
    lbl.pack(fill=BOTH, side=TOP)
    btnRock2.pack(fill=BOTH, side=TOP)
    btnPaper2.pack(fill=BOTH, side=TOP)
    btnScissors2.pack(fill=BOTH, side=TOP)
    ex.pack(fill=Y, side=BOTTOM)
    lbl2.pack(fill=BOTH, side=BOTTOM)

def p2com():

    ans = randint(0, 2)
    if ans == 0:
        rockp2com()
    elif ans == 1:
        paperp2com()
    else:
        scissorsp2com()

def rockp2com():
    global p2rock, p2paper, p2scissors
    p2rock = True
    p2paper = False
    p2scissors = False
    choise()

def paperp2com():
    global p2rock, p2paper, p2scissors
    p2rock = False
    p2paper = True
    p2scissors = False
    choise()

def scissorsp2com():
    global p2rock, p2paper, p2scissors
    p2rock = False
    p2paper = False
    p2scissors = True
    choise()


def rockp2():
    global p2rock, p2paper, p2scissors
    p2rock = True
    p2paper = False
    p2scissors = False
    cp2.grid_remove()
    choise()

def paperp2():
    global p2rock, p2paper, p2scissors
    p2rock = False
    p2paper = True
    p2scissors = False
    cp2.grid_remove()
    choise()

def scissorsp2():
    global p2rock, p2paper, p2scissors
    p2rock = False
    p2paper = False
    p2scissors = True
    cp2.grid_remove()
    choise()

def p1draw():
    cdraw.grid_remove()
    if choisee == 1:
        p1()
    if choisee == 2:
        p1com()

def choise():
    global cdraw
    num=0
    winp1=0
    winp2=0
    p1n=0
    p2n=0
    if num < 1:
        if p1rock == True:
            selection = "rock"
        elif p1paper == True:
            selection = "paper"
        elif p1scissors == True:
            selection = "scissors"
    
        if p2rock == True:
            computer_chose = "rock"
        elif p2paper == True:
            computer_chose ="paper"
        elif p2scissors == True:
            computer_chose = "scissors"

    if p1n < 3 and p2n < 3:
        if p1n == 3:
            winp1+=1
            print("Player 1 win")
            num+=1
        if p2n == 3:
            winp2+=1
            print("Player 2 win")
            num+=1
    cdraw = Canvas(win, bg = bg, height = "550",width = "550")
    lbl2=Label(cdraw,bg=bg,fg=fg,height=12, width=20)
    lbl3=Label(cdraw,bg=bg,fg=fg,height=14, width=20)
    btnn=Button(cdraw, text="Jätka", fg="Black", font="Arial 22", relief=RAISED, width=15, borderwidth=5, command=p1draw)
    ex=Button(cdraw, text="Väljuda", fg="red", font="Arial 10", relief=RAISED, width=6, borderwidth=3, command=exit)

    if selection == "rock" and computer_chose == "rock":
        lbl=Label(cdraw,text="Viik", bg=bg,fg=fg,font="Arial 35", width=20)
   
    elif selection == "paper" and computer_chose == "paper":
        lbl=Label(cdraw,text="Viik", bg=bg,fg=fg,font="Arial 35", width=20)

    elif selection == "scissors" and computer_chose == "scissors":
        lbl=Label(cdraw,text="Viik", bg=bg,fg=fg,font="Arial 35", width=20)

    elif selection == "rock" and computer_chose == "scissors":
        p1n+=1
        if robot == True:
            lbl=Label(cdraw,text="Inimene võitis", bg=bg,fg=fg,font="Arial 35", width=20)
        elif robot == False:
            lbl=Label(cdraw,text="1 inimene võitis", bg=bg,fg=fg,font="Arial 35", width=20)

    elif selection == "paper" and computer_chose == "rock":
        p1n+=1
        if robot == True:
            lbl=Label(cdraw,text="Inimene võitis", bg=bg,fg=fg,font="Arial 35", width=20)
        elif robot == False:
            lbl=Label(cdraw,text="1 inimene võitis", bg=bg,fg=fg,font="Arial 35", width=20)

    elif selection == "scissors" and computer_chose == "paper":
        p1n+=1
        if robot == True:
            lbl=Label(cdraw,text="Inimene võitis", bg=bg,fg=fg,font="Arial 35", width=20)
        elif robot == False:
            lbl=Label(cdraw,text="1 inimene võitis", bg=bg,fg=fg,font="Arial 35", width=20)

    elif selection == "scissors" and computer_chose == "rock":
        p2n+=1
        if robot == True:
            lbl=Label(cdraw,text="Robot võitis", bg=bg,fg=fg,font="Arial 35", width=20)
        elif robot == False:
            lbl=Label(cdraw,text="2 inimene võitis", bg=bg,fg=fg,font="Arial 35", width=20)
        


    elif selection == "rock" and computer_chose == "paper":
        p2n+=1
        if robot == True:
            lbl=Label(cdraw,text="Robot võitis", bg=bg,fg=fg,font="Arial 35", width=20)
        elif robot == False:
            lbl=Label(cdraw,text="2 inimene võitis", bg=bg,fg=fg,font="Arial 35", width=20)


    elif selection == "paper" and computer_chose == "scissors":
        p2n+=1
        if robot == True:
            lbl=Label(cdraw,text="Robot võitis", bg=bg,fg=fg,font="Arial 35", width=20)
        elif robot == False:
            lbl=Label(cdraw,text="2 inimene võitis", bg=bg,fg=fg,font="Arial 35", width=20)

    cdraw.grid()
    lbl.pack(fill=X, side=TOP)
    lbl2.pack(fill=Y, side=TOP)
    btnn.pack(fill=Y, side=TOP)
    ex.pack(fill=Y, side=BOTTOM)
    lbl3.pack(fill=Y, side=BOTTOM)


def white():
    global bg, fg
    bg = "white"
    fg = "black"
    c.grid_remove()
    startwinKNB()

def black():
    global bg, fg
    bg = "black"
    fg = "white"
    c.grid_remove()
    startwinKNB()

start()
win.mainloop()