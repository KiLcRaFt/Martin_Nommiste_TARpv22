from random import *

def loe_failist(f):
    fail=open(f,'r',encoding="utf-8-sig")
    mas=[] 
    for rida in fail:
        mas.append(rida.strip())
    fail.close()
    return mas
def list_failisse(f,list_):
    fail=open(f,'w',encoding="utf-8-sig")
    for k in list_:
        fail.write(k+"\n")
    fail.close()
    return list_
def salvesta_failisse(f,text):    
    fail=open(f,'a',encoding="utf-8-sig")
    fail.write(text+"\n")
    fail.close()
    mas=[]
    mas=loe_failist(f)
    return mas
def uued_sonad():
    rus_sona=input("Sisesta sõna vene keeles:")
    est_sona=input("Sisesta sõna eesti keeles:")
    rus_list=salvesta_failisse("rus.txt",rus_sona)
    est_list=salvesta_failisse("est.txt",est_sona)
    return rus_list, est_list
def tolkimine(rus_list,est_list):
    slovo=input("Sisestage tõlgitav sõna: ")
    if slovo in rus_list:
        ind=rus_list.index(slovo)
        print(f"{slovo} - {est_list[ind]}")
    elif slovo in est_list:
        ind=est_list.index(slovo)
        print(f"{slovo} - {rus_list[ind]}")
    else:
        print(f"{slovo.upper()} pole sõnastikus")
        v=input("Kas soovite sõnaraamatusse sõna lisada??")
        if v.lower()=="jah": uued_sonad()
def parandus(rus_list,est_list):
    viga=input("Sisestage valesti kirjutatud sõna: ")
    if viga in rus_list:
        ind=rus_list.index(viga)
        print(f"Paar sõna parandatakse{viga} - {est_list[ind]}")
        rus_list.pop(ind)
        est_list.pop(ind)
        rus_list=list_failisse("rus.txt",rus_list)
        est_list=list_failisse("est.txt",est_list)
        uued_sonad()
        
    elif viga in est_list:
        ind=est_list.index(viga)
        print(f"Paar sõna parandatakse{viga} - {rus_list[ind]}")
        rus_list.pop(ind)
        est_list.pop(ind)
        rus_list=list_failisse("rus.txt",rus_list)
        est_list=list_failisse("est.txt",est_list)
        uued_sonad()
    else:
        print(f"{viga.upper()} pole sõnastikus")
    rus_list=loe_failist("rus.txt")
    est_list=loe_failist("est.txt")
    return rus_list,est_list

def game(rus_list,est_list):
    x=[]
    v=k=0
    rus,est=(rus_list,est_list)
    numb=int(input("Kui palju mänge soovite mängida? "))
    for i in range(numb):
        num=randint(0,(len(rus)-1))
        while num in x:
            num=randint(0,(len(rus)-1))
        try:
            keel=int(input("Mis keeles soovite mängida?\n1-vene\n2-eesti "))
        except:
            print("Value Error")
        if keel==1:                                               
            tolk=input(f"Kuidas tõlkida {rus[num]} õige? ") 
            if tolk==est[num]:
                print(f"{keel} vastus on õige")
                print("Õige\n") 
                v+=1
            else:
                print(f"{keel} vastus on vale") 
                print("Vale\n")
                k+=1
        elif keel==2:                                                              
            tolk=input(f"Kuidas tõlkida {est[num] } õige? ") 
            if tolk==rus[num]:
                print(f"{keel} vastus on õige")
                print("Õige\n")
                v+=1
            else:
                print(f"{keel} vastus on vale") 
                print("Vale\n")
                k+=1
        x.append(num)
        resV=v*100//numb
        resK=k*100//numb
    print(f"Õigete sõnade protsent - {resV}%")
    print(f"Valede sõnade protsent - {resK}%")