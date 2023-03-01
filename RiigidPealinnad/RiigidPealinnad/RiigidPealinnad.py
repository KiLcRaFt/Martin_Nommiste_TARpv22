from OmaMoodul import *

sonastik={}
riik_pealinn = {}
pealinn_riik ={}

while True:
    menu=int(input("Показать словарь - 1\nНайти страну/столицу - 2\nДобавить в словарь - 3\nИсправить в словаре - 4\nЗакрыть - 0\n"))
    x = 0
    if x < 1:
        file("RiikPealinn.txt", sonastik, riik_pealinn, pealinn_riik)
        x += 1
    if menu == 0:
        break
    elif menu == 1:
        print(riik_pealinn)
    elif menu == 2:
        riigid_pealinn(riik_pealinn, pealinn_riik)
    elif menu == 3:
        file_add(riik_pealinn, pealinn_riik)
    elif menu == 4:
        file_change(riik_pealinn, pealinn_riik)
    elif menu == 5:
        game(riik_pealinn, pealinn_riik)
