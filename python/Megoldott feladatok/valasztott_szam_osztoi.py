"""5. Egy szám osztóinak kiszámítása!"""

#Kiválasztatunk egy számot a felhasználóval:

try:
    szam=int(input("Melyik számnak keresed az osztóit? "))
except:
    print("Számot adj meg légyszíves!")

#Létrehozunk egy üres listát, amibe bele szeretnénk majd tenni a kapott osztókat
osztok=[]

#Végiglépkedünk 0-tól a választott számig minden egész számon, és megvizsgáljuk, hogy osztható-e vele maradék nélkül. Ha igen, akkor hozzáadjuk az osztók listájához

for i in range(1,szam+1):
    if szam%i==0:
        osztok.append(i)

#kiíratjuk a létrejött listát:
print("",end="\n\n")
print(f"A valasztott {szam} osztói a következők:")
print(osztok)