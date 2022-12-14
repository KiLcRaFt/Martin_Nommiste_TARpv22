

print("Tere! olen sinu uus sõber - Python!")
nimi=input("Mis on teie nimi?\n")
print(f"{nimi}, oi kui ilus nimi!")
answer=int(input(f"{nimi}! Kas leian Sinu keha indeksi? 0-ei, 1-jah => "))   
try:
    if answer==1:
            pikkus=int(input("Pikkus? "))
            mass=float(input("Massa? "))
            if pikkus>0 and mass>0:    
                indeks=mass/(0.01*pikkus)**2
                print(f"{nimi}! Sinu keha indeks on: {round(indeks)}")
                if indeks<=16:
                    print("Tervisele ohtlik alakaal")
                if indeks>16 and indeks<=19:
                    print("Alakaal")
                if indeks>19 and indeks<=25:
                    print("Normaalkaal")
                if indeks>25 and indeks<=30:
                    print("Ülekaal")
                if indeks>30 and indeks<=35:
                    print("Rasvumine")
                if indeks>35 and indeks<=40:
                    print("Tugev rasvumine")
                if indeks>40:
                    print("Tervisele ohtlik rasvumine")
            else:
                print("ValueError")
    else:   
        print("Kahju! See on väga kasulik info!\n")
        exit
except:
    print("ValueError")
