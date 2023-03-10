from OmaMoodul import *
palgad=[1200,2500,750,395,1200]
inimesed=["Arhagel","Biba","Coop","Delay","Eeeesports"]
while True:
    print(inimesed)
    print(palgad)
    menu = int(input("Valik:\n1-Lisa andmed\n2-Kustuta andmed\n3-Suurim palk\n4-Väikseim palk\n5-Loetelu sorteerimine\n6-Vordsed palgad\n7-Keskmine palk\n"))
    if menu == 0:
        break
    elif menu == 1:
        inimesed, palgad = Lisa_andmed(inimesed, palgad)
    elif menu == 2:
        inimesed, palgad = Kustutamine(inimesed, palgad)
    elif menu ==3:
        inimesed, palgad = suurim_palk(inimesed, palgad)
    elif menu == 4:
        inimesed, palgad = v_palk(inimesed, palgad)
    elif menu == 5:
        inimesed, palgad = sorterimine(inimesed, palgad)
    elif menu==6:
        inimesed, palgad=Vordsed_palgad(inimesed, palgad)
    elif menu==7:
        inimesed, palgad=Keskmine(inimesed, palgad)
    elif menu==8:
         palgad=top(palgad)
