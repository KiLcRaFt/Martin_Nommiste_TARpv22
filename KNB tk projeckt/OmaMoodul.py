from random import *
from tkinter import *
from tkinter import ttk
from math import *
from time import sleep
from LoginPass import *

#win=Tk()
#win.geometry("450x450")

bg = "white"
fg = "black"

def startwinKNB():
    global c, menubar, win
    #win.iconbitmap("logo.ico")
    win=Tk()
    win.geometry("600x300")
    c = Canvas(win, bg = bg, height = "600",width = "300")
    menubar = Menu(win)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Valge", command=white)
    filemenu.add_command(label="Must", command=black)
    filemenu.add_separator()
    menubar.add_cascade(label="Teema", menu=filemenu)
    lbl=Label(c,text="Kivi/Paber/Käärid", bg=bg,fg=fg,font="Arial 35", width=20)
    btn1=Button(c, text="KOOPERATIVNE", fg="Black", font="Arial 22", relief=RAISED, width=15, borderwidth=5, command=p1)
    btn2=Button(c, text="Arvutiga", fg="Black", font="Arial 22", relief=RAISED, width=15, borderwidth=5, command=p1com)
    ex=Button(c, text="Väljuda", fg="red", font="Arial 10", relief=RAISED, width=6, borderwidth=3, command=exit)

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
    cp1 = Canvas(win, bg = bg, height = "600",width = "300")
    lbl=Label(cp1,text="Inimene 1 valik on:", bg=bg,fg=fg,font="Arial 35", width=20)
    btnRock1=Button(cp1, text="Kivi", fg="Black", font="Arial 22", relief=RAISED, width=15, borderwidth=5, command=rockp1)
    btnPaper1=Button(cp1, text="Paber", fg="Black", font="Arial 22", relief=RAISED, width=15, borderwidth=5, command=paperp1)
    btnScissors1=Button(cp1, text="Käärid", fg="Black", font="Arial 22", relief=RAISED, width=15, borderwidth=5, command=scissorsp1)
    ex=Button(cp1, text="Väljuda", fg="red", font="Arial 10", relief=RAISED, width=6, borderwidth=3, command=exit)

    cp1.grid()
    lbl.pack(fill=BOTH, side=TOP)
    btnRock1.pack(fill=BOTH, side=TOP)
    btnPaper1.pack(fill=BOTH, side=TOP)
    btnScissors1.pack(fill=BOTH, side=TOP)
    ex.pack(fill=Y, side=BOTTOM)

def p1com():
    global cp1, choisee
    c.grid_remove()
    choisee = 2
    cp1 = Canvas(win, bg = bg, height = "600",width = "300")
    lbl=Label(cp1,text="Inimene 1 valik on:", bg=bg,fg=fg,font="Arial 35", width=20)
    btnRock1=Button(cp1, text="Kivi", fg="Black", font="Arial 22", relief=RAISED, width=15, borderwidth=5, command=rockp1com)
    btnPaper1=Button(cp1, text="Paber", fg="Black", font="Arial 22", relief=RAISED, width=15, borderwidth=5, command=paperp1com)
    btnScissors1=Button(cp1, text="Käärid", fg="Black", font="Arial 22", relief=RAISED, width=15, borderwidth=5, command=scissorsp1com)
    ex=Button(cp1, text="Väljuda", fg="red", font="Arial 10", relief=RAISED, width=6, borderwidth=3, command=exit)

    cp1.grid()
    lbl.pack(fill=BOTH, side=TOP)
    btnRock1.pack(fill=BOTH, side=TOP)
    btnPaper1.pack(fill=BOTH, side=TOP)
    btnScissors1.pack(fill=BOTH, side=TOP)
    ex.pack(fill=Y, side=BOTTOM)

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
    cp2 = Canvas(win, bg = bg, height = "600",width = "300")
    lbl=Label(cp2,text="Inimene 2 valik on:", bg=bg,fg=fg,font="Arial 35", width=20)
    btnRock2=Button(cp2, text="Kivi", fg="Black", font="Arial 22", relief=RAISED, width=15, borderwidth=5, command=rockp2)
    btnPaper2=Button(cp2, text="Paber", fg="Black", font="Arial 22", relief=RAISED, width=15, borderwidth=5, command=paperp2)
    btnScissors2=Button(cp2, text="Käärid", fg="Black", font="Arial 22", relief=RAISED, width=15, borderwidth=5, command=scissorsp2)
    ex=Button(cp2, text="Väljuda", fg="red", font="Arial 10", relief=RAISED, width=6, borderwidth=3, command=exit)

    cp2.grid()
    lbl.pack(fill=BOTH, side=TOP)
    btnRock2.pack(fill=BOTH, side=TOP)
    btnPaper2.pack(fill=BOTH, side=TOP)
    btnScissors2.pack(fill=BOTH, side=TOP)
    ex.pack(fill=Y, side=BOTTOM)

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


    if selection == "rock" and computer_chose == "rock":
        global cdraw
        cdraw = Canvas(win, bg = bg, height = "600",width = "300")
        lbl=Label(cdraw,text="Joonistada", bg=bg,fg=fg,font="Arial 35", width=20)
        btnn=Button(cdraw, text="Jätka", fg="Black", font="Arial 22", relief=RAISED, width=15, borderwidth=5, command=p1draw)
        ex=Button(cdraw, text="Väljuda", fg="red", font="Arial 10", relief=RAISED, width=6, borderwidth=3, command=exit)
   
        cdraw.grid()
        lbl.pack(fill=X, side=TOP)
        btnn.pack(fill=Y, side=TOP)
        ex.pack(fill=Y, side=BOTTOM)
    elif selection == "paper" and computer_chose == "paper":
        cdraw = Canvas(win, bg = bg, height = "600",width = "300")
        lbl=Label(cdraw,text="Joonistada", bg=bg,fg=fg,font="Arial 35", width=20)
        btnn=Button(cdraw, text="Jätka", fg="Black", font="Arial 22", relief=RAISED, width=15, borderwidth=5, command=p1draw)
        ex=Button(cdraw, text="Väljuda", fg="red", font="Arial 10", relief=RAISED, width=6, borderwidth=3, command=exit)

        cdraw.grid()
        lbl.pack(fill=X, side=TOP)
        btnn.pack(fill=Y, side=TOP)
        ex.pack(fill=Y, side=BOTTOM)
    elif selection == "scissors" and computer_chose == "scissors":
        cdraw = Canvas(win, bg = bg, height = "600",width = "300")
        lbl=Label(cdraw,text="Joonistada", bg=bg,fg=fg,font="Arial 35", width=20)
        btnn=Button(cdraw, text="Jätka", fg="Black", font="Arial 22", relief=RAISED, width=15, borderwidth=5, command=p1draw)
        ex=Button(cdraw, text="Väljuda", fg="red", font="Arial 10", relief=RAISED, width=6, borderwidth=3, command=exit)

        cdraw.grid()
        lbl.pack(fill=X, side=TOP)
        btnn.pack(fill=Y, side=TOP)
        ex.pack(fill=Y, side=BOTTOM)
    elif selection == "rock" and computer_chose == "scissors":
        p1n+=1
        cdraw = Canvas(win, bg = bg, height = "600",width = "300")
        lbl=Label(cdraw,text="Inimene 1 võita", bg=bg,fg=fg,font="Arial 35", width=20)
        btnn=Button(cdraw, text="Jätka", fg="Black", font="Arial 22", relief=RAISED, width=15, borderwidth=5, command=p1draw)
        ex=Button(cdraw, text="Väljuda", fg="red", font="Arial 10", relief=RAISED, width=6, borderwidth=3, command=exit)

        cdraw.grid()
        lbl.pack(fill=BOTH, side=TOP)
        btnn.pack(fill=Y, side=TOP)
        ex.pack(fill=Y, side=BOTTOM)
    elif selection == "paper" and computer_chose == "rock":
        p1n+=1
        cdraw = Canvas(win, bg = bg, height = "600",width = "300")
        lbl=Label(cdraw,text="Inimene 1 võita", bg=bg,fg=fg,font="Arial 35", width=20)
        btnn=Button(cdraw, text="Jätka", fg="Black", font="Arial 22", relief=RAISED, width=15, borderwidth=5, command=p1draw)
        ex=Button(cdraw, text="Väljuda", fg="red", font="Arial 10", relief=RAISED, width=6, borderwidth=3, command=exit)

        cdraw.grid()
        lbl.pack(fill=BOTH, side=TOP)
        btnn.pack(fill=Y, side=TOP)
        ex.pack(fill=Y, side=BOTTOM)
    elif selection == "scissors" and computer_chose == "paper":
        p1n+=1
        cdraw = Canvas(win, bg = bg, height = "600",width = "300")
        lbl=Label(cdraw,text="Inimene 1 võita", bg=bg,fg=fg,font="Arial 35", width=20)
        btnn=Button(cdraw, text="Jätka", fg="Black", font="Arial 22", relief=RAISED, width=15, borderwidth=5, command=p1draw)
        ex=Button(cdraw, text="Väljuda", fg="red", font="Arial 10", relief=RAISED, width=6, borderwidth=3, command=exit)

        cdraw.grid()
        lbl.pack(fill=BOTH, side=TOP)
        btnn.pack(fill=Y, side=TOP)
        ex.pack(fill=Y, side=BOTTOM)
    elif selection == "scissors" and computer_chose == "rock":
        p2n+=1
        cdraw = Canvas(win, bg = bg, height = "600",width = "300")
        lbl=Label(cdraw,text="Inimene 2 võita", bg=bg,fg=fg,font="Arial 35", width=20)
        btnn=Button(cdraw, text="Jätka", fg="Black", font="Arial 22", relief=RAISED, width=15, borderwidth=5, command=p1draw)
        ex=Button(cdraw, text="Väljuda", fg="red", font="Arial 10", relief=RAISED, width=6, borderwidth=3, command=exit)

        cdraw.grid()
        lbl.pack(fill=BOTH, side=TOP)
        btnn.pack(fill=Y, side=TOP)
        ex.pack(fill=Y, side=BOTTOM)
    elif selection == "rock" and computer_chose == "paper":
        p2n+=1
        cdraw = Canvas(win, bg = bg, height = "600",width = "300")
        lbl=Label(cdraw,text="Inimene 2 võita", bg=bg,fg=fg,font="Arial 35", width=20)
        btnn=Button(cdraw, text="Jätka", fg="Black", font="Arial 22", relief=RAISED, width=15, borderwidth=5, command=p1draw)
        ex=Button(cdraw, text="Väljuda", fg="red", font="Arial 10", relief=RAISED, width=6, borderwidth=3, command=exit)

        cdraw.grid()
        lbl.pack(fill=BOTH, side=TOP)
        btnn.pack(fill=Y, side=TOP)
        ex.pack(fill=Y, side=BOTTOM)
    elif selection == "paper" and computer_chose == "scissors":
        p2n+=1
        cdraw = Canvas(win, bg = bg, height = "600",width = "300")
        lbl=Label(cdraw,text="Inimene 2 võita", bg=bg,fg=fg,font="Arial 35", width=20)
        btnn=Button(cdraw, text="Jätka", fg="Black", font="Arial 22", relief=RAISED, width=15, borderwidth=5, command=p1draw)
        ex=Button(cdraw, text="Väljuda", fg="red", font="Arial 10", relief=RAISED, width=6, borderwidth=3, command=exit)

        cdraw.grid()
        lbl.pack(fill=BOTH, side=TOP)
        btnn.pack(fill=Y, side=TOP)
        ex.pack(fill=Y, side=BOTTOM)

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

