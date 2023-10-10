""" A közismert Kő, Papír, Olló játék.
A játék menete:
- a felhasználó eldönti, hogy hány kört akar játszani (1-10-között)
- a felhasználó eldönti, hogy gép ellen, vagy játékos ellen akar-e játszani

- A játékos választ Kő, Papír, Olló közül
- B játékos (vagy a Gép), választ szintén Kő, Papír, vagy Olló közül

- A program összehasonlítja a választűsokat és kiírja, hogy melyik játékos nyerte a kört
- Az összes kör lejátszása után a program kiértékeli, hogy összesítésben melyik játékos nyert
"""

import random
import time





print("",end="\n\n")
print("KŐ, PAPÍR, OLLÓ")
print("",end="\n\n")
A_nyertes = 0
B_nyertes = 0
lejatszott_jatekok_szama = 0
tovabbi_jatek = "i"
gep_elleni = 0
jatekok_osszesen = False
dontetlenek_szama = 0

while not 0 < jatekok_osszesen < 10:
    try:
        jatekok_osszesen = int(input("Hány kört szeretnél játszani?"))
    except:
        print("Számot adj meg")
    if not 0 > jatekok_osszesen >=10:
        print(" 0 és 10 kör között választhatsz")

while not 0 < gep_elleni < 3 :
    try:
        gep_elleni=int(input("Válassz játék típust! (1 = Gép elleni játék, 2 = PVP)"))
    except:
        print("", end = "")
    print("Válassz 1, vagy 2 közül!")

def gondolkodas():
    print("Az én tippem...")
    # Várakozás véletlenszerű időtartamig (pl. 1-3 másodperc)
    varakozas_ido = random.randint(0, 2)
    time.sleep(varakozas_ido)

def jatekszamolas():
    global lejatszott_jatekok_szama
    lejatszott_jatekok_szama += 1
    return lejatszott_jatekok_szama

def vegeredmenyvizsgalat(A_nyertes,B_nyertes):
    # A végeredmény: A_nyertes és B_nyertes változók összehasonlításából ered 
    if A_nyertes < B_nyertes:
        print("ÖSSZESÍTÉSBEN 'B' játékos NYERT")
    elif A_nyertes > B_nyertes:
        print("ÖSSZESÍTÉSBEN 'A' játékos NYERT")
    else:
        print("Szerintem ez DÖNTETLEN",A_nyertes,":",B_nyertes)


while lejatszott_jatekok_szama != jatekok_osszesen:
    jatekszamolas()
    print("\n", lejatszott_jatekok_szama, ". kör:", sep="", end="\n")
    lista = {1:"kő", 2:"papír", 3:"olló"}

    A = False
    B = False
    

    while A == False:
        try:
            A = int(input("'A' játékos tipje: (1=Kő, 2=Papír, 3=Olló)"))
        except:
            print("számot adj meg!")
        if 0 < A < 4:
            pass
        else:
            print("Válassz a 3 lehetőség közül!")
            A = False
    if gep_elleni == 2:
        while B == False:
            try:
                B = int(input("'B' játékos tipje: (1=Kő, 2=Papír, 3=Olló)"))
                
            except:
                print("számot adj meg!")
            if 0 < B < 4:
                pass
            else:
                print("Válassz a 3 lehetőség közül!")
                B = False
    else:
# ide betetttem egy gondolkodást szimuláló függvényt
        gondolkodas()
        B = random.randint(1,3)
        
        
    def vizsgalat(A, B):
        #Ezzel a függvénnyel megvizsgáljuk, hogy melyik játékos nyeri a kört jatszma_eredmeny==True, vagy False, amit később 'A' nyert, vagy 'B' nyert-re fogunk változtatni
        jatszma_eredmeny="meg nincs eredmeny"
        if A == B:    
            return 0
        elif (A == 1 and B == 3) or (A == 2 and B == 1) or (A==3 and B==2):
            return 1
        else:
            return 2    
        
        
        
    print("'A' játékos tippje:", lista[A])
    print("'B' játékos tippje:", lista[B]) 
    
    if vizsgalat(A, B) == 0:
        print("Döntetlen")
        dontetlenek_szama += 1
    elif vizsgalat(A, B) == 1:
        A_nyertes += 1
        print("Ezt a kört 'A' játékos nyerte")
    else:
        B_nyertes += 1
        print("Ezt a kört 'B' játékos nyerte")
    print()
    print("Eredményjelző:", A_nyertes, ":", B_nyertes, end="\n\n")
    tovabbi_jatek = "kerdes"
    
print("", end="\n\n")
print("*********************", "*  Vége a játéknak  *", "*********************", sep="\n", end="\n\n")
print("Döntetlenre végződő játszmák száma: ", dontetlenek_szama, end="\n\n")
print("Végeredmény:", A_nyertes, ":", B_nyertes)

print("", end="\n\n")
vegeredmenyvizsgalat(A_nyertes, B_nyertes)