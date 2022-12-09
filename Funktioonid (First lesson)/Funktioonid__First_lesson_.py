from math import *
from xml.etree.ElementTree import PI # импортированы все функции
#import math    math.function()

# 08/12/2022

#print("hello world") # вывод информации на экран
#text=input("something: ") # ввод информации в ввиде str
#print() #пустая строка
#print(f"{text}, yep")
#print(text, ", agree houmie") # автоматический пробел
#print(text+", samurai") # str+str
#number=int(input("how much did u do this? ")) # int(str)
#print(text+f", u did it for {number} times")
#number+=10
#print(text+", u did it for "+str(number)+" times")

print()
print("Равная площадь прямоугольника и круга")
a=float(input("Длинна: "))
b=float(input("Ширина: "))
S=a*b # +, -, *, /, //, **, %
P=2*a+2*b
d=round(sqrt(a**2+b**2), 2) # round (num, x) x= до какого знака после запятой нужно округлить
r=round(sqrt(S/pi), 2)
print(f"\n Площадь: {S}\n Периметр: {P}\n Диагональ: {d}\n Радиус окружности: {r}")
