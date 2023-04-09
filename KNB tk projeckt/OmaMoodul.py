from random import *
from tkinter import *
from tkinter import ttk
from math import *
from time import sleep



def startwin():
        global c, win
        win=Tk()
        win.geometry("450x450")
        #win.iconbitmap("logo.ico")
        win.title("Rock-Paper-Scissors")
        c = Canvas(win, bg = "white", height = "600",width = "600")
        lbl=Label(c,text="Rock/Papper/Scissors", bg="white",fg="black",font="Arial 20", width=20)
        btn1=Button(c, text="Start", fg="Black", font="Arial 10", relief=RAISED, width=15, borderwidth=5, command=p1)

        lbl.pack(fill=BOTH, side=TOP)
        btn1.pack(fill=BOTH, side=TOP)
        c.grid()
        win.mainloop()

def p1():
    global can
    c.grid_remove()
    can = Canvas(win, bg = "white", height = "600",width = "600")
    lbl=Label(can,text="P1 choise is:", bg="white",fg="black",font="Arial 20", width=20)
    btnRock1=Button(can, text="Rock", fg="Black", font="Arial 10", relief=RAISED, width=15, borderwidth=5, command=rockp1)
    btnPaper1=Button(can, text="Paper", fg="Black", font="Arial 10", relief=RAISED, width=15, borderwidth=5, command=paperp1)
    btnScissors1=Button(can, text="Scissors", fg="Black", font="Arial 10", relief=RAISED, width=15, borderwidth=5, command=scissorsp1)

    can.grid()
    lbl.pack(fill=BOTH, side=TOP)
    btnRock1.pack(fill=BOTH, side=TOP)
    btnPaper1.pack(fill=BOTH, side=TOP)
    btnScissors1.pack(fill=BOTH, side=TOP)


def rockp1():
    global p1rock, p1paper, p1scissors
    p1rock = True
    p1paper = False
    p1scissors = False
    p2()
   
def paperp1():
    global p1rock, p1paper, p1scissors
    p1rock = False
    p1paper = True
    p1scissors = False
    p2()
    
def scissorsp1():
    global p1rock, p1paper, p1scissors
    p1rock = False
    p1paper = False
    p1scissors = True
    p2()

def p2():
    global canv
    win.title("Rock-Paper-Scissors")
    can.grid_remove()
    canv = Canvas(win, bg = "white", height = "600",width = "600")
    lbl=Label(canv,text="P2 choise is:", bg="white",fg="black",font="Arial 20", width=20)
    btnRock2=Button(canv, text="Rock", fg="Black", font="Arial 10", relief=RAISED, width=15, borderwidth=5, command=rockp2)
    btnPaper2=Button(canv, text="Paper", fg="Black", font="Arial 10", relief=RAISED, width=15, borderwidth=5, command=paperp2)
    btnScissors2=Button(canv, text="Scissors", fg="Black", font="Arial 10", relief=RAISED, width=15, borderwidth=5, command=scissorsp2)

    canv.grid()
    lbl.pack(fill=BOTH, side=TOP)
    btnRock2.pack(fill=BOTH, side=TOP)
    btnPaper2.pack(fill=BOTH, side=TOP)
    btnScissors2.pack(fill=BOTH, side=TOP)

def rockp2():
    global p2rock, p2paper, p2scissors
    p2rock = True
    p2paper = False
    p2scissors = False
    choise()

def paperp2():
    global p2rock, p2paper, p2scissors
    p2rock = False
    p2paper = True
    p2scissors = False
    choise()

def scissorsp2():
    global p2rock, p2paper, p2scissors
    p2rock = False
    p2paper = False
    p2scissors = True
    choise()
    
def draw():
    global canvad
    win.title("Rock-Paper-Scissors")
    canvad = Canvas(win, bg = "white", height = "600",width = "600")
    lbl=Label(canv,text="Draw", bg="white",fg="black",font="Arial 20", width=20)
   
    canvad.grid()
    lbl.pack(fill=BOTH, side=TOP)
    sleep(5)
    choise()

def p1win():
    global canvap1w
    win.title("Rock-Paper-Scissors")
    canvap1w = Canvas(win, bg = "white", height = "600",width = "600")
    lbl=Label(canv,text="P1 win", bg="white",fg="black",font="Arial 20", width=20)
   
    canvap1w.grid()
    lbl.pack(fill=BOTH, side=TOP)
    sleep(5)
    choise()

def p2win():
    global canvap2w
    win.title("Rock-Paper-Scissors")
    canvap2w = Canvas(win, bg = "white", height = "600",width = "600")
    lbl=Label(canv,text="P1 win", bg="white",fg="black",font="Arial 20", width=20)
   
    canvap2w.grid()
    lbl.pack(fill=BOTH, side=TOP)
    sleep(5)
    choise()

num=0
winp1=0
winp2=0
p1=0
p2=0

def choise():
    canv.grid_remove()
    canvad.grid_remove()
    canvap1w.grid_remove()
    canvap2w.grid_remove()
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

    if p1 < 3 and p2 < 3:
        if p1 == 3:
            winp1+=1
            print("Player 1 win")
            num+=1
        if p2 == 3:
            winp2+=1
            print("Player 2 win")
            num+=1


    if selection == "rock" and computer_chose == "rock":
        lbl=Label(canv,text="Draw", bg="white",fg="black",font="Arial 20", width=20)
        canvad.grid()
        lbl.pack(fill=BOTH, side=TOP)
        choise()
    elif selection == "paper" and computer_chose == "paper":
        lbl=Label(canv,text="Draw", bg="white",fg="black",font="Arial 20", width=20)
        canvad.grid()
        lbl.pack(fill=BOTH, side=TOP)
        choise()
    elif selection == "scissors" and computer_chose == "scissors":
        lbl=Label(canv,text="Draw", bg="white",fg="black",font="Arial 20", width=20)
        canvad.grid()
        lbl.pack(fill=BOTH, side=TOP)
        choise()
    elif selection == "rock" and computer_chose == "scissors":
        lbl=Label(canv,text="P1 win", bg="white",fg="black",font="Arial 20", width=20)
        canvap1w.grid()
        lbl.pack(fill=BOTH, side=TOP)
        p1+=1
        sleep(5)
        choise()
    elif selection == "paper" and computer_chose == "rock":
        lbl=Label(canv,text="P1 win", bg="white",fg="black",font="Arial 20", width=20)
        canvap1w.grid()
        lbl.pack(fill=BOTH, side=TOP)
        p1+=1
        sleep(5)
        choise()
    elif selection == "scissors" and computer_chose == "paper":
        lbl=Label(canv,text="P1 win", bg="white",fg="black",font="Arial 20", width=20)
        canvap1w.grid()
        lbl.pack(fill=BOTH, side=TOP)
        p1+=1
        sleep(5)
        choise()
    elif selection == "scissors" and computer_chose == "rock":
        lbl=Label(canv,text="P2 win", bg="white",fg="black",font="Arial 20", width=20)
        canvap2w.grid()
        lbl.pack(fill=BOTH, side=TOP)
        p2+=1
        sleep(5)
        choise()
    elif selection == "rock" and computer_chose == "paper":
        lbl=Label(canv,text="P2 win", bg="white",fg="black",font="Arial 20", width=20)
        canvap2w.grid()
        lbl.pack(fill=BOTH, side=TOP)
        p2+=1
        sleep(5)
        choise()
    elif selection == "paper" and computer_chose == "scissors":
        lbl=Label(canv,text="P2 win", bg="white",fg="black",font="Arial 20", width=20)
        canvap2w.grid()
        lbl.pack(fill=BOTH, side=TOP)
        p2+=1
        sleep(5)
        choise()

#def game():
#    while True:
#        num=0
#        winp1=0
#        winp2=0
#        p1=0
#        p2=0
#        while num < 1:
#            if p1rock == True:
#                selection = "rock"
#            elif p1paper == True:
#                selection = "paper"
#            elif p1scissors == True:
#                selection = "scissors"
    
#            if p2rock == True:
#                computer_chose = "rock"
#            elif p2paper == True:
#                computer_chose ="paper"
#            elif p2scissors == True:
#                computer_chose = "scissors"

#            #if answer == "bot":
#            #    options = [rock, paper, scissors]
#            #    computer_chose = choice(options)
#            #    print("Computer chose:" , computer_chose)
        
#            if p1 < 3 and p2 < 3:
#                if p1 == 3:
#                    winp1+=1
#                    print("Player 1 win")
#                    num+=1
#                if p2 == 3:
#                    winp2+=1
#                    print("Player 2 win")
#                    num+=1
#            elif selection == "rock" and computer_chose == "rock":
#                draw()
#            elif selection == "paper" and computer_chose == "paper":
#                draw()
#            elif selection == "scissors" and computer_chose == "scissors":
#                draw()
#            elif selection == "rock" and computer_chose == "scissors":
#                p1+=1
#                p1win()
#            elif selection == "paper" and computer_chose == "rock":
#                p1+=1
#                p1win()
#            elif selection == "scissors" and computer_chose == "paper":
#                p1+=1
#                p1win()
#            elif selection == "scissors" and computer_chose == "rock":
#                p2lblw.pack()
#                p2+=1
#            elif selection == "rock" and computer_chose == "paper":
#                p2lblw.pack()
#                p2+=1
#            elif selection == "paper" and computer_chose == "scissors":
#                p2lblw.pack
#                p2+=1
        
#        print("Game over")
#        print(f"Ochko p1 {winp1} \n Ochko p2 {winp2}" )
#        a=input("Prodolzhim? da/net ")
#        if a == "da":
#            pass
#        if a == "net":
#            break

    
