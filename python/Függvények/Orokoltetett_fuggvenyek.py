"""  2023.07.30 / 10:00 / Python OOP / 2023MAY / Rob
https://programozas-karrier.teachable.com/courses/1421971/lectures/47853117
"""

class Ember:
    def __init__(self, kn, vn, kor, nem):
        self.keresztnev = kn
        self.vezeteknev = vn
        self.kor = kor
        self.nem = nem
knev = input("Keresztnév:")
vnev = input("Vezetéknév:")
nem = input("Nem:")
veg = int(input("végzés éve:"))
szuletesi_ev = int(input("Születési év:"))
kor = 2023-szuletesi_ev

class Tanulo(Ember):
    def __init__(self,kn, vn, kor, nem, veg):
        super().__init__(kn, vn, kor, nem)
        self.vegzes = veg
    def tanulo_kiiratas(self):
        return f"{self.keresztnev} {self.vezeteknev} {self.kor} {self.nem} {self.vegzes}"

Tanuló = Tanulo(knev,vnev,kor,"Férfi",veg)

print(Tanuló.tanulo_kiiratas())