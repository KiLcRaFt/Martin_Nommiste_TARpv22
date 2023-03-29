from OmaMoodul import *

riik_pealinn = {}
pealinn_riik = {}
file=open("riigid_pealinnd.txt", 'r')
for line in file:
    k, v = line.strip().split('-')
    riik_pealinn[k] = v
    pealinn_riik[v] = k

while True:
    ans = int(input("Хотите узнать страну? 1\nХотите узнать столицу? 2\nХотите добавить новое значение в словарь? 3\n"))
    if ans == 1:
        riig = str(input("Какая страна?\n"))
        print(riik_pealinn[f"{riig}"], "\n")
    elif ans == 2:
        pealinn = str(input("Какая столица?\n"))
        print(pealinn_riik[f"{pealinn}"], "\n")
    elif ans == 3:
        riik = str(input("Введите название Страны ---> "))
        pealinn = str(input("Введите название Столицы ---> "))
        riik_pealinn.update({f"{riik}": f"{pealinn}"})
        pealinn_riik.update({f"{pealinn}": f"{riik}"})