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

#try:
#    n=int(input("Mis toa korteris? "))
#    for i in range(1, n+1):
    
#        t=float(input(f"{i} Temperatuur: "))
#        if t>=18:
#            print("Soe")
#        else:
#            print("Külm")

#except:
#    print(TypeError)

#try:
#    n=int(input("Mis toa korteris? "))
#    for i in range(1, n+1):
    
#        t=float(input(f"{i} Temperatuur: "))
#        if t>=18:
#            print("Soe")
#        else:
#            print("Külm")

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

#p=k=l=0
#kogus=randint(1, 20)
#print("Всего человек", kogus)
#for i in range(1, kogus+1):
#    pikkus=randint(56, 256)
#    if pikkus>0:
#        if pikkus<150:
#            print("У тебя низкий рост")
#            l+=1       
#        elif pikkus>=150 and pikkus<180:
#            print("У тебя средний рост")
#            k+=1
#        elif pikkus>=180:
#            p+=1
#            print("У тебя высокий рост")
#print(f"Высоких: {p}\nСредних: {k}\nНизких: {l}")

#p=k=l=0
#kogus=randint(1, 20)
#print("Всего человек", kogus)
#i=0
#while i<=kogus-1:
#    i+=1
#    pikkus=randint(56, 256)
#    if pikkus>0:
#        if pikkus<150:
#            print("У тебя низкий рост")
#            l+=1       
#        elif pikkus>=150 and pikkus<180:
#            print("У тебя средний рост")
#            k+=1
#        elif pikkus>=180:
#            p+=1
#            print("У тебя высокий рост")
#print(f"Высоких: {p}\nСредних: {k}\nНизких: {l}")

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

#9


#try:
#    a=float(input("Utle pool a "))
#    b=float(input("Utle pool b "))
#    if a==b:
#        print("See on ruut")
#    else:
#        print("See ei ole ruut")
#except:
#    print(TypeError)

a=0
b=1
while a!=b:
    while True:
        try:
            a=float(input("Сторона а:  "))
            break
        except:
            print("Попробуйте ещё раз")
    while True:
        try:
            b=float(input("Сторона б: "))
            break
        except:
            print("Попробуйте ещё раз")
    if a!=b:
        print("Попробуйте ещё раз")
print(f"Это квадрат, его стороны равны {a}")

#10


#try:
#    a=float(input("1 number "))
#    b=float(input("1 number "))
#    c=input("mis märk sa oled +-/ \n ")
#    if c==("+"):
#        print(a+b)
#    elif c==("-"):
#        print(a-b)
#    elif c==(""):
#        print(a*b)
#    elif c==("/"):
#        if b==0:
#            print("Väiksem kui 0")
#        else:
#            print(a/b)
#except:
#    print(TypeError)


#11


#now = datetime.datetime.now()
#try:
#    a=int(input("Sisesta sünniaasta. "))
#except:
#    print(TypeError)
#b=int(now.year)
#c=int(b-a)
#print(c)
#f=c%5
#if f==0:
#    print("teil on juubel")
#else:
#    print("Kui kaju")

#12


#try:
#    a=float(input("sisesta toote hind "))
#    if a<=10:
#        print("sul on soodus 10%",a-a0.1)
#    elif a>10:
#        print("sul on soodus 20%",a-a0.2)
#except:
#    print(TypeError)

#13


#try:
#    a=int(input("Kas sa oled mees?(jah-1 või ei-0)"))
#    if a==1:
#        b=int(input("Kui vana sa oled? "))
#        if b>=16 and b<=18:
#            print("sa sobid")
#    else:
#        print("sa oled naine sest, et sa ei sobi")
#except:
#    print(TypeError)