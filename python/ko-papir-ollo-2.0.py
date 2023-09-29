print("Kő, Papír, Olló")

uj_jatek="i"
while uj_jatek=="i":
    A=0
    B=0
    while (1>A or A>3):
        print("A-játékos")
        try:
            A=int(input("Add meg a választásod sorszámát! (1:Kő, 2:Papír, 3:Olló)"))
        except:
            print("Nem számot adtál meg. Próbáld meg újra!")
        if 1>A or A>3:
            print("Nem jó számot adtál meg! Próbáld meg újra!")

    while (1>B or B>3):
        print("B-játékos")
        try:
            B=int(input("Add meg a választásod sorszámát! (1:Kő, 2:Papír, 3:Olló)"))
        except:
            print("Nem számot adtál meg. Próbáld meg újra!")
        if 1>B or B>3:
            print("Nem jó számot adtál meg! Próbáld meg újra!")
    
    print("A-játékos tippje:", A,"B-játékos tippje:", B)
    uj_jatek="x"
    while uj_jatek!="i" and uj_jatek!="n":
        uj_jatek=input("Szeretnél új játékot? ")
    
        
print("Vége")
    
    