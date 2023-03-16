from tkinter import *  


users = {"username":"password"}  
win=Tk()
win.geometry("600x600")

def reg():
    regwin=Tk()
    regwin.title("Registreerimine")
    regwin.geometry("600x600")
    reglabel = Label(regwin,text="Username : ", fg="red", font="Arial 24")
    regname = Entry(regwin,width=32)

    reglabel.pack(fill=BOTH, side=LEFT)
    regname.pack()
    regwin.mainloop()

win.title("Login or Registreerimine")
lbl=Label(win,text="Welcome", bg="grey",fg="black",font="Arial 24",height=5,width=15)
btn1=Button(win, text="Login", font="Arial 22", fg="black", relief=RAISED, width=15, borderwidth=5, )
btn2=Button(win, text="Registreerimine", font="Arial 22", fg="black", relief=RAISED, width=15, borderwidth=5, command=reg)
btn3=Button(win, text="Exit", font="Arial 22", fg="black", relief=RAISED, width=15, borderwidth=5, command=exit)
#ent=Entry(win,fg="purple", bg="lightblue", width=15, font="Arial 22", justify=CENTER)

lbl.pack()
btn1.pack(fill=BOTH, side=TOP)
btn2.pack(fill=BOTH, side=TOP)
btn3.pack(fill=BOTH, side=TOP)

win.mainloop()
















# Beginning function

#def beginning():
#    global registerfirsterror
#    global beginningwindow
#    beginningwindow = Tk()
#    beginningwindow.geometry("215x110+1000+35")
#    chooseloginbutton = Button(beginningwindow,text="LOGIN",command=loginscript)
#    chooseloginbutton.pack(fill=BOTH)
#    chooseregisterbutton = Button(beginningwindow,text="REGISTER",command=registerscript)
#    chooseregisterbutton.pack(fill=BOTH)
#    chooseexitbutton = Button(beginningwindow,text="EXIT",command=sys.exit)
#    chooseexitbutton.pack(fill=BOTH)
#    registerfirsterror = Label(beginningwindow)
#    frame = Frame()
#    frame.pack(pady=2)

## Register script

#def registerscript():
#    global regusername
#    global regpassword
#    global registerwindow
#    global registerverifylabel
#    registerwindow = Tk()
#    registerwindow.geometry("215x150+1000+35")
#    regusernamelabel = Label(registerwindow,text="Username : ")
#    regusernamelabel.pack(fill=BOTH)
#    regusername = Entry(registerwindow,width=32)
#    regusername.pack()
#    regpasswordlabel = Label(registerwindow,text="Password : ")
#    regpasswordlabel.pack(fill=BOTH)
#    regpassword = Entry(registerwindow,width=32)
#    regpassword.pack()
#    frame = Frame()
#    frame.pack(pady=3)
#    registerbutton = Button(registerwindow,text="REGISTER",command=registerverify)
#    registerbutton.pack()
#    frame = Frame()
#    frame.pack(pady=2)
#    backbutton = Button(registerwindow,text="BACK",command=beginning)
#    backbutton.pack()
#    registerverifylabel = Label(registerwindow)
#    registerverifylabel.pack()

## Login script

#def loginscript():
#    global username
#    global password
#    global loginwindow
#    global loginverifylabel
#    try:
#        registerverifylabel["text"] = ""
#        loginwindow = Tk()
#        loginwindow.geometry("215x160+1000+35")
#        usernamelabel = Label(loginwindow,text="Username : ")
#        usernamelabel.pack(fill=BOTH)
#        username = Entry(loginwindow,width=32)
#        username.pack()
#        passwordlabel = Label(loginwindow,text="Password : ")
#        passwordlabel.pack(fill=BOTH)
#        password = Entry(loginwindow,width=32)
#        password.pack()
#        loginbutton = Button(loginwindow,text="LOGIN",command=loginverify)
#        loginbutton.pack()
#        frame = Frame()
#        frame.pack(pady=2)
#        backbutton = Button(loginwindow,text="BACK",command=beginning)
#        backbutton.pack()
#        loginverifylabel = Label(loginwindow)
    
#    except NameError:          # if you try login before create account it will display an error message
#        registerfirsterror.pack()
#        registerfirsterror["text"] = "Please Create Account ! "


#def loginverify():
#    frame = Frame()
#    frame.pack(pady=3)
#    loginverifylabel.pack(fill=BOTH)
#    if username.get() in users.keys():
#        if password.get() == users[username.get()]:       #if username matches password
#            loginverifylabel["text"] = "Login Successful ! "
#        else:
#            loginverifylabel["text"] = "Invalid username or password ! "
#    else:
#        loginverifylabel["text"] = "Invalid username or password ! "


#def registerverify():
#    if regusername.get() in users:    # if you enter a username that you used it will display an error message
#        frame = Frame()
#        frame.pack(pady=2)
#        registerverifylabel["text"] = "This Username Is Taken"
#    else:
#        users[regusername.get()] = regpassword.get()    # else it will add your new username and password in "users" dictionary 
#        beginning()


#beginning()   # Starting program
#mainloop()