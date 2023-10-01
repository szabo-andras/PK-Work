
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



    
    
    


    



