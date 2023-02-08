from datetime import *
#8/02/23
def Lisa_andmed(i:list, p:list):
    """
    Küsib inimese list ja palgad list
    :param list i:inimeste järjend
    :param list p: palgade järjend
    :rtype list, list:
    """
    n=int(input("Mitu inimest: "))
    for j in range(n):
        nimi=input("Sisesta nimi: ")
        palk= int(input("Sisesta palk: "))
        i.append(nimi)
        p.append(palk)
    return i, p

def Kustutamine(i:list, p:list):
    """
    Küsib inimese list ja palgad list
    :param list i:inimeste järjend
    :param list p: palgade järjend
    :rtype list, list:s
    """
    nimi=input("Sisesta nimi: ")
    if nimi in i:
        n=i.count(nimi)
        for j in range(n):
            ind=i.index(nimi)
            i.pop(ind)
            p.pop(ind)
    return i, p

def suurim_palg(i:list, p:list):
    """
    Küsib inimese list ja palgad list
    :param list i:inimeste järjend
    :param list p: palgade järjend
    :rtype list, list:s
    """
