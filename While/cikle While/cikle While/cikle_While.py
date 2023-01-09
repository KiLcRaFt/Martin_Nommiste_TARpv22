#1

#try:
#    print("Arvuta peast! ...4*100-55")
#    k=1
#    o_vastus=4*100-55
#    vastus=int(input("Lahenda ülesanne ..."))
#    while True:
#        if vastus==o_vastus:
#            break
#        else:
#            print("Viga! Sisesta Õige vastus on ...", )
#            vastus=int(input("Sisesta vastus ..."))
#            k+=1
#    print("Õige vastus! Katsed oli ...",k )
#except:
#    print(TypeError)

#2

#x=0
#while True:
#    if x==30:
#        break
#    elif x%2==1:

#        print(x, end=" ")
#    x+=1

#print("\n For: ")
#for x in range(0,30,1):
#    if x%2==1:
#        print(x, end=" ")


#*** ИГРЫ С ЧИСЛАМИ ***
print("*** NUMBRIDEGA MÄNGUD ***")
print()
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
while 1:
    try:
        a = (abs(int(input("Sisestage täisarv => ")))) #добавил 2 скобки
        break
    except ValueError:
         print("See ei ole täisarv")
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
if a==0:
    print("Nulliga pole mõtet midagi peale hakata")
else:
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Määrake, kui palju paaris ja mitu paaritu numbrit on arvus")
    print()
    c=b=a
    paaris=0 # убрал =
    paaritu=0 # убрал =
    while b > 0: # :
            if b % 2 == 0: # 2 равно
                    paaris += 1 # +=
            else:
                    paaritu += 1 # +=
            b = b // 10 #убрал пробеl  
    print("Paarisarvud:", paaris) # ,
    print("Paaritud numbrid:", paaritu) # ,
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("*Tagurda* sisestatud number")
    print()
    b=0
    while a > 0: # :
        number = a % 10
        a = a // 10
        b = b * 10
        b =+ number #убрал пробеl  
    print("*Ümberpööratud* number", b)
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Syracuse hüpoteesi testimine") #лишняя скобка
    print()
    if c % 2 == 0: # =
        print("с - Paaris arv. Jagame 2.")
    else:
        print("с - Paaritu arv. Korrutame 3, liidame 1 ja jagame 2.")
    while c != 1:
            if c % 2 == 0: # =
                c == c / 2
            else:
                c == (3*c + 1) / 2
                print(round(c), end=" ") # "
                break
    print()
    print("Hüpotees on õige") # "

   