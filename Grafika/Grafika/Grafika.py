from tkinter import *

k=0
def clicker(event):
    global k
    k+=1
    btn.configure(text=k)
    if k==20:
        btn.configure(fg="purple", text="Harder")
def clickermaha(event):
    global k
    k-=1
    btn.configure(text=k)
    if k==-20:
        btn.configure(fg="red",text="Stop it!")
def tekst_to_lbl(event):
    t=ent.get()
    lbl.configure(text=t)
    ent.delete(0, END)
   


aken=Tk()
aken.geometry("400x500")
aken.title("Minu esimene aken")
lbl=Label(aken,text="Elemendid", bg="green",fg="black",font="Arial 24",height=5,width=15)
btn=Button(aken, text="Press me", font="Arial 22", fg="black", relief=RAISED, width=15, borderwidth=5, )
ent=Entry(aken,fg="purple", bg="lightblue", width=15, font="Arial 22", justify=CENTER)

btn.bind("<Button-1>",clicker) #lkm
btn.bind("<Button-3>",clickermaha) #pkm
ent.bind("<Return>", tekst_to_lbl) #Enter
lbl.pack()
btn.pack(side=LEFT)
ent.pack(side=LEFT)
aken.mainloop()
