import random

# Ülesanne 0
# Väljund tsüklite abil, paaritute numbritega 1 kuni 50.

#x=0
#while True:
#    if x==50:
#        break
#    elif x%2==1:

#        print(x, end=" ")
#    x+=1

#x=0
#while x<=50:
#    if x%2==1:
#        print(x, end=" ")
#    x+=1

#for x in range(0,50,1):
#    if x%2==1:
#        print(x, end=" ")


# Ülesanne 10
# Programm väljastab ainult 5ga jaguvad arvud 1-100.

#x=1
#while True:
#    if x>100:
#        break
#    elif x%5==0:

#        print(x, end=" ")
#    x+=1

#x=1
#while x<=100:
#    if x%5==0:
#        print(x, end=" ")
#    x+=1

#for x in range(1,101,1):
#    if x%5==0:
#        print(x, end=" ")

#Ülesanne 9
# Koosta programm, mis tekitab automaatselt viiega korrutustabeli.

#x=1
#n=1
#while True:
#    if x>50:
#        break
#    elif x%5==0:
#        print(f"5 x {n} = {x}")
#        n+=1
#    x+=1

#x=1
#n=1
#while x<=50:
#        if x%5==0:
#            print(f"5 x {n} = {x}")
#            n+=1
#        x+=1

#x=1
#n=1
#for x in range(1,51,1):
#    if x%5==0:
#        print(f"5 x {n} = {x}")
#        n+=1
#    x+=1

#Ülesanne 17

#try:
#    num_horiz=int(input("Sissesta ruutude arv horisontaalselt ==> \n"))
#    num_vert=int(input("Sissesta ruutude arv vertikalselt ==> \n"))
#    for y in range (num_vert):
#        for x in range(num_horiz):
#            print("O", end=" ")
#        print("")
#except:
#    print(ValueError)

# Практическая работа "Проверка знаний по математике"
print("Проверка знаний по математике")
print("Правила просты.\n Вам доступны 3 уровня сложности. \n На первом уровне вам доступны действия +,- \n На втором уровне вам доступны действия +,-,*,/ \n На третьем уровне вам доступны действия +,-,*,/, **")
try:
    while True:
        tase=int(input("Уровень 1, Уровень 2, Уровень 3? 1/2/3 ===> "))
        if tase<=3 and tase>=1:
            count=int(input("Какое колличесто примеров вы хотите? ===> "))
            x=1
            while tase==1:
                while x <= count:
                    a = random.randint(1, 99)
                    b = random.randint(1, 99)
                    action = random.randint(1, 2)
                    if action==1:
                        answer=a+b
                        panswer=int(input(f"{a} + {b} = "))
                        if answer==panswer:
                            print("Great")
                            x+=1
                        else:
                            print("Wrong")
                    elif action==2:
                        answer=a-b
                        panswer=int(input(f"{a} - {b} = "))
                        if answer==panswer:
                            print("Great")
                            x+=1
                        else:
                            print("Wrong")    
                break                 
            while tase==2:
                while x <= count:
                    a = random.randint(1, 99)
                    b = random.randint(1, 99)
                    action = random.randint(1, 4)
                    if action==1:
                        answer=a+b
                        panswer=int(input(f"{a} + {b} = "))
                        if answer==panswer:
                            print("Great")
                            x+=1
                        else:
                            print("Wrong")
                    elif action==2:
                        answer=a-b
                        panswer=int(input(f"{a} - {b} = "))
                        if answer==panswer:
                            print("Great")
                            x+=1
                        else:
                            print("Wrong")
                    elif action==3:
                        answer=a*b
                        panswer=int(input(f"{a} * {b} = "))
                        if answer==panswer:
                            print("Great")
                            x+=1
                        else:
                            print("Wrong")
                    elif action==4:
                        a1=random.randint(10, 100)
                        b1=random.randint(1, 10)
                        answer=round(a1/b1, 0)
                        panswer=float(input(f"(Нужно округлить до целго) {a1} / {b1} = "))
                        if answer==panswer:
                            print("Great")
                            x+=1
                        else:
                            print("Wrong")       
                break         
            while tase==3:
                while x <= count:
                    a = random.randint(1, 99)
                    b = random.randint(1, 99)
                    action = random.randint(1, 5)
                    if action==1:
                        answer=a+b
                        panswer=int(input(f"{a} + {b} = "))
                        if answer==panswer:
                            print("Great")
                            x+=1
                        else:
                            print("Wrong")
                    elif action==2:
                        answer=a-b
                        panswer=int(input(f"{a} - {b} = "))
                        if answer==panswer:
                            print("Great")
                            x+=1
                        else:
                            print("Wrong")
                    elif action==3:
                        answer=a*b
                        panswer=int(input(f"{a} * {b} = "))
                        if answer==panswer:
                            print("Great")
                            x+=1
                        else:
                            print("Wrong")
                    elif action==4:
                        a1=random.randint(10, 100)
                        b1=random.randint(1, 10)
                        answer=round(a1/b1, 0)
                        panswer=float(input(f"(Нужно округлить до целго) {a1} / {b1} = "))
                        if answer==panswer:
                            print("Great")
                            x+=1
                        else:
                            print("Wrong")
                    elif action==5:
                        a1=random.randint(1, 10)
                        b1=random.randint(2, 4)
                        answer=a1**b1
                        panswer=int(input(f"{a1} ** {b1} = "))
                        if answer==panswer:
                            print("Great")
                            x+=1
                        else:
                            print("Wrong")                
                break 
            print("Вы вычислили все примеры!")
        else:
            print("Введите число от 1 до 3")
except:
    print(TypeError)