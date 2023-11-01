'''Osztályok az "Öntőformák" '''

#Létrehozzuk az "Ember" osztályt:
class Ember:
    def __init__(self,ember_név) -> None:
        self.név = ember_név
    
    def köszönés(self):
        print(f"Helló, én {self.név} vagyok!, a Főnök")
    
    

#Az Ember osztállyal létrehozunk egy példányt:

egy_ember = Ember("Géza")

print(egy_ember.név)
egy_ember.köszönés()


#Létrehozom a Munkatárs osztályt:
class Munkatárs:
    munkatársak_összlétszáma = 0

    def __init__(self, név, életkor):
        self.név = név
        self.életkor = életkor
        Munkatárs.munkatársak_összlétszáma += 1

    def köszönés(self):
        print(f"Szervusz! Az én nevem: {self.név} és {self.életkor} éves vagyok")

    def vége_a_műszaknak(cls):
        Munkatárs.munkatársak_összlétszáma -= 1

    @classmethod
    def hányan_dolgoznak_még(cls):
        print(cls.munkatársak_összlétszáma, "ember dolgozik még")

első_munkatárs = Munkatárs("Géza", 22)
második_munkatárs = Munkatárs("József", 20)

első_munkatárs.köszönés()
második_munkatárs.köszönés()

Munkatárs.hányan_dolgoznak_még()
első_munkatárs.vége_a_műszaknak()
Munkatárs.hányan_dolgoznak_még()

