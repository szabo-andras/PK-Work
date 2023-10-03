import math
import numbers
""" print("1. Készíts egy függvényt, amely összead két számot és az eredményt adja visszatérési értékként")

def összeadás(a,b):
    összeg=a+b
    return összeg
a=-1
b=-1
while a<0:
    try:
        a=int(input("adj meg egy egész számot (a): "))
    except:
       print("Nem egész számot adtál meg, próbáld meg újra:")
while b<0:
    try:
        b=int(input("adj meg egy egész számot: (b)"))
    except:
        print("Nem egész számot adtál meg, próbáld meg újra:")

print()
print(a,"+",b,"=",összeadás(a,b),sep="")
print() """

print("Készíts egy függvényt, amely elvégzi egy másodfokú egyenlet megoldását. Feltételes utasításra is szükség van a megoldáshoz.")
a=0
while a==0:
    try:
        a=int(input("Adj meg egy számot de nem lehet nulla (a):"))
    except:
        print("!!!Számot adj meg, ami NEM NULLA!!!")

b="hianyzik"
while b=="hianyzik":
    try:
        b=int(input("Adj meg egy számot de nem lehet nulla (b):"))
    except:
        print("!!!Számot adj meg, ami NEM NULLA!!!")

c="hianyzik"
while c=="hianyzik":
    try:
        c=int(input("Adj meg egy számot de nem lehet nulla (c):"))
    except:
        print("!!!Számot adj meg, ami NEM NULLA!!!")
print()
print("A megadott értékeid:","a=",a,"b=",b,"c=",c)
print()

def masodfoku(a,b,c):
    if a != 0:
        print("A diszkrimináns kiszámítása: D=b^2-4*a*c")
        D =  pow (b,2)-4*a*c
        print("Diszkrimináns (D) =",D)
        if D>0: 
            """ ("Az egyenletnek két megoldása lesz, mert a diszkrimináns nagyobb, mint nulla",D,">0") """
            return "Az egyenlet megoldása: x1=",(-b+D**0.5)/(2*a), "x2=", (-b-D**0.5)/(2*a)
        elif D==0:
            return "Az egyenlet megoldása: x=",(-b+D**0.5)/(2*a),
        else:
            return "Az egyenletnek nincs valós gyöke, vagyis nem érinti az x tengelyt"

    else:
        print("Az egyenletnek nincs megoldása, mert a=0")

print()
print(masodfoku(a,b,c))
