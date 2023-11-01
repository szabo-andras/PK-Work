#9 Írjon Python programot két pozitív egész szám legnagyobb közös osztójának kiszámításához!

#Euklideszi megoldás:
""" Euklideszi algoritmus, amely két szám legnagyobb közös osztóját (LKO) hatékonyan kiszámítja. 
Íme, hogyan működik:

Vegyüknk a két számot.

Használjuk az Euklideszi algoritmust az adott két számra. Az algoritmus lépései a következők:
a. Osszuk el a nagyobb számot a kisebbel.
b. Ez után a nagyobb szám helyére a kisebb szám kerül, a kisebb szám helyére pedig az előbbi osztás maradéka.
c. Ismételjük meg az előző két lépést, amíg a maradék 0 lesz.

Amikor a maradék 0, akkor az algoritmus megáll, és az utolsó nem nulla maradék lesz a legkisebb közös osztó (LKO).

Például, ha az LKO-t a 48 és 18 számok között kell kiszámítani az Euklideszi algoritmussal:

Osszuk el a 48-at 18-cal. Az eredmény 2, a maradék pedig 12.
Osszuk el a 18-at a maradékkal (12). Az eredmény 1, a maradék pedig 6.
Osszuk el a 12-t a maradékkal (6). Az eredmény 2, a maradék pedig 0.

Amikor a maradék 0, az algoritmus megáll, és az utolsó nem nulla maradék, azaz 6, lesz az LKO.
Az Euklideszi algoritmus lehetővé teszi a legnagyobb közös osztó gyors és hatékony meghatározását anélkül, hogy szükség lenne a számok prímfaktoros felbontására.
"""

import time
print(
    "\n\nKét egész szám legnagyobb közös osztójának (LKO) megtalálása Euklideszi algoritmussal:",
    end="\n\n")

#Adatbekérés kivételkezeléssel
def adatbekérés (elso_szam, masodik_szam):
  while elso_szam == "nincs megadva érték" or elso_szam == 0:
    try:
      elso_szam = int(input("Adj meg egy egész számot (x), majd nyomj ENTER-t! "))
    except:
      print(
          "\nHIBA HIBA HIBA\n Szerintem ez nem  egész szám. Próbáld meg még egyszer!",
          end="\n\n")
    if elso_szam == 0:
      print("Nullát nem adhatsz meg, mert ezzel a számmal később osztanom kellene, és nullával nem tudok osztani.")
  while masodik_szam == "nincs megadva érték" or masodik_szam == 0:
    try:
      masodik_szam = int(input("Adj meg egy másik egész számot (y) majd nyomj ENTER-t! "))
    except:
      print(
          "\nHIBA HIBA HIBA\n Szerintem ez nem  egész szám. Próbáld meg még egyszer!",
          end="\n\n")
    if masodik_szam == 0:
      print("Nullát nem adhatsz meg, mert ezzel a számmal később osztanom kellene, és nullával nem tudok osztani.")
  return elso_szam, masodik_szam


    

#Függvények:
def euklidesz(x, y):
  '''Ez a függvény a bekért szam1 (x) és szam2 (y) legnagyobb közös osztóját keresi meg úgy, hogy
    1. Elosztja a nagyobb számot a kisebbel.
    2. A kisebb számot (y) behelyettesíti a nagyobb szám helyére (x), majd az osztás utáni maradékot behelyettesíti a kisebb szám helyére (y).
    3. Megismétli az előző két lépést, amíg az osztás maradéka 0 lesz.

    Amikor a maradék 0 lesz, az algoritmus megáll, és az utolsó nem nulla maradék (y) lesz a legnagyobb közös osztó (LKO).'''
  print()
  print(f"A {x} és {y} számok legnagyobb közös osztója: ")

  #Ha az első szám kisebb, mint a második, akkor fel kell őket cserélni:
  if x < y:
    x, y = y, x

  while x % y != 0:
    x, y = y, x % y

  return y

# ISMÉTLÉSI KÉRDÉS FÜGGVÉNYE:
def ismetlesi_kerdes():
  '''Ezzel a függvénnyel megkérdezzük a felhasználót, hogy szeretné-e újból lefuttatni a programot'''
  ismetles = "nincs megadva érték"
  while ismetles == "nincs megadva érték":
    ismetles = input("Szeretnél további LKO-kat keresni? Válassz: i = Igen, n = Nem, majd nyomj ENTER-t! ")
  
    if ismetles == "i":
      if összes_ismétlés_száma % 2 == 0  and ismetles != "n":
        print("!!! RENDBEN, DE ELŐTTE PIHENEK 10 MÁSODPERCET !!!","ELÉGGÉ FÁRASZTÓ EZ A SOK SZÁMOLÁS","Mi lenne, ha addig bedugnád a töltőt?", "...", "ÉHES VAGYOK!!!", sep="\n")
        pihenés_10mp()
        print("Lássuk a következő számpárt!")
      else:
        print("Rendben. Akkor lássuk a következő számpárt!")
      break
    elif ismetles == "n":
      print("Értem", f"Szóval a válaszod: {ismetles}, vagyis NEM.")
    else:
      print()
      print(f"Ezt a választ ({ismetles}) sajnos nem értem. Válassz: i = Igen, n = Nem","Majd nyomj ENTER-t! ", end="\n\n")
      ismetles = "nincs megadva érték"    
  return ismetles


# MEGSZÁMOLJUK, HOGY HÁNYSZOR ISMÉTELTE A PROGRAMOT A FELHASZNÁLÓ:
def ismétlés_számolás(ismetles):
  '''Ennek a függvénynek 1, vagy 0 lesz az eredménye, ami hozzáadódik az "összes_ismétlés_száma" változóhoz'''
  if ismetles == "i":
    további_ismétlés = 1
  else:
    további_ismétlés = 0
  return további_ismétlés


# A PIHENÉS SZIMULÁLÁSÁNAK FÜGGVÉNYE:
def pihenés_10mp():
  '''Ez a függvény a számítógép 10mp-es pihenését szimulálja'''
  print("...")
    
  varakozas_ido = 10
  time.sleep(varakozas_ido)
  print("OK. Folytathatjuk!")



def befejezes():
  '''A program lezárásakor kiírt mondatok'''
  print()
  print(f"A mai napon {összes_ismétlés_száma} alkalommal kérted tőlem, hogy számítsam ki két szám legnagyobb közös osztóját")
  print("Köszönöm a közös munkát.", "Mára végeztünk.", "Szép napot!", sep="\n\n")

#Futtatás:

ismetles = "i"
összes_ismétlés_száma = 1

while ismetles == "i":
  elso_szam = "nincs megadva érték"
  masodik_szam = "nincs megadva érték"
  szamok = adatbekérés(elso_szam, masodik_szam)
  elso_szam = szamok[0]
  masodik_szam = szamok[1]
  print(euklidesz(elso_szam, masodik_szam), end = "\n\n")
  ismetles = ismetlesi_kerdes()
  összes_ismétlés_száma += ismétlés_számolás(ismetles)
befejezes()