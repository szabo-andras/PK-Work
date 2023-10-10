import random
print("",end="\n\n")
print("KŐ, PAPÍR, OLLÓ")
print("",end="\n\n")
A_nyertes = 0
B_nyertes = 0
lejatszott_jatekok_szama = 0
tovabbi_jatek = "i"
gep_elleni = 0
jatekok_osszesen = False
while not 0 < jatekok_osszesen < 10:
    try:
        jatekok_osszesen = int(input("Hány kört szeretnél játszani?"))
    except:
        print("Számot adj meg")
    print(" 0 és 10 kör között választhatsz")

while not 0 < gep_elleni < 3 :
    try:
        gep_elleni=int(input("Válassz játék típust! (1 = Gép elleni játék, 2 = PVP)"))
    except:
        print("", end = "")
    print("Válassz 1, vagy 2 közül!")

def jatekszamolas():
    global lejatszott_jatekok_szama
    lejatszott_jatekok_szama +=1
    return lejatszott_jatekok_szama

def vegeredmenyvizsgalat(A_nyertes,B_nyertes):
    # A végeredmény: A_nyertes és B_nyertes változók összehasonlításából ered 
    if A_nyertes < B_nyertes:
        print("Összesítésben 'B' játékos nyert")
    elif A_nyertes > B_nyertes:
        print("Összesítésben 'A' játékos nyert")
    else:
        print("Szerintem ez döntetlen",A_nyertes,":",B_nyertes)

while tovabbi_jatek == "i":

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
        B = random.randint(1,3)
        
    def vizsgalat(A, B):
        #Ezzel a függvénnyel megvizsgáljuk, hogy melyik játékos nyer eredmeny==True, vagy False, amit később 'A' nyert, vagy 'B' nyert-re fogunk változtatni
        eredmeny="meg nincs eredmeny"
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
    elif vizsgalat(A, B) == 1:
        A_nyertes += 1
        print("A nyert")
    else:
        B_nyertes += 1
        print("B nyert")
    
    print("A nyertes játszmái:", A_nyertes, ":", B_nyertes, ":B nyertes játszmái")
    tovabbi_jatek = "kerdes"
    
    while tovabbi_jatek != "i":
        tovabbi_jatek = input("Akartok tovább játszani? i=igen, n=nem: ")
        if tovabbi_jatek == "i":
            jatekszamolas()
        elif tovabbi_jatek == "n":
            print("Vége a játéknak")
            print("A játék végeredménye:", A_nyertes, ":", B_nyertes)
            break
        else:
            print("'i', vagy 'n' közül válassz")
print("", end="\n\n")
print("lejátszott körök száma: ", jatekszamolas())

print("", end="\n\n")
vegeredmenyvizsgalat(A_nyertes, B_nyertes)