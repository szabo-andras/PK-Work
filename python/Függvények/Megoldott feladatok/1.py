class Ember:
    def __init__(self, kn, vn):
        self.knev = kn
        self.vnev = vn
        

    def kiir(self):
        print(self.vnev,self.knev)

felhasználó1 = Ember("András", "Szabó")
felhasználó1.kiir()

# Örököltetéssel létrehozunk egy tanulót:

class Tanulo(Ember):
    def __init__(self, kn, vn, veg):
        super().__init__(kn,vn)
        self.vegzes=veg

    def koszones(self):
        print("Hello",self.vnev, self.knev, "! Te",self.vegzes,"évben végeztél")

tanuló = Tanulo("Tamás","Szabó", 2006)
tanuló.koszones()
