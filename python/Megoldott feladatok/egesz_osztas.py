import os

os.system('clear')
print("Ebben a feladatban azt fogjuk vizsgálni, hogy egy szám osztható-e 3-mal és 5-tel egyaránt maradék nélkül")

a = int (input("Írj be egy számot: "))

import os

os.system('clear')
print("a megadott számot ellenőriztem és arra az eredményre jutottam, hogy:")
print()
if ((a%3==0) and (a%5==0)):
    print("ez a szám osztható maradék nélkül 3-mal és 5-tel is")
elif (a%3==0):
    print("ez a szám csak 3-mal osztható maradék nélkül,")
    print("5-tel nem")
elif(a%5==0):
    print("Ez a szám csak 5-tel osztható maradék nélkül,")
    print(" 3-mal nem")
else:
    print("Ez a szám nem osztható 3-mal és 5-tel sem maradék nélkül")
 