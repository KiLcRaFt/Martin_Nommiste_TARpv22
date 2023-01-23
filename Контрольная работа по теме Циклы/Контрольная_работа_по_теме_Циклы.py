from random import *

#Ulesanne 1
try:
    n = int(input("Введите число зверьков от 1 - 9: "))
    a = 1
    while n<=9 and n>0 and a<=n:
        for x in range(n):
            print("\n ^---^", end=" \n")
            print("( o o )", end="  \n")
            print(" ! = !/)", end=" \n") 
            a+=1
    else:
        print("Введите число от 1 - 9")
except:
    print(TypeError)

#Ülesanne 2

#n = int(input("Введите число: "))
#pk = int(input("Введите показатель чисел: "))
#if n>0 and pk>0:
#        for i in range(1,n):
#            answer = i**pk
#            if answer<=n:
#                print(answer,end=" ")
#            elif i>n:
#                break
#else:
#    print("Числа должны быть больше 0")

#Ülesanne 3

#opilased = randint(10, 42)
#a = []
#for i in range(10, opilased):
#    hinne = randint(1, 100)
#    a.append(hinne)
#print(f"Самое минимальное колличество ", min(a), "баллов")
#print(f"Самое максимальное колличество ", max(a), "ебаллов")
