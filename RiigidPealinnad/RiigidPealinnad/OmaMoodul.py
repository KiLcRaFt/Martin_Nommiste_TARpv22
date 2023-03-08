from random import *

def file(f: dict, s: dict, r: dict, p: dict):
    file=open(f, "r")
    for line in file:
        k, v=line.strip().split("-")
        s[k.strip()] = v.strip()
        r[k]=v
        p[v]=k
    file.close()
    return s, r, p

def riigid_pealinn(r:dict, p:dict):
    ans=int(input("Riik - 1, Pealinn - 2\n"))
    if ans == 1:
        riik = str(input("Riigi nimi.\n"))
        print(r[f"{riik}"])
    elif ans == 2:
        pealinn = str(input("Pelinna nimi.\n"))
        print(p[f"{pealinn}\n"])
    return r, p

def file_add(r:dict, p:dict):
        riik=input("Määra riik: ")
        pealinn=input("Määrake pealinn: ")
        r.update({riik:pealinn})
        p.update({pealinn:riik})
        return r, p

def file_change(r:dict, p:dict):
        riik = str(input("Sisestage riik, mida soovite muuta: "))
        pealinn = str(input("Sisestage pealinn, mida soovite parandada: "))
        r.pop(riik)
        p.pop(pealinn)
        riik2 = str(input("Sisestage uus riik: "))
        pealinn2 = str(input("Sisestage uus pealinn: "))
        r.update({riik2: pealinn2})
        p.update({pealinn2: riik2})
        return r, p

def game(r:dict, p:dict):
    print(r)
    riik=list(r.keys())
    pealinn=list(p.values())
    ko=0
    n = int(input("Kui palju küsimusi soovite?\n"))
    k = int(input("Kas soovite nimetada pealinnad(1) või riik(2)?"))
    for i in range(0,n):
        if k==1:
            rand=choice(riik)
            ind=riik.index(rand)
            print(pealinn[ind])
            sona=input("Sisenema: ")
            if sona in riik[ind]:
                print("Õige")
                ko+=1
            else:
                print("Vale")
        elif k ==2:
            rand=choice(pealinn)
            ind=pealinn.index(rand)
            print(riik[ind])
            sona = input("Sisenema: ")
            if sona in pealinn[ind]:
                print("Õige")
                ko+=1
            else:
                print("Vale")
    percent = ko * 100 // n
    print(percent, "%")