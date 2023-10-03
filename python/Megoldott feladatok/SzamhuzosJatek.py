""" Feladat: 18 tételből 1,2, vagy 3 húzás felváltva. Hogyan kerüljük el az utolsó tételt?"""

try:
    mennyiseg=int(input("Hány elemű a halmaz, amiből húzunk? "))
except:
    print("Számot írj be! ")
def aHuz():
    aHuzas=0
    
    while 1> aHuzas or aHuzas >3:
        try:
            aHuzas=int(input("'A' Játékos: Hányat húzol? (1,2, vagy 3) "))
        except:
            print("1, 2, vagy 3-at választhatsz")
    
    return aHuzas

def bHuz():
    
    bHuzas=0
    
    while 1> bHuzas or bHuzas >3:
        try:
            bHuzas=int(input("'B' Játékos: Hányat húzol? (1,2, vagy 3) "))
        except:
            print("1, 2, vagy 3-at választhatsz")
    return bHuzas
    

maradekMennyiseg=mennyiseg

while maradekMennyiseg>1:
    
    aHuzasszam=0
    bHuzasszam=0

    maradekMennyiseg = maradekMennyiseg - aHuz()
    aHuzasszam+=1
    print("Maradék mennyiség:",maradekMennyiseg)
    
    maradekMennyiseg = maradekMennyiseg-bHuz()
    bHuzasszam+=1
    print("Maradék mennyiség:",maradekMennyiseg)

#Ez itt például egy szelekció:
    
if aHuzasszam>bHuzasszam:
    print("A nyert")    
else:
    print("b-nyert")

