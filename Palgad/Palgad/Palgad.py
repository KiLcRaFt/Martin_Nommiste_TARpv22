from OmaMoodul import *
palgad=[1200,2500,750,395,1200]
inimesed=["A","B","C","D","E"]
while True:
    print(inimesed)
    print(palgad)
    menu=int(input("Valik:`\n 1-Lisa andmed\n2-Kustuta andmed"))
    if menu==0:
        break
    elif menu==1:
        inimesed, palgad=Lisa_andmed(inimesed, palgad)
    elif menu==2:
        inimesed, palgad=Kustutamine(inimesed, palgad)
