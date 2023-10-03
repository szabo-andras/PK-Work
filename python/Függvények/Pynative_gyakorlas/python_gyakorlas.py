""" 1. gyakorlat: Számítsa ki két szám szorzását és összegét! 
Adott két egész szám, csak akkor küldje vissza az szorzatukat, 
ha a szorzat egyenlő vagy kisebb, mint 1000. 
Ellenkező esetben adja vissza az összegüket. """
""" 
try:
    a=int(input("Add meg az első számot!"))
except:
    print("Számot kérek!")
try:
    b=int(input("Add meg a második számot!"))
except:
    print("Számot kérek!")
    
if a*b<=1000:
    print("'a' és 'b' szorzata:",a*b)
else:
    print("'a' és 'b' összege:", a+b)
     """
""" 2. gyakorlat: Nyomtassa ki az aktuális és az előző szám összegét
Írjon programot az első 10 szám iterálására, 
és minden iterációban írja ki az aktuális és az előző szám összegét. """
""" szam=0
for i in range (1,11):
    print(i,i+szam)
    szam=i """
    
""" 3. gyakorlat: Nyomtasson ki olyan karaktereket egy karakterláncból, 
amelyek páros indexszámmal vannak jelen
Írjon programot, amely elfogad egy karakterláncot a felhasználótól, 
és megjeleníti azokat a karaktereket, amelyek páros indexszámmal vannak jelen.

Például str = "pynative"meg kell jelenítenie a „p”, „n”, „t”, „v” betűket. """
karakterlanc=str(input("Írj ide egy karakterláncot: "))
for i in range(1,len(karakterlanc)+1):
    if i%2==0:
        print(karakterlanc[i-1])