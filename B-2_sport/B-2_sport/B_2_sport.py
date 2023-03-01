from OmaMoodul import *
from random import *

sportlased=[]
tulemused=[]

while True:
   print(sportlased)
   print(tulemused)
   print()
   menu=int(input("0-välju\n1-andmete lisamine\n2-top\n3-sorteerimine suremate tulemuste järel\n4-tulemuste näitamine\n5-diskvalifitseerimine\n6-boonuspukntid\n"))
   if menu==0:
       break
   if menu==1:
       Lisa_andmed(sportlased, tulemused)
   elif menu==2:
       top(sportlased, tulemused)
   elif menu==3:
       Suurim_tulemus(sportlased, tulemused)
   elif menu==4:
       näita_tulemused(sportlased, tulemused)
   elif menu==5:
       diskvalifitseerimine(sportlased, tulemused)
   elif menu==6:
       boonuspunktid(sportlased, tulemused)
   else:
        print("")
