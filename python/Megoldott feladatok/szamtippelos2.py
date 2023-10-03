import random
print("# 20.Készíts egy szám kitalálós játékot, amely a beírt tippre válaszként megmondja, hogy kisebb, vagy nagyobb a helyes megoldás. A feladatot minél több függvény segítségével oldd meg")
ujra="i"
vesztes=0
nyertes=0
felso_hatar=True
random_szam=0
tippeles_szama=1
tippeles_szama_dict={1:"elso",2:"második",3:"harmadik",4:"negyedik",5:"ötödik",6:"hatodik",7:"hetedik",8:"nyolcadik",9:"kilencedik",10:"tizedik"}
also_hatar=0


def tippeles_emeles():
    global tippeles_szama
    tippeles_szama = tippeles_szama+1
    return int(tippeles_szama)
def szam_tippeles():
    print("Add meg a(z)",tippeles_szama_dict[tippeles_szama],"tippedet", also_hatar,"és",felso_hatar,"számok között:" )
    global tipp
    tipp=int(input(""))
    return tipp
    

def szamosszehasonlitas():
    global felso_hatar
    global random_szam
    global also_hatar
    global tippeles_szama
    global vesztes
    global nyertes
    while tippeles_szama<10:
        
        if tipp<random_szam:
            print("Nagyobb számra gondoltam mint: ",tipp, "de kisebbre, mint", felso_hatar)
            also_hatar=tipp
            tippeles_emeles()
            szam_tippeles()
        elif tipp > random_szam:
            print("Kisebb számra gondoltam mint: ",tipp, "de nagyobbra, mint", also_hatar)
            felso_hatar=tipp
            tippeles_emeles()
            szam_tippeles()
        else:
            print(f"Gratulálok, erre a számra gondoltam {tipp}={random_szam}")
            print("Találgatások száma:",tippeles_szama)
            nyertes+=1
            break

def eredmeny():
    if tippeles_szama<9:
        print("Gratulálok, kitaláltad a(z)",tippeles_szama_dict[tippeles_szama],"tippelésre")
    else:
        print("Nem találtad ki 10 tippelésből. Sajnos most vesztettél")
        print("Vége a játéknak")
        vesztes=vesztes+1

""" OTT TARTOK, HOGY RESETELNI KELL 
AZ ÉRTÉKEKET MINDEN ÚJ JÁTSZMA ELŐTT """

def reset():
    global also_hatar=0


def uj_jatek():
    global ujra
    global felso_hatar
    global random_szam
    felso_hatar=int(input("Add meg, hogy mi lehet a legnagyobb szám, amire gondolhatok: "))
    random_szam=random.randint(0,felso_hatar)
    print(random_szam)
    szam_tippeles()
    szamosszehasonlitas()
    while ujra=="i" or ujra!="n":
        ujra=input("Szeretnél még egyszer játszani? (i: Igen, n: Nem) ")
        if ujra=="i":
            szam_tippeles()
            szamosszehasonlitas()
            eredmeny()
        elif ujra=="n":
            print("Vége")
        else:
            print("Nem jó választ adtál, 'i' vagy 'n' közül válassz!")

def vegeredmeny():
    print("Nyertél:",nyertes,"alkalommal")
    print("Vesztettél:",vesztes,"alkalommal")
    
uj_jatek()
vegeredmeny()
