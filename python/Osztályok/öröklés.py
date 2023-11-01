# Öröklés

#Létrehozunk egy egyetemi hallgató osztályt, majd 2 osztálypéldányt

class Egyetemi_hallgató:
    def __init__(self, név, kor):
        self.név = név
        self.kor = kor
        print(self.név," létrehozva.")
    
    def adatok_kiírása(self):
        print(f"Név: {self.név}, Kor: {self.kor}", )


# csináljunk több féle hallgatót, Pl. Bölcsész, és Mérnök szakos hallgatók

class Bölcsész(Egyetemi_hallgató):
    def __init__(self, név, kor, kedvenc_író):
        Egyetemi_hallgató.__init__(self, név, kor)
        self.kedvenc_író = kedvenc_író
        
    def adatok_kiírása(self):
        Egyetemi_hallgató.adatok_kiírása(self)
        print("Kedvenc írója:", self.kedvenc_író, end = "\n\n")
        
class Mérnök(Egyetemi_hallgató):
    def __init__(self, név, kor,kedvenc_fizikus):
        super().__init__(név, kor)
        self.kedvenc_fizikus = kedvenc_fizikus
    """ def __init__(self, név, kor, kedvenc_fizikus): 
        Egyetemi_hallgató.__init__(self, név, kor) """
        
    def adatok_kiírása(self):
        Egyetemi_hallgató.adatok_kiírása(self)
        print("Kedvenc fizikusa:", self.kedvenc_fizikus, end = "\n\n")

hallgató_1 = Bölcsész("Balázs",19,"Arany János")
hallgató_2 = Mérnök("Éva",19,"Teller Ede")

print() #Egy üres sor

hallgatók = [hallgató_1, hallgató_2]
for hallgató in hallgatók:
    hallgató.adatok_kiírása()