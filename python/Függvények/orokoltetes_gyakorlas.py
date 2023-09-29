"""Ebben a kódban azt gyakoroltam, hogy a Focicsapatok adatait felhasználva 
megjelenítünk egy játékost, aki épp benne játszik"""

class Focicsapat:
    def __init__(self,csnev,orszag,alapitas):
        self.csapatnev = csnev
        self.csapatorszag = orszag
        self.csapat_alapitas = alapitas

class Jatekos(Focicsapat):
    def __init__(self, csnev, orszag, alapitas,jknev,jvnev):
        super().__init__(csnev, orszag, alapitas)
        self.jatekos_keresztnev = jknev
        self.jatekos_vezeteknev = jvnev
        
    def jatekosadatok(self):
        print(self.jatekos_vezeteknev, self.jatekos_keresztnev, "jelenlegi csapata:", self.csapatnev)
    
futballista1 = Jatekos("Liverpool","Anglia", 1893,"Dominik","Szoboszlai")

futballista1.jatekosadatok()
