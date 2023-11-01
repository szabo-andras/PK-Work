# kivételkezelés

# with

with open("fajlnev.txt", "r") as fájl:
    for sor in fájl:
        print(sor, end="")

# nem szükséges a fájl lezárása



class Túl_kis_szám_kivétel(Exception):
    '''"Akkor szól, ha túl kicsi a bevitt szám."'''
    def __init__(self, bevitt_szám, minimális_érték):
        Exception.__init__(self)
        self.bevitt_szám = bevitt_szám
        self.minimális_érték = minimális_érték

try:
    szám = int(input("Írjon be egy számot! "))  # beolvassuk én konvertáljuk egész típussá
    if szám < 100:
        raise Túl_kis_szám_kivétel(szám, 100)  # itt egy kivétel keletkezik
except Túl_kis_szám_kivétel as TKSZK:
    print(f"A beírt szám: {TKSZK.bevitt_szám},"
        f" A minimális érték: {TKSZK.minimális_érték}")
except ValueError:
    print("Sajnos nem számot írt be!")
except:
    print("VALAMILYEN hiba lépett fel!")  # bármilyen hiba esetén fut le
else:
    print(f"A következő számot írta be: {szám}")
finally: #ennek a kivételkezelésnek MUSZÁJ az utolsónak lennie
    print("Viszont látásra!")  # ezt mindenképpen le fogja futtatni
    #Ebben a kivételkezelésben, ha nyitva van egy fájl, akkor azt be KELL zárni (fájl.close())
    