from random import *
from tkinter import *
from tkinter import ttk
from math import *
from time import sleep


win=Tk()
win.geometry("450x450")

def startwinKNB():
    global c
    win.iconbitmap("logo.ico")
    win.title("Rock-Paper-Scissors")
    c = Canvas(win, bg = "white", height = "450",width = "450")
    lbl=Label(c,text="Rock/Papper/Scissors", bg="white",fg="black",font="Arial 20", width=20)
    btn1=Button(c, text="Start", fg="Black", font="Arial 20", relief=RAISED, width=15, borderwidth=5, command=p1)

    c.grid()
    lbl.pack(fill=X, side=TOP)
    btn1.pack(fill=Y, side=TOP)
 

def p1():
    global cp1
    c.grid_remove()
    cp1 = Canvas(win, bg = "white", height = "450",width = "450")
    lbl=Label(cp1,text="P1 choise is:", bg="white",fg="black",font="Arial 20", width=20)
    btnRock1=Button(cp1, text="Rock", fg="Black", font="Arial 10", relief=RAISED, width=15, borderwidth=5, command=rockp1)
    btnPaper1=Button(cp1, text="Paper", fg="Black", font="Arial 10", relief=RAISED, width=15, borderwidth=5, command=paperp1)
    btnScissors1=Button(cp1, text="Scissors", fg="Black", font="Arial 10", relief=RAISED, width=15, borderwidth=5, command=scissorsp1)

    cp1.grid()
    lbl.pack(fill=BOTH, side=TOP)
    btnRock1.pack(fill=BOTH, side=TOP)
    btnPaper1.pack(fill=BOTH, side=TOP)
    btnScissors1.pack(fill=BOTH, side=TOP)


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
    cp2 = Canvas(win, bg = "white", height = "600",width = "600")
    lbl=Label(cp2,text="P2 choise is:", bg="white",fg="black",font="Arial 20", width=20)
    btnRock2=Button(cp2, text="Rock", fg="Black", font="Arial 10", relief=RAISED, width=15, borderwidth=5, command=rockp2)
    btnPaper2=Button(cp2, text="Paper", fg="Black", font="Arial 10", relief=RAISED, width=15, borderwidth=5, command=paperp2)
    btnScissors2=Button(cp2, text="Scissors", fg="Black", font="Arial 10", relief=RAISED, width=15, borderwidth=5, command=scissorsp2)

    cp2.grid()
    lbl.pack(fill=BOTH, side=TOP)
    btnRock2.pack(fill=BOTH, side=TOP)
    btnPaper2.pack(fill=BOTH, side=TOP)
    btnScissors2.pack(fill=BOTH, side=TOP)

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
    p1()

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
        cdraw = Canvas(win, bg = "white", height = "600",width = "600")
        lbl=Label(cdraw,text="Draw", bg="white",fg="black",font="Arial 20", width=20)
        btnn=Button(cdraw, text="Continue", fg="Black", font="Arial 20", relief=RAISED, width=15, borderwidth=5, command=p1draw)
   
        cdraw.grid()
        lbl.pack(fill=X, side=TOP)
        btnn.pack(fill=Y, side=TOP)
    elif selection == "paper" and computer_chose == "paper":
        cdraw = Canvas(win, bg = "white", height = "600",width = "600")
        lbl=Label(cdraw,text="Draw", bg="white",fg="black",font="Arial 20", width=20)
        btnn=Button(cdraw, text="Continue", fg="Black", font="Arial 20", relief=RAISED, width=15, borderwidth=5, command=p1draw)
   
        cdraw.grid()
        lbl.pack(fill=X, side=TOP)
        btnn.pack(fill=Y, side=TOP)
    elif selection == "scissors" and computer_chose == "scissors":
        cdraw = Canvas(win, bg = "white", height = "600",width = "600")
        lbl=Label(cdraw,text="Draw", bg="white",fg="black",font="Arial 20", width=20)
        btnn=Button(cdraw, text="Continue", fg="Black", font="Arial 20", relief=RAISED, width=15, borderwidth=5, command=p1draw)
   
        cdraw.grid()
        lbl.pack(fill=X, side=TOP)
        btnn.pack(fill=Y, side=TOP)
    elif selection == "rock" and computer_chose == "scissors":
        p1n+=1
        cdraw = Canvas(win, bg = "white", height = "600",width = "600")
        lbl=Label(cdraw,text="P1 win", bg="white",fg="black",font="Arial 20", width=20)
        btnn=Button(cdraw, text="Continue", fg="Black", font="Arial 20", relief=RAISED, width=15, borderwidth=5, command=p1draw)
   
        cdraw.grid()
        lbl.pack(fill=BOTH, side=TOP)
        btnn.pack(fill=Y, side=TOP)
    elif selection == "paper" and computer_chose == "rock":
        p1n+=1
        cdraw = Canvas(win, bg = "white", height = "600",width = "600")
        lbl=Label(cdraw,text="P1 win", bg="white",fg="black",font="Arial 20", width=20)
        btnn=Button(cdraw, text="Continue", fg="Black", font="Arial 20", relief=RAISED, width=15, borderwidth=5, command=p1draw)
   
        cdraw.grid()
        lbl.pack(fill=BOTH, side=TOP)
        btnn.pack(fill=Y, side=TOP)
    elif selection == "scissors" and computer_chose == "paper":
        p1n+=1
        cdraw = Canvas(win, bg = "white", height = "600",width = "600")
        lbl=Label(cdraw,text="P1 win", bg="white",fg="black",font="Arial 20", width=20)
        btnn=Button(cdraw, text="Continue", fg="Black", font="Arial 20", relief=RAISED, width=15, borderwidth=5, command=p1draw)
   
        cdraw.grid()
        lbl.pack(fill=BOTH, side=TOP)
        btnn.pack(fill=Y, side=TOP)
    elif selection == "scissors" and computer_chose == "rock":
        p2n+=1
        cdraw = Canvas(win, bg = "white", height = "600",width = "600")
        lbl=Label(cdraw,text="P2 win", bg="white",fg="black",font="Arial 20", width=20)
        btnn=Button(cdraw, text="Continue", fg="Black", font="Arial 20", relief=RAISED, width=15, borderwidth=5, command=p1draw)
   
        cdraw.grid()
        lbl.pack(fill=BOTH, side=TOP)
        btnn.pack(fill=Y, side=TOP)
    elif selection == "rock" and computer_chose == "paper":
        p2n+=1
        cdraw = Canvas(win, bg = "white", height = "600",width = "600")
        lbl=Label(cdraw,text="P2 win", bg="white",fg="black",font="Arial 20", width=20)
        btnn=Button(cdraw, text="Continue", fg="Black", font="Arial 20", relief=RAISED, width=15, borderwidth=5, command=p1draw)
   
        cdraw.grid()
        lbl.pack(fill=BOTH, side=TOP)
        btnn.pack(fill=Y, side=TOP)
    elif selection == "paper" and computer_chose == "scissors":
        p2n+=1
        cdraw = Canvas(win, bg = "white", height = "600",width = "600")
        lbl=Label(cdraw,text="P2 win", bg="white",fg="black",font="Arial 20", width=20)
        btnn=Button(cdraw, text="Continue", fg="Black", font="Arial 20", relief=RAISED, width=15, borderwidth=5, command=p1draw)
   
        cdraw.grid()
        lbl.pack(fill=BOTH, side=TOP)
        btnn.pack(fill=Y, side=TOP)



