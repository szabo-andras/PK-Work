""" import datetime
import math
import random

def print_feladat_vege():
    print()
    print("**************************", end="\n\n")

print(" #1. Kérd be a felhasználó nevét. Köszöntsd a felhasználót a saját nevén. ")
felhasznalonev = str(input("Add meg a neved:"))
print("Szervusz",felhasznalonev)

print_feladat_vege()

print("#2. Kérd be a felhasználó magasságát, és írd ki, hogy mennyivel magasabb, mint 100")
magassag=False
while magassag==False:
    try:
        magassag=int(input("hány cm magas vagy?"))
    except:
        print("Adj meg egy számot!")

if 0<magassag<=100:
    print("Te ",100-magassag,"cm-rel alacsonyabb vagy, mint 100cm")
elif 100<magassag:
    print("Te ",magassag-100,"cm-rel magasabb vagy, mint 100cm")
else:
    print("Jajj de negatív vagy")
print_feladat_vege()

print("#3. Kérj be a felhasználótól egy szöveges értéket egy változóba.")
varos = input("Hol születtél? ")

print_feladat_vege()

print("#4. Írasd ki a bekért változó minden második betűjét!")
print(varos[1::2])

print_feladat_vege()

print("#5. Írasd ki a bekért változó minden második betűjét visszafelé!")
print(varos[-2::-2])

print_feladat_vege()

print("#6. Írasd ki a bekért változó minden betűjét a 3. karaktertől visszafelé!")
print(varos[2::-1])

print_feladat_vege()

print("#7. Írasd ki a bekért szöveges változó minden karakterét a harmadik és hatodik karakterek között")
print(varos[2:5:1])

print_feladat_vege()

print("#8. Írasd ki a bekért szöveges változó utolsó előtti karakterét")
print(varos[-2:-1])

print_feladat_vege()

print("#9. Kérd be egy derékszögű háromszög két befogóját, számítsd ki az átfogóját, majd írasd ki két tizedes jegy pontossággal")
 
befogó1=int(input("befogó1:"))
befogó2=int(input("befogó2:"))

def atfogo(befogo1,befogo2):
    return float(pow(pow(befogo1,2)+pow(befogo2,2),0.5))
print(round(atfogo(befogó1,befogó2),2))

print_feladat_vege()

print("#10. Kérd be egy kör sugarát, számítsd ki a kerületét és területét, majd írasd ki egy tizedes jegy pontossággal.")

sugar=int(input("Add meg a sugár hosszát: "))

def kor_terulet():
    return pow(sugar,2)*math.pi

def kor_kerulet():
    return 2*sugar*math.pi

print("Terület: ",round(kor_terulet(),1))
print("Kerület: ",round(kor_kerulet(),1))

print_feladat_vege()

print("#11. Kérd be egy kör sugarát, számítsd ki a kerületét és területét, majd írasd ki három tizedes jegy pontossággal.")

sugar=int(input("Add meg a sugár hosszát: "))

def kor_terulet():
    return pow(sugar,2)*math.pi

def kor_kerulet():
    return 2*sugar*math.pi

print("Terület: ",round(kor_terulet(),3))
print("Kerület: ",round(kor_kerulet(),3))

print_feladat_vege()

print("#12. Írd le a következő logikai összefüggést a fentiek alapján: (A kisebb, mint 5 ÉS B nagyobb egyenlő, mint 6) VAGY A nagyobb, mint B.")
A=int(input("A: "))
B=int(input("B: "))
if (A<5 and B>=6) or A>B:
    pass

print_feladat_vege()

print("#13. Írd le a következő logikai összefüggést a fentiek alapján: A egyenlő-e B-vel?")

if A==B:
    pass

print_feladat_vege()

print("#14. Kő papír olló")

A_nyertes=0
B_nyertes=0
global jatekok_szama
jatekok_szama=0
tovabbi_jatek="i"

def jatekszamolas ():
    global jatekok_szama
    jatekok_szama +=1
    return jatekok_szama

def vegeredmenyvizsgalat(A_nyertes,B_nyertes):
    # A végeredmény: A_nyertes és B_nyertes változók összehasonlításából ered 
    if A_nyertes<B_nyertes:
        print("Összesítésben 'B' játékos nyert")
    elif A_nyertes>B_nyertes:
        print("Összesítésben 'A' játékos nyert")
    else:
        print("Szerintem ez döntetlen",A_nyertes,":",B_nyertes)
while tovabbi_jatek=="i":
    
    while tovabbi_jatek=="i":
        lista={1:"kő", 2:"papír", 3:"olló"}

        A=False
        B=False
        

        while A==False:
            try:
                A=int(input("'A' játékos tipje: (1=Kő, 2=Papír, 3=Olló)"))
            except:
                print("számot adj meg!")
            if 0<A<4:
                pass
            else:
                print("Válassz a 3 lehetőség közül!")
                A=False
        while B==False:
            try:
                B=int(input("'B' játékos tipje: (1=Kő, 2=Papír, 3=Olló)"))
                
            except:
                print("számot adj meg!")
            if 0<B<4:
                pass
            else:
                print("Válassz a 3 lehetőség közül!")
                B=False

        def vizsgalat(A,B):
            #Ezzel a függvénnyel megvizsgáljuk, hogy melyik játékos nyer eredmeny==True, vagy False, amit később 'A' nyert, vagy 'B' nyert-re fogunk változtatni
            eredmeny="meg nincs eredmeny"
            if A==B:
                
                return 0
            elif (A==1 and B==3) or (A==2 and B==1) or (A==3 and B==2):
                return 1
            else:
                return 2    
            
            
           
        print("'A' játékos tippje:", lista[A])
        print("'B' játékos tippje:", lista[B]) 
        
        if vizsgalat(A,B)==0:
            print("Döntetlen")
        elif vizsgalat(A,B)==1:
            A_nyertes = A_nyertes+1
            print("A nyert")
        else:
            B_nyertes=B_nyertes+1
            print("B nyert")
        
        print("A nyertes játszmái:",A_nyertes,":",B_nyertes,":B nyertes játszmái")
        tovabbi_jatek="kerdes"
        
        while tovabbi_jatek !="i":
            tovabbi_jatek=input("Akartok tovább játszani? i=igen, n=nem: ")
            if tovabbi_jatek=="i":
                jatekszamolas()
            elif tovabbi_jatek=="n":
                print("Vége a játéknak")
                print("A játék végeredménye:", A_nyertes,":",B_nyertes)
                break
            else:
                print("'i', vagy 'n' közül válassz")

vegeredmenyvizsgalat(A_nyertes,B_nyertes)
print("lejátszott körök száma: ", jatekszamolas())

print_feladat_vege()
print("# 16 Kérj be egy szöveget a felhasználótól, majd írasd ki a szöveg karaktereit egymás alá. Készítsd el ezt az algoritmus a for és a while ciklus segítségével is.")

szoveg=input("Írj be egy szöveget ide: ")
for i in szoveg:
    print(i)
print()
x=0
while len(szoveg)>x:
    print(szoveg[x])
    x+=1

print_feladat_vege()

print("#17.Készíts egy olyan algoritmust, amely képes értéket adni egy 3 x 3 -as táblázat minden egyes cellájának. (Ehhez két ciklusra lesz szükséges, amelyek egymásba vannak ágyazva. Az egyik lépkedjen végig a táblázat sorain, a másik pedig az oszlopain.)")
oszlopszam=False
while oszlopszam==False:
    try:
        oszlopszam=int(input("hány oszlopot szeretnél? "))
    except:
        print("Számot írj be!")
sorszam=False
while sorszam==False:
    try:
        sorszam=int(input("hány oszlopot szeretnél? "))
    except:
        print("Számot írj be!")
lista_oszlopai=[]

lista_sorai=[]
sor=1
oszlop=1

while sor<=sorszam:
    while oszlop<=oszlopszam:
        lista_oszlopai.append(oszlop)
        oszlop+=1
    lista_sorai.append(lista_oszlopai)
    sor+=1

print(lista_sorai)

print_feladat_vege()

print("#18.Készíts egy függvényt, amely összead két számot és az eredményt adja visszatérési értékként.")
A=int(input("Adj meg egy számot (A)"))
B=int(input("Adj meg egy számot (B)"))
def összeadás_függvény(A,B):
    return A+B

print(összeadás_függvény(A,B))

print_feladat_vege()



print("#19.Készíts egy függvényt, amely elvégzi egy másodfokú egyenlet megoldását. Feltételes utasításra is szükség van a megoldáshoz.")
print("**************************************")

print("", end= "\n\n")
print("#19.Készíts egy függvényt, amely elvégzi egy másodfokú egyenlet megoldását. Feltételes utasításra is szükség van a megoldáshoz.")
print("**************************************")
print("", end= "\n\n")
import math
a=False
b=False
c=False
#Bekérjük az adatokat:
while a==False:
    try:
        a=float(input("Add meg 'a' értékét: "))
    except:
        print("Adj meg egy számot!")
        a=False
while b==False:
    try:
        b=float(input("Add meg 'b' értékét: "))
    except:
        print("Adj meg egy számot!")
while c==False:
    try:
        c=float(input("Add meg 'c' értékét: "))
    except:
        print("Adj meg egy számot!")
#létrehozzuk x,x1 és x2 változókat, hogy később a függvényben használhassuk őket
x1=False
x2=False
x=False

def masodfoku(a,b,c):
    global x
    global x1
    global x2

    print("Na most akkor kiszámolom neked:")
    print()
    print("Először is ellenőrzöm, hogy 'a' értéke nem egyenlő 0-val, mert a képletben 'a' a nevezőben van, ami nem lehet nulla:")
    if a!=0:
        print(f"Szuper!!! 'a' értéke {a}, vagyis nem nulla, ezért mehetünk tovább...")
        print()
        print("Most megvizsgálom a D, diszkrimináns értékét")
        D=(b*b)-(4*a*c) #Kiszámoljuk a gyökjel alatt levő D=diszkrimináns értékét
        print("A diszkrimináns D=",D)
        
        if D>0:
            print("Mivel" ,D, "> 0, - más szóval a diszkrimináns pozitív - ezért az egyenletnek 2 megoldása van, x1, és x2:")
            x1=(-b+math.sqrt(D))/(2*a)
            x2=(-b-math.sqrt(D))/(2*a)
            print()
            print ("x1=",x1)
            print()
            print("x2=",x2)
            return x1, x2
        
        elif D==0:
            print("Mivel a", D,"= 0 ezért az egyenletnek 2 azonos megoldása van, x1 és x2 = x")
            x=(-b+math.sqrt(D))/(2*a)
            print("x=",x)
            return x
        else:
            print("Mivel a ",D,"< 0, ezért a függvény nem metszi az x tengelyt, nincsen valós gyöke")
    else:
        print("'A' értéke nem lehet 0!")

def ellenorzes (x,x1,x2):
    
    
    print("", end= "\n\n")
    print("**************************************")
    print("", end= "\n\n")
    print("ELLENŐRZÉS 'x', VAGY 'x1' és 'x2' behelyettesítésével:")
    print()
    print("A számított értékeink a következők:")
    print("x=",x,"x1=",x1,"x2=",x2)
    print()
    print("Te pedig az alábbi értékeket adtad meg:")
    print("a=",a,"b=",b,"c=",c)
    # Ellenőrizzük az eredményeket közelítő értékkel
    if x1!=False:
        print()
        print("Amit én számoltam az pedig:")
        print(f"x1={x1}, x2={x2}")
        print("", end= "\n\n")
        print("Szóval a nagy kérdés, hogy...")
        print(f"Igaz, hogy: {a}*{x1}*{x1}+b*{x1}+c = 0 ???", round(a*x1*x1+b*x1+c,2) ,"=0")
        print(round(a*x1*x1+b*x1+c,2)==0)
        print()
        print("Igaz, hogy: ", round(a*x2*x2+b*x2+c,2) ,"=0")
        print(round(a*x2*x2+b*x2+c,2)==0)    
        
    elif x!=False:
        print()
        print("Amit én számoltam az pedig:")
        print(f"x={x}")
        print("", end= "\n\n")        
        print("Szóval a nagy kérdés, hogy...")
        print("Igaz, hogy: ", round(a*x*x+b*x+c,2) ,"=0")
        print(round(a*x*x+b*x+c,2)==0)
    else:
        print("nincs megoldás, mert A értéke nem lehet 0")

def ellenorizzuk():
    valasz=False
    while valasz==False:
        valasz=input("Ellenőrizzük, hogy helyesen számoltam-e? (i=Igen, n=Nem): ")
        if valasz=="i":
            ellenorzes(x,x1,x2)
        elif valasz=="n":
            print("Örülök, hogy hiszel nekem és nem kell bizonyítanom az igazamat :-)")
        else:
            print()
            print("Válassz a megadott lehetőségek közül!!!")
            valasz=False

masodfoku(a,b,c)
ellenorizzuk()

print("", end= "\n\n")
print("Vége")

print_feladat_vege()

print("#3. Páros vagy páratlan számot írtunk be?")
szam=True
while szam==True:
    try:
        szam=int(input("Add meg a vizsgálandó számot!"))
    except:
        print("Számot tessék megadni!")

if szam%2==0 and szam!=0:
    print("A",szam, "szám páros")
elif szam%2!=0:
    print("A",szam,"szám páratlan")
else:
    print("A",szam,"nem páros és nem páratlan")

print_feladat_vege()

print("#4. Írjuk ki egy lista x-nél kisebb elemeit!")

lista=[]
listaelem=1
elemszam=int(input("Hány elemes listát szeretnél? "))
while len(lista)!=elemszam:
    lista.append(listaelem)
    listaelem +=1
print(lista)

x=int(input("Hányadik elemig írjuk ki a lista elemeit?"))

for i in range(0,x-1):
    print(lista[i])

print_feladat_vege()
print("#7. Fibonacci sor kiírása! A Fibonacci-számok a matematikában az egyik legismertebb másodrendben rekurzív sorozat elemei. A nulladik eleme 0, az első eleme 1, a további elemeket az előző kettő összegeként kapjuk.")

n=int(input("Milyen hosszú legyen a lista? "))
lista=[]
x=1
y=1

while len(lista)<n:
    lista.append(x)
    tarolo=x
    x=y+x
    y=tarolo

print(lista)
     """

""" 25. Egy autónak van típusa (string), rendszáma (string), tulajdonosa (string), 
lóerőszáma (egész szám), és mérjük benne a megtett kilométerek számát is (integer).
Hozz létre egy dict (szótár) típust, amelyben egy konkrét autó példányt hozol létre 
az általad megadott adatokkal."""

auto={"típus":"Ford Galaxy","rendszam":"LOV-572", "tulajdonos":"Andras", "LE":int(90), "km":int(300000) }
print(auto)

"""26. Írd ki print utasítás segítségével a 25. feladatban létrehozott autó 
típusát és teljesítményét, és a teljesítmény mögé írd a LE (lóerő) mértékegységet. 
Az egész print utasítást egyetlen sorban hozd létre.
"""

print(auto["típus"]," ",auto["LE"],"LE",sep="")

"""27. Hozz létre egy listát, amelyben összesen 3 autó szerepel. 
Az egyes autók értékeit tetszőlegesen beállíthatod, de legyenek egymástól 
különbözőek."""

autolista=["Ford Galaxy", "VW Polo", "Trabant"]

"""28. Sorold fel a 27. feladatban létrehozott lista kulcsait. 
Print utasítás segítségével írd ki a lista tetszőleges elemét.
"""
for kulcs in range(0,len(autolista)):
    print("kulcs",kulcs)
print("28.feladat:",autolista[1])

"""29. Sorold fel a 27. feladatban létrehozott lista tetszőleges elemének kulcsait. Print utasítás segítségével írd ki a lista tetszőleges elemének tetszőleges értékét. 
"""
