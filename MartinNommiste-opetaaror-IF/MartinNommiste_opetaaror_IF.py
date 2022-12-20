from random import Random, randint

#1

#try:
#    nimi=str(input("What is your name? "))
#    if nimi==str("Juku"):
#        print(f"{nimi}, siis lähme kinno!")
#        vana=int(input("Aga kui vana sa oled? "))
#        if vana>0 and vana<=6:
#            print("Okei, siis ostame tasuta pilet")
#        elif vana>6 and vana<=14:
#            print("Okei, siis ostame lastepilet pilet")
#        elif vana>14 and vana<=65:
#            print("Okei, siis ostame täispilet pilet")
#        elif vana>65 and vana<=100:
#            print("Okei, siis ostame sooduspilet pilet")
#        elif vana<1 or vana>100:
#            print("Не лги мне!")
#except:
#    print("TypeError")

#2
#try:
#    nimi1=input("Как звать первого человека? \n")
#    nimi2=input("Как звать второго человека? \n")
#    if nimi1.isalpha()==True and nimi2.isalpha()==True:
#        print(f"{nimi1} и {nimi2}, вы сегодня соседи.")
#    elif nimi1.isalpha()==False or nimi2.isalpha()==False:
#        print("no")
#except:
#    print(TypeError)

#3
#try:
#    a=float(input("Какая длинна пола? "))
#    b=float(input("Какая ширина пола? "))
#    if a>0 and b>0:
#        S=a*b
#        print(f"Площаль пола равна {S}")
#        vibor=str(input("Хотите ли вы сделать ремонт? y/n \n"))
#        if vibor==str("y"):
#            cena=float(input("Какова цена за кв.м? "))
#            if cena>0:    
#                remont=cena*S
#                print(f"Цена замены пола будет состовлять {remont} eur")
#            else:
#                print("Цифра должна быть больше 0")
#        elif vibor==str("n"):
#            print("\n")
#        else:
#            print(TypeError)
#    else:
#        print("Цифра должна быть больше 0")
#except:
#    print(TypeError)

#4
#try:
#    hind=float(input("Mis hind? "))
#    if hind>=700:
#        print("Исходная цена", hind)
#        soodushind=float(hind)*0.7
#        print("Цена со скидкой в 30% будет:", round(soodushind))
#    elif hind<700 and hind>0:
#        print("Исходная цена", hind)
#        print("Скидка начинает действовать начиная с 700 евро.")
#    elif hind<=0:
#        print(f"{hind} меньше или равна 0")
#except:
#    print(TypeError)

#5

#try:
#    degriees=int(input("Сколько градусов? "))
#    if degriees>18:
#        print(degriees, "больше 18 градусов")
#    elif degriees==18:
#        print("Зимой предпочтительнее комнатная температура")
#    else:
#        print(degriees, "меньше 18 градусов")
#except:
#    print(TypeError)

#7

#try:
#    kasv=int(input("Какой у тебя рост? \n"))
#    if kasv>0:
#        if kasv<150:
#            print("У тебя низкий рост")
#        elif kasv>=150 and kasv<180:
#            print("У тебя средний рост")
#        elif kasv>=180:
#            print("У тебя высокий рост")
#    else:
#        print("Неверно")
#except:
#    print(TypeError)

#8

#try:
#    piim=str(input("Kas te soovite piim? y/n \n"))
#    if piim=="y":
#        piimhind=randint(1, 5)
#        sai=str(input("Kas te soovite sai? y/n \n"))
#        if sai=="y":
#            saihind=randint(1, 5)
#            leib=str(input("Kas te soovite leib y/n \n"))
#            if leib=="y":
#                 leibhind=randint(1, 5)
#                 hindkokku=piimhind+saihind+leibhind
#                 print(f"Kokku hind on {hindkokku} eur")
#            elif leib=="n":
#                 hindkokku=piimhind+saihind
#                 print(f"Kokku hind on {hindkokku} eur")
#        elif sai=="n":
#            leib=str(input("Kas te soovite leib y/n \n"))
#            if leib=="y":
#                 leibhind=randint(1, 5)
#                 hindkokku=piimhind+leibhind
#                 print(f"Kokku hind on {hindkokku} eur")
#            elif leib=="n":
#                 hindkokku=piimhind
#                 print(f"Kokku hind on {hindkokku} eur")
#    elif piim=="n":
#        sai=str(input("Kas te soovite sai? y/n \n"))
#        if sai=="y":
#            saihind=randint(1, 5)
#            leib=str(input("Kas te soovite leib y/n \n"))
#            if leib=="y":
#                 leibhind=randint(1, 5)
#                 hindkokku=saihind+leibhind
#                 print(f"Kokku hind on {hindkokku} eur")
#            elif leib=="n":
#                 hindkokku=saihind
#                 print(f"Kokku hind on {hindkokku} eur")
#        elif sai=="n":
#            leib=str(input("Kas te soovite leib y/n \n"))
#            if leib=="y":
#                 leibhind=randint(1, 5)
#                 hindkokku=leibhind
#                 print(f"Kokku hind on {hindkokku} eur")
#            elif leib=="n":
#                 hindkokku=0
#                 print(f"Kokku hind on {hindkokku} eur")
#except:
#    print(TypeError)