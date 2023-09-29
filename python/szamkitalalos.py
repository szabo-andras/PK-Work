"""Készíts egy szám kitalálós játékot, amely a beírt tippre válaszként megmondja, hogy kisebb, vagy nagyobb a helyes megoldás. A feladatot minél több függvény segítségével oldd meg. """
import random
print()
print("SZÁM KITALÁLÓS JÁTÉK")
print()
print("Gondoltam egy számot 1 és 100 között. Kitalálod?")
SZAM=random.randint(1,100)
a=0
i=0
while SZAM!=a:
    
    try:
        a=int(input("Add meg a tipped:"))
    except:
        print("Számot adj meg")
    if a > SZAM:
        print ("A szám kisebb, mint", a)
    elif a<SZAM:
        print("A szám nagyobb, mint", a)
    i+=1
print("BRAVÓ!!!",i,"Lépésből kitaláltad")