import random
print("# 20.Készíts egy szám kitalálós játékot, amely a beírt tippre válaszként megmondja, hogy kisebb, vagy nagyobb a helyes megoldás. A feladatot minél több függvény segítségével oldd meg")

felso_hatar=int(input("Add meg, hogy mi lehet a legnagyobb szám, amire gondolhatok: "))

tippeles_szama=1
tippeles_szama_dict={1:"elso",2:"második",3:"harmadik",4:"negyedik",5:"ötödik",6:"hatodik",7:"hetedik",8:"nyolcadik",9:"kilencedik",10:"tizedik"}
also_hatar=0
random_szam=random.randint(0,felso_hatar)
print(random_szam)
class Tippeles():
    def tippeles_emeles():
        global tippeles_szama
        tippeles_szama = tippeles_szama+1
        return int(tippeles_szama)
    def szam_tippeles():
        print("Add meg a(z)",tippeles_szama_dict[tippeles_szama],"tippedet", also_hatar,"és",felso_hatar,"számok között:" )
        global tipp
        tipp=int(input(""))
        return tipp
    
class Ellenorzes():
    def szamosszehasonlitas():
        global felso_hatar
        global random_szam
        global also_hatar
        global tippeles_szama
        while tippeles_szama<10:
            
            if tipp<random_szam:
                print("Nagyobb számra gondoltam mint: ",tipp, "de kisebbre, mint", felso_hatar)
                also_hatar=tipp
                Tippeles.tippeles_emeles()
                Tippeles.szam_tippeles()
            elif tipp > random_szam:
                print("Kisebb számra gondoltam mint: ",tipp, "de nagyobbra, mint", also_hatar)
                felso_hatar=tipp
                Tippeles.tippeles_emeles()
                Tippeles.szam_tippeles()
            else:
                print(f"Gratulálok, erre a számra gondoltam {tipp}={random_szam}")
                print("Találgatások száma:",tippeles_szama)
                break
Tippeles.szam_tippeles()
Ellenorzes.szamosszehasonlitas()
if tippeles_szama<9:
    print("Gratulálok, kitaláltad a(z)",tippeles_szama_dict[tippeles_szama],"tippelésre")
else:
    print("Nem találtad ki 10 tippelésből. Én nyertem")
print("Vége a játéknak")
