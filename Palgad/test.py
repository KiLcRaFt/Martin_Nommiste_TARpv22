from random import *
palgad=[1200,2500,750,395,1200]
inimesed=["Arhagel","Biba","Coop","Delay","Eeeesports"]

def top(p:list):
    g = randint(0,2500)
    avg = list(filter(p))
    return avg > g

print(top(palgad))