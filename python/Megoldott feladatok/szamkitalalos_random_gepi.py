"""Készíts egy szám kitalálós játékot, amely a beírt tippre válaszként megmondja, hogy kisebb, vagy nagyobb a helyes megoldás. A feladatot minél több függvény segítségével oldd meg. """
import random
print()
print("SZÁM KITALÁLÓS JÁTÉK")
print()
print("Gondoltam egy számot 1 és 100 között. Kitalálod?")
SZAM = random.randint(1,100)
seged1=1
seged2=100
tipp = random.randint(seged1,seged2)
i = 0
while SZAM != tipp:
    
    if tipp > SZAM:
        print ("A szám kisebb, mint", tipp)
        seged2=tipp-1
        tipp=random.randint(seged1,seged2)
        
    elif tipp < SZAM:
        print("A szám nagyobb, mint", tipp)
        seged1=tipp+1
        tipp=random.randint(seged1,seged2)
    i += 1
print("BRAVÓ!!!",i,"Lépésből kitaláltad",tipp,"=",SZAM)