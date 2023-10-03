""" Feladat: 18 tételből 1,2, vagy 3 húzás felváltva. Hogyan kerüljük el az utolsó tételt?"""
# Úgy lehet elkerülni, hogy A mindig (4-bHuzas) húzásmennyiséget húz


maradekMennyiseg=18
print("Kezdeti mennyiség:",maradekMennyiseg)
aHuzas=1
maradekMennyiseg=maradekMennyiseg-aHuzas

while maradekMennyiseg>1:
    bHuzas=0
    while 1>bHuzas or bHuzas>3:
        bHuzas=int(input("Hányat húzol B-játékos? (1,2,3)"))
    maradekMennyiseg -=bHuzas
    print("Maradék",maradekMennyiseg)
    if maradekMennyiseg>1:
        aHuzas=4-bHuzas
        print("A húzott:", aHuzas)
        maradekMennyiseg-=aHuzas
        print("Maradék",maradekMennyiseg)

    
