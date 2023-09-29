
# FÜGGVÉNY LÉTREHOZÁSA:

def koszones(*args):
    for x in args:
        print(x)

koszones("Hello","Robi",",","Hogy","vagy","?")

# def fuggvenynev() : Létrehozzuk a "fuggvenynev" nevű függvényt a "def" függvénnyel:
# () : a zárójelek között megadhatunk paramétereket a függvénynek, amiket a függvényben használhatunk.
# *args : ezzel tetszőleges számú paramétert tudunk átadni a függvénynek

# KULCSSZAVAS PARAMÉTER MEGADÁSA:

def koszones3(koszones,nev):
    print(koszones, nev)

koszones3(nev = "András", koszones = "Szervusz")

# vagyis a kulcsszavas paraméter esetén, amikor meghívjuk a függvényt, 
# akkor megadhatunk paramétereket különböző sorrendben, a függvény
# viszont a benne szereplő sorrendben használja majd fel. Fent is a
# függvény meghívásakor először a "nev" változót, majd a "koszones" 
# változót adtuk meg, de a függvényen belül, a print sorban adtuk
# meg a kiírás sorrendjét.

# FIX PARAMÉTER MEGADÁSA:

def koszones4(nev4, koszones = "Hello"):
    print(koszones,nev4)

koszones4(nev4="Péter")

# A fix paraméter egy "nem kötelező" paraméter, mivel már eleve
# van egy értéke, amit megadtunk. Tehát a függvény meghívásakor
# nem kell kötelezően megadnunk a zárójelek között.
# Ha nem változtatjuk meg (a függvény meghívásakor), akkor az fixen
# meg van adva. 

#!!! A "nem kötelező paraméter"-t MINDIG a "kötelező paraméter"-ek után kell
# megadni.


# TETSZŐLEGES SZÁMÚ KULCSSZAVAS PARAMÉTER (key words arguments = **kwargs) ÁTADÁSA:

def koszones5(nev, koszones = "Hello",*args,**kwargs):
    print(koszones,nev)
    print(args)
    print(kwargs)

koszones5("Robi", "Hi", "jhfkdj", 12, kw1="ttt", kw2=33)

# 1. a paramétereknél az első helyen mindig a kötelezően megadandó értékeknek kell szerepelnie. (Pl.:nev)
# 2. következő a kulcsszavas paraméter (jelen esetben opcionális, hiszen megadtunk egy kezdeti értéket (koszones = "Hello"))
# 3. ezt követi a tetszőleges számú, nem kulcsszavas paraméter (pozícionális paraméterek) (Pl.: *args)
# 4. majd a tetszőleges számú kulcsszavas paraméter 