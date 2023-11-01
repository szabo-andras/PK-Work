#1. Írjon egy Python programot hisztogram létrehozásához az adott egész számok listájából.
""" 
lista_hisztogramhoz = [3, 5, 12, 3]

def histogram(lista_hisztogramhoz):
    for i in lista_hisztogramhoz:
        if i != 0:
            print(i*"*", end="", sep="")
        print()    
histogram(lista_hisztogramhoz)
 """
 
#2. Írjon Python programot annak ellenőrzésére, hogy egy megadott érték szerepel-e egy értékcsoportban/listában.

""" 
lista = [12, 18, 23, 45]
a = int(input("melyik számot keressük a listában? "))
print("A lista elemei: ", lista)

if a in lista:
    print(a, "szerepel")
    
else:
    print(a, "NEM szerepel a" )

index = 0    
for i in lista:
    
    if i == a:
        print(f"Az index sorszáma, ahol {a} szerepel: ", index)
    index += 1    
     """
     
    # Alternatív megoldás: is_group_member fügvénnyel

""" 
def is_group_member(lista):
    kereses = int(input("Add meg milyen szöveget keresünk: "))
    if kereses in lista:
        return True
    else:
        return False
    
print(is_group_member(lista)) 
"""


# 3. Írjon Python programot az adott karakterlánc első 2 karakterének n (nem negatív egész
#    szám) másolatának megszerzéséhez. Ha a hossz kevesebb, mint 2, adja vissza az egész
#    karakterlánc n példányát.
""" 
def karaktermennyisegvizsgalat(karakterlanc):
    if len(karakterlanc) < 2:
        karakterek = karakterlánc
    else:
        karakterek = karakterlánc[:2]
    return karakterek

def karakterszorzás(karakterek,szorzószám):
    karakterszorzat = karakterek * szorzószám
    return karakterszorzat

karakterlánc = "3"
szorzószám = 3
karakterek = karaktermennyisegvizsgalat(karakterlánc)

print(karakterszorzás(karakterek, szorzószám)) 
"""

# 4. Írjon egy Python programot a 4-es szám megszámolásához egy adott listában.

lista = [1, 4, 4, 6, 2, 3, 1, 4, "f", 6, 4, "a",4]
"""
talalat = 0
for i in lista:
    if i == 4:
        talalat += 1

print(talalat)
 """
    #Függvényes megoldás:
"""    
keresett_ertek = 0
def szamolas(keresett_ertek, lista):
    '''Ez a függvény megszámolja egy adott helyen (pl. egy lista változóben), hogy hányszor szerepel a keresett érték'''
    indexeken = []
    index = 0
    keresett_ertek = input("Mit keressek? ")
    talalat = 0
    for i in lista:
        try:
            if i == int(keresett_ertek):
                talalat += 1
                indexeken.append(index)
        except:
            pass
        if i == keresett_ertek:
            talalat += 1
            indexeken.append(index)
        index += 1
    def eredmenynyomtatas():
        print(f"A keresett :'{keresett_ertek}' {talalat} alkalommal szerepelt a {lista} listában az alábbi indexeken: {indexeken}")
    eredmenynyomtatas()
    return talalat, indexeken

    

szamolas(keresett_ertek, lista)
"""

# 5. Írjon Python függvényt, hogy megtalálja a maximális és a minimális számot egy számsorozatból. Ne használjon beépített funkciókat.
""" 
szamlista = [1, 2, 1, 2, 5, 2, 34234, 54, 3, 5, 3, 4, 2, -1, -346, 234, -5435]

# Létrehozok (definiálok) egy függvényt:
def max_min_kereses(szamlista):
    '''Ez a függvény a megadott listából (pl. szamlista) kikeresi a legnagyobb, és a legkisebb értékeket
    szüksége van 1 paraméterre, mégpedig a listaváltozó megnevezésére'''
    maximum = False
    minimum = False
    
    for i in szamlista:
        if maximum == False:
            maximum = i
        elif maximum < i:
            maximum = i
        
        if minimum == False:
            minimum = i
        elif minimum > i:
            minimum = i

    print(f"A legnagyobb szám: {maximum}, a legkisebb pedig: {minimum}")
    return maximum, minimum
    
    #meghívom a függvényt:

max_min_kereses(szamlista)
    #Kinyomtatom a függvény eredményét (A 'return' utáni eredményeket)
print(max_min_kereses(szamlista))
"""

#6. Írjon egy Python programot, amely igazra tér vissza, ha a megadott két egész érték egyenlő, illetve összegük vagy különbségük 5.
""" 
szam1 = -10
szam2 = -5

def függvényem(szam1,szam2):
    if szam1 == szam2 or szam1 + szam2 == 5 or szam1 - szam2 == 5 or szam2 - szam1 == 5:
        return True
    else:
        return False
    
print(függvényem(szam1,szam2))
"""

#7. Írjon Python programot két megadott egész összegére! Ha az összeg 15 és 20 között van, akkor 20 legyen az eredmény.
""" 
szam1 = 1
szam2 = 17

def összeg_függvény(szam1, szam2):
    összeg = szam1 + szam2
    if 15 < összeg < 20:
        összeg = 20
    return összeg

print(összeg_függvény(szam1, szam2))
 """
 




# 9. Írjon Python programot két pozitív egész szám legnagyobb közös osztójának kiszámításához.

#Euklideszi megoldás:
""" Euklideszi algoritmus, amely két szám LKO-ját hatékonyan kiszámítja. Íme, hogyan működik:

Vegyük a két számot, amelyek LKO-ját kiszámítjuk.

Használjuk az Euklideszi algoritmust az adott két számra. Az algoritmus lépései a következők:
a. Osszuk el a nagyobb számot a kisebbel.
b. Az osztás utáni maradékot vesszük, és a kisebb szám helyére tesszük.
c. Ismételjük meg az előző két lépést, amíg a maradék 0 lesz.

Amikor a maradék 0 lesz, az algoritmus megáll, és az utolsó nem nulla maradék lesz az LKO.

Például, ha az LKO-t a 48 és 18 számok között kell kiszámítani az Euklideszi algoritmussal:

Osszuk el a 48-at 18-cal. Az eredmény 2, a maradék pedig 12.
Osszuk el a 18-at a maradékkal (12). Az eredmény 1, a maradék pedig 6.
Osszuk el a 12-t a maradékkal (6). Az eredmény 2, a maradék pedig 0.

Amikor a maradék 0, az algoritmus megáll, és az utolsó nem nulla maradék, azaz 6, lesz az LKO.
Az Euklideszi algoritmus lehetővé teszi a legnagyobb közös osztó gyors és hatékony meghatározását anélkül, hogy szükség lenne a számok prímfaktoros felbontására.
"""

""" szam1 = False
szam2 = False

print(
    "\n\nKét egész szám legnagyobb közös osztójának (LKO) megtalálása Euklideszi algoritmussal:",
    end="\n\n")

#Adatbekérés kivételkezeléssel
while szam1 == False:
  try:
    szam1 = int(input("Adj meg egy egész számot (x): "))
  except:
    print(
        "\nHIBA HIBA HIBA\n Szerintem ez nem  egész szám. Próbáld meg még egyszer!",
        end="\n\n")
while szam2 == False:
  try:
    szam2 = int(input("Adj meg egy másik egész számot (y): "))
  except:
    print(
        "\nHIBA HIBA HIBA\n Szerintem ez nem  egész szám. Próbáld meg még egyszer!",
        end="\n\n")


#Függvény:
def euklidesz(x, y):
  '''Ez a függvény a bekért szam1 (x) és szam2 (y) legnagyobb közös osztóját keresi meg úgy, hogy
    1. Elosztja a nagyobb számot a kisebbel.
    2. A kisebb számot (y) behelyettesíti a nagyobb szám helyére (x), majd az osztás utáni maradékot behelyettesíti a kisebb szám helyére (y).
    3. Megismétli meg az előző két lépést, amíg az osztás maradéka 0 lesz.

    Amikor a maradék 0 lesz, az algoritmus megáll, és az utolsó nem nulla maradék (y) lesz a legnagyobb közös osztó (LKO).'''
  print()
  print(f"A {x} és {y} számok legnagyobb közös osztója:")

  #Ha az első szám kisebb, mint a második, akkor fel kell őket cserélni:
  if x < y:
    x, y = y, x

  while x % y != 0:
    x, y = y, x % y

  return y


#Futtatás:
print(euklidesz(szam1, szam2))
 """
 
# 10. Írjon Python programot, ami minden harmadik számot eltávolít és kinyomtat a számok listából, amíg a lista ki nem ürül.

szamok_listaja = [10,20,30,40,50,60,70,80,90]

def eltavolit_minen_harmadikat(lista):
    print(lista)
    uj_lista = []
    eltavolitott_elem = "semmi"
    index_szam = 2
    while len(lista) > 0:
        if len(lista)<3:
            index_szam = 0
        eltavolitott_elem = lista.pop(index_szam)
        uj_lista.append(eltavolitott_elem)
        print(eltavolitott_elem)    
    
    print(uj_lista)    
    
    #még nincsen kész, mivel nem minden 3. elemet veszi ki a listából
  


eltavolit_minen_harmadikat(szamok_listaja)