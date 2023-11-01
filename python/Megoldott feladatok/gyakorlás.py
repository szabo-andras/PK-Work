#11. Írjon Python programot a derékszögű háromszög harmadik oldalának kiszámításához két megadott oldalról.
""" 
a = False
b = False

while a == False:
    try:
        a = int(input("Add meg az egyik befogót (a), majd nyomj Enter-t: "))
    except:
        print("Légyszíves számot adj meg!")

while b == False:
    try:
        b = int(input("Add meg a másik befogót (b), majd nyomj Enter-t: "))
    except:
        print("Légyszíves számot adj meg!")
        
def pythagoras(x,y):
    '''A függvény a Pitagorasz-tétellel, 2 tizedes pontossággal kliszámolja x-és y-változókból az "atfogo"-változót, ami a derékszögű háromszög a, b, és c oldalainak felel meg'''
    atfogo = pow((x*x + y*y),0.5)
    print("A c oldal hossza: ", atfogo)
    return round(atfogo,2)

print(pythagoras(a,b))
 """

#13. Írjon egy Python programot, amely elfogad egy pozitív számot, és kivonja ebből a számból a számjegyeinek összegét és így tovább. Addig folytassa ezt a műveletet, amíg a szám pozitív marad. Adja vissza az ismétlések számát.

def számbekérés():
    szám = False
    while szám == False:
        try:
            szám = int(input("Adj meg egy pozitív egész számot (szám), majd nyomj Enter-t: "))
        except:
            print("Légyszíves számot adj meg!")
    return szám

"""
def művelet(szám):
    '''Ez a függvény visszadaja az ismétlések számát'''
    def számjegyek_összege(szám):
        '''Ez a függvény kiszámolja a neki "szám" változóban megadott szám számjegyeinek összegét'''
        kezdeti_szam = szám
        szamjegyek_osszege = 0
        while szám >= 1:
            maradek = szám % 10
            szám = szám/10 - (maradek/10)
            szám = int(szám)
            szamjegyek_osszege += maradek
        szamjegyek_osszege = int(szamjegyek_osszege)
        print(f"a {kezdeti_szam} számjegyeinek összege: {szamjegyek_osszege}")
        return szamjegyek_osszege
    
    def kivonás(szám):
        '''Ez a függvény kivonja a számból, a számjegyeinek összegét'''
        szám -= számjegyek_összege(szám) 
        print(f"Ha ezeket kivonom egymásból, akkor {szám}-ot kapom új számként", end="\n\n")
        return szám
    
    print(f"A megadott számod: {szám}")
    
    ismetlesek_szama = 0
    
    while szám > 0:
        szám = kivonás(szám)
        ismetlesek_szama += 1
    print("Az ismétlések száma: ", ismetlesek_szama)
    return ismetlesek_szama


szám = számbekérés()
művelet(szám)
 """
""" #vagy másképp megoldva: 
def repeat_times(szám):
    s = 0
    n_str = str(szám)
    while (szám > 0):
        szám -= sum([int(i) for i in list(n_str)])
        n_str = list(str(szám))
        s += 1
    return s

print(repeat_times(számbekérés()))
 """
 
 
#14. Írjon egy Python programot, hogy megtalálja az adott egész szám osztóinak számát.
""" 
def osztók_száma(szám):
    osztok_szama = 0
    osztók = []
    i=1
    while i < szám:
        if szám % i == 0:
            osztok_szama += 1
            osztók.append(i)
        i += 1
    print(osztók)
    return osztok_szama

print(f"Összesen {osztók_száma(számbekérés())} osztója van")
 """
 
#15. Írjon egy Python programot, hogy megtalálja azokat a számjegyeket, amelyek hiányoznak az adott mobil számból.
mobilszám=False
while mobilszám == False:
    try:
        mobilszám = int(input("Add meg a mobilszámodat, majd nyomj Enter-t: "))
    except:
        print("Csak számokat írj be!")
print("\n","Vizsgálom a ",mobilszám,"telefonszámot:", end="\n\n")
str_mobilszám = str(mobilszám)
szamlista = ["1","2","3","4","5","6","7","8","9","0"]
közös = set()
for z in szamlista:
    for i in str_mobilszám:
        if z == i:
            közös.add(z)

szamlista = set(szamlista)


hiányzók = szamlista - közös

hiányzók = list(hiányzók)


# Hiányzók sorbarendezése sort() függvénnyel:

hiányzók.sort()
print(f"A megadott mobilszámban az alábbi számjegyek nem szerepelnek: \n{hiányzók}")
    
    
    

