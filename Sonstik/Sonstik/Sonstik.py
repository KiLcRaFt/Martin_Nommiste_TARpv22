﻿from OmaMoodul import *


rus_list=loe_failist("rus.txt")
est_list=loe_failist("est.txt")
print(rus_list)
print(est_list)
while True:
    v=int(input("1-Tõlge\n2-Uus sõna\n3-Õige viga\n4-Mäng"))
    if v==1:
        tolkimine(rus_list,est_list)
    elif v==2:
        rus_list, est_list=uued_sonad()
    elif v==3:
        print(rus_list,est_list)
        rus_list,est_list=parandus(rus_list,est_list)
        print(rus_list,est_list)
    elif v==4:
        game(rus_list,est_list)

