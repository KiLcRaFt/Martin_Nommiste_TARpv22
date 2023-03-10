from random import *
def Lisa_andmed(i:list,p:list):
    """Kirjekdus
    :param list i: Inimeste j�rjend
    :param list p: Palgade j�rjend
    :rtype: list, list
    """
    n=int(input("Mitu inimest: "))
    for j in range(n):
        nimi = input("Sisesta nimi:")
        palk = int(input("Sisesta palk: "))
        i.append(nimi)
        p.append(palk)
    return i,p

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

def suurim_palk(i:list, p:list):
    """
    Küsib inimese list ja palgad list
    :param list i:inimeste järjend
    :param list p: palgade järjend
    :rtype int, str
    """
    palk = max(p)
    ind = p.index(palk)
    nimi = i[ind]

    return palk, nimi

def v_palk(i:list, p:list):
    """Kirljedus...
    :param list i: inimene 
    :parak list p: v_palk
    .rtype int, str
    """

    palk = min(p)
    ind = p.index(palk)
    nimi = i[ind]


    return palk, nimi

def sorterimine(i:list, p:list):
    """Kirljedus...
    :param list i: Inimesed
    :param list p: sortirovka
    :rtype int, str
    """
    v = int(input("1-kahaneb,2-kasvab\n"))
    if v == 1:
        n = len(p)
        for j in range(0,n-1):
            for k in range(j+1,n):
                if p[j]>p[k]:
                    abi =p[j]
                    p[j]=p[k]
                    p[k]=abi
                    abi =i[j]
                    i[j]=i[k]
                    i[k]=abi
    else:
        if v == 2:
            n = len(p)
            for j in range(0,n-1):
                for k in range(j+1,n):
                    if p[j]<p[k]:
                        abi =p[j]
                        p[j]=p[k]
                        p[k]=abi
                        abi =i[j]
                        i[j]=i[k]
                        i[k]=abi
    return i,p

def Vordsed_palgad(i:list, p:list):
    """
    Küsib suurim palg
    :param list i:inimeste järjend
    :param list p: palgade järjend
    :rtype list, list:s
    """
    dublikatid=[x for x in p if p.count(x)>1 ]
    dublikatid=list(set(dublikatid)) #[1200, 2500, 750, 750, 1200] -> [1200, 750]
    for palk in dublikatid:
        n=p.count(palk)
        k=-1
        print(f"{palk} saavad kätte järgmised inimesed:")
        for j in range(n):
            k=p.index(palk,k+1)
            nimi=i[k]
            print(nimi, "saab kätte", palk)


def Keskmine(i:list, p:list):
    list = p
    avg = sum(p) / len(p)
    print("Keskmine palk on ", round(avg,2))
    if avg == avg:
            ind = p.index(avg)
            nimi = i[ind]
            print(nimi)
            ind = p.index(avg,1)
            nimi = i[ind]
            print(nimi)
    return i,p

def top(p:list):
    g = randint(0,2500)
    f = input("1,2\n")
    if f == "1":
        return p > g
    elif f == "2":
        return p < g

    return p