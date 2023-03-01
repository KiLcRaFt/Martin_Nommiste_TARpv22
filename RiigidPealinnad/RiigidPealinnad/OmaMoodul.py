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
    ans=int(input("Страна - 1, Столица - 2\n"))
    if ans == 1:
        riik = str(input("Название страны.\n"))
        print(r[f"{riik}"])
    elif ans == 2:
        pealinn = str(input("Название столицы.\n"))
        print(p[f"{pealinn}\n"])
    return r, p

def file_add(r:dict, p:dict):
        riik=input("Задать страну: ")
        pealinn=input("Задать столицу: ")
        r.update({riik:pealinn})
        p.update({pealinn:riik})
        return r, p

def file_change(r:dict, p:dict):
        riik = str(input("Введите страну которую хотите исправить: "))
        pealinn = str(input("Введите столицу которую хотите исправить: "))
        r.pop(riik)
        p.pop(pealinn)
        riik2 = str(input("Введите новую страну: "))
        pealinn2 = str(input("Введите новую столицу: "))
        r.update({riik2: pealinn2})
        p.update({pealinn2: riik2})
        return r, p

def game(r:dict, p:dict):
    print(r)
    riik=list(r.keys())
    pealinn=list(p.values())
    ko=0
    n = int(input("Сколько вопросов желаете?\n"))
    k = int(input("Желаете называть столицы(1) или страны(2)?"))
    for i in range(0,n):
        if k==1:
            rand=choice(riik)
            ind=riik.index(rand)
            print(pealinn[ind])
            sona=input("Введите: ")
            if sona in riik[ind]:
                print("Правильно")
                ko+=1
            else:
                print("Неверно")
        elif k ==2:
            rand=choice(pealinn)
            ind=pealinn.index(rand)
            print(riik[ind])
            sona = input("Введите: ")
            if sona in pealinn[ind]:
                print("Верно")
                ko+=1
            else:
                print("Неверно")
    percent = ko * 100 // n
    print(percent, "%")