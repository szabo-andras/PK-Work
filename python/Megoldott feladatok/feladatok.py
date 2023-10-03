#Kérd be a felhasználó nevét. Köszöntsd a felhasználót a saját nevén.
felhasznalonev = input("Hogy hívnak? ")
print(f"Szia {felhasznalonev}!")

#Kérd be a felhasználó magasságát, és írd ki, hogy mennyivel magasabb, mint 100cm
felhasznalo_magassaga = -1
while 0>felhasznalo_magassaga:
    
    try:
        felhasznalo_magassaga = int(input("Hány cm magas vagy?"))
    except:
        print("Nem értettem pontosan.Adj meg egy pozitív egész számot!")
if felhasznalo_magassaga > 100:
    print(f"Te {felhasznalo_magassaga-100} cm-rel vagy magasabb 100cm-nél")        
elif felhasznalo_magassaga <100:
    print(f"Te {100-felhasznalo_magassaga} cm-rel vagy alacsonyabb 100cm-nél")
else:
    print(f"Te pont {felhasznalo_magassaga} cm magas vagy.")

#Kérj be a felhasználótól egy szöveges értéket egy változóba.
szoveg = str(input("Írj be ide bármit:"))
print(f"Az előbb beírt szöveg az alábbi: {szoveg}")
for szoveg in 2:
print(szoveg)

