from OmaMoodul import *
palgad=[1200,2500,750,395,1200]
inimesed=["Arhagel","Biba","Coop","Delay","Eeeesports"]
while True:
    print(inimesed)
    print(palgad)
    menu=int(input("Valik:\n 1-Lisa andmed\n 2-Kustuta andmed\n 3-Suurim palg\n 4-Väiksem andmed\n 5-Sorteerimine\n 6-Vordsed palgad\n"))
    if menu==0:
        break
    elif menu==1:
        inimesed, palgad=Lisa_andmed(inimesed, palgad)
    elif menu==2:
        inimesed, palgad=Kustutamine(inimesed, palgad)
    elif menu==3:
        inimesed, palgad=suurim_palg(inimesed, palgad)
    elif menu==4:
        inimesed, palgad=väiksem_palg(inimesed, palgad)
    elif menu==5:
        inimesed, palgad=Sorteerimine(inimesed, palgad)
    elif menu==6:
        inimesed, palgad=Vordsed_palgad(inimesed, palgad)
