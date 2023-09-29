import datetime
import math
import random
""" #1. Kérd be a felhasználó nevét. Köszöntsd a felhasználót a saját nevén. 
felhasznalonev = str(input("Add meg a neved:"))
print("Szervusz",felhasznalonev)

#2. Kérd be a felhasználó magasságát, és írd ki, hogy mennyivel magasabb, mint 100
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
#3. Kérj be a felhasználótól egy szöveges értéket egy változóba.

varos = input("Hol születtél? ")
#4. Írasd ki a bekért változó minden második betűjét!
print(varos[1::2])

#5. Írasd ki a bekért változó minden második betűjét visszafelé!
print(varos[-2::-2])

#6. Írasd ki a bekért változó minden betűjét a 3. karaktertől visszafelé!
print(varos[2::-1])

#7. Írasd ki a bekért szöveges változó minden karakterét a harmadik és hatodik karakterek között
print(varos[2:5:1])

#8. Írasd ki a bekért szöveges változó utolsó előtti karakterét
print(varos[-2:-1])
"""
#9. Kérd be egy derékszögű háromszög két befogóját, számítsd ki az átfogóját, majd írasd ki két tizedes jegy pontossággal
""" 
befogó1=int(input("befogó1:"))
befogó2=int(input("befogó2:"))

def atfogo(befogo1,befogo2):
    return float(pow(pow(befogo1,2)+pow(befogo2,2),0.5))
print(round(atfogo(befogó1,befogó2),2))
 """
#10. Kérd be egy kör sugarát, számítsd ki a kerületét és területét, majd írasd ki egy tizedes jegy pontossággal.

""" sugar=int(input("Add meg a sugár hosszát: "))

def kor_terulet():
    return pow(sugar,2)*math.pi

def kor_kerulet():
    return 2*sugar*math.pi

print("Terület: ",round(kor_terulet(),1))
print("Kerület: ",round(kor_kerulet(),1)) """

#11. Kérd be egy kör sugarát, számítsd ki a kerületét és területét, majd írasd ki három tizedes jegy pontossággal.

""" sugar=int(input("Add meg a sugár hosszát: "))

def kor_terulet():
    return pow(sugar,2)*math.pi

def kor_kerulet():
    return 2*sugar*math.pi

print("Terület: ",round(kor_terulet(),3))
print("Kerület: ",round(kor_kerulet(),3)) """

#12. Írd le a következő logikai összefüggést a fentiek alapján: (A kisebb, mint 5 ÉS B nagyobb egyenlő, mint 6) VAGY A nagyobb, mint B.
""" A=int(input("A: "))
B=int(input("B: "))
if (A<5 and B>=6) or A>B:
    pass """

#13. Írd le a következő logikai összefüggést a fentiek alapján: A egyenlő-e B-vel?

""" if A==B:
    pass """

#14. Kő papír olló
""" A_nyertes=0
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
 """

# 16 Kérj be egy szöveget a felhasználótól, majd írasd ki a szöveg karaktereit egymás alá. Készítsd el ezt az algoritmus a for és a while ciklus segítségével is.

""" szoveg=input("Írj be egy szöveget ide: ")
for i in szoveg:
    print(i)
print()
x=0
while len(szoveg)>x:
    print(szoveg[x])
    x+=1 """

#17.Készíts egy olyan algoritmust, amely képes értéket adni egy 3 x 3 -as táblázat minden egyes cellájának. (Ehhez két ciklusra lesz szükséges, amelyek egymásba vannak ágyazva. Az egyik lépkedjen végig a táblázat sorain, a másik pedig az oszlopain.)
""" oszlopszam=False
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

print(lista_sorai) """

#18.Készíts egy függvényt, amely összead két számot és az eredményt adja visszatérési értékként.
""" A=int(input("Adj meg egy számot (A)"))
B=int(input("Adj meg egy számot (B)"))
def összeadás_függvény(A,B):
    return A+B

print(összeadás_függvény(A,B)) """
print()
print("**************************") 

print("#19.Készíts egy függvényt, amely elvégzi egy másodfokú egyenlet megoldását. Feltételes utasításra is szükség van a megoldáshoz.")

a=float(input("add meg A értékét"))
b=float(input("add meg B értékét"))
c=float(input("add meg C értékét"))

def masodfoku():
    if a!=0:
        D=pow(b,2)-4*a*c
        print("A diszkrimináns D=",D)
        
        if D>0:
            print("mivel" ,D, "> 0, ezért az egyenletnek 2 megoldása van, x1, és x2:")
            x1=(-b+D)/2*a
            x2=(-b-D)/2*a
            print ("x1=",x1)
            print("x2=",x2)
        elif D==0:
            print("Mivel a", D,"= 0 ezért az egyenletnek 2 azonos megoldása van, x1 és x2 = x")
            x=(-b+xD)/2*a
        else:
            print("Mivel a ",D,"< 0, ezért a függvény nem metszi az x tengelyt, nincsen valós gyöke")

masodfoku() 
print()
print("**************************")


print()
print("**************************")
print("#1. FizzBuzz feladat számok sorban, de ahol 3-mal osztható, ott Fizz, ahol 5-tel ott Buzz, ahol mindkettővel, ott FizzBuzz legyen kiírva")

for i in range(1,31):
    if i%3==0 and i%5!=0:
        print("Fizz")
    elif i%5==0 and i%3 != 0:
        print("Buzz")
    elif i%5==0 and i%3==0:
        print("FizzBuzz")
    else:
        print(i)
print()
print("**************************")
print("#2. Mikor lennél 100 éves?")

import datetime
year = datetime.date.today().year

print("Today's date:", datetime.date.today()) 

eletkor=int(input("Hány éves vagy? "))
kulonbseg=100-eletkor
print("Te",year+kulonbseg,"-ben,", kulonbseg,"év múlva leszel 100 éves")
szuletesi_ev=int(input("Melyik évben születtél? "))
print("Te",szuletesi_ev+100,"-ben,", kulonbseg,"év múlva leszel 100 éves")

print()
print("**************************")

#3. Páros vagy páratlan számot írtunk be?
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

print()
print("**************************")

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

print()
print("**************************")

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




    