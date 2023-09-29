""" Ez a fájl a https://programozas-karrier.teachable.com/courses/1421971/lectures/47853117
honlapon található   2023.07.30 / 10:00 / Python OOP / 2023MAY / Rob
videó alapján készült """

# Létrehozzuk az EMBER osztályt:

class Ember:
    x = 5 #Ez egy osztály változó

# Létrehozzuk a létrehozó függvényt a magic __init__() függvénynel

    def __init__(self,nev,kor,lakohely): #itt a self, az a függvény saját osztályának minden változója/objektuma
        """Ezt a függvényt használva megadhatjuk a függvény által létrehozott objektum változóinak értékét
        Pl. ha létrehozzuk a felhasználó1-et és ésrtékeként meghívjuk az Ember(Béla) függvényt, akkor 
        a felhasználó1.nev változó értéke Béla lesz"""
        self.nev = nev
        self.kor = kor
        self.lakohely = lakohely

# Meghatározzuk, hogy mit írjon ki, ha olyan objektumra mutatunk, ami a jelen Class fuggvényével lett létrehozva
    def __str__(self): # Mivel benne van a paraméterek között a self, így a saját osztályának (függvényen kívüli) változóit is használhatjuk
        return f"{self.nev}({self.kor})" # az f-betű a formázott szöveget jelzi

# Írunk egy olyan függvényt, ami kiírja a nev objektum tartalmát:
    def kiir(self):
        print(self.nev)


# Az Ember objektumban található függvényekkel végzett feladatok:

felhasználó1 = Ember("Béla",25,"Győr") # A "felhasználó1" objektum nev változójának Béla értéket adunk, mert a függvény első paramétere a self után a "nev" paraméter
felhasználó2 = Ember("Géza",19,"Budapest")

print(felhasználó1.nev,felhasználó1.kor,felhasználó1.lakohely)
print(felhasználó1) # itt egy olyan objektumra hivatkozunk, amiben meg van adva, hogy hogyan jelenítse meg saját magát (def __str__(self):)
felhasználó1.kiir()

felhasználó2.kiir()

