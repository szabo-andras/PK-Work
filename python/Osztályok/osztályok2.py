# osztályok és objektumok


class Munkatárs:
    '''Munkatársak regisztrálása'''

    ennyi_munkatárs_lett_létrehozva = 0  # osztályváltozó, ebből csak egy van

    def __init__(self, munkatárs_név):
        self.név = munkatárs_név
        Munkatárs.ennyi_munkatárs_lett_létrehozva += 1  # ha létrehozunk egyet

    def köszönés(self):
        print(f"Helló, én {self.név} vagyok! :)")

    def vége_a_műszaknak(self):
        Munkatárs.ennyi_munkatárs_lett_létrehozva -= 1  # hazament

    @classmethod
    def hányan_dolgoznak_még(cls):
        print(cls.ennyi_munkatárs_lett_létrehozva, " ember dolgozik még.")


egy_munkatárs = Munkatárs("Géza")
egy_munkatárs.köszönés()
másik_munkatárs = Munkatárs("Zoltán")
másik_munkatárs.köszönés()

Munkatárs.hányan_dolgoznak_még()
egy_munkatárs.vége_a_műszaknak()
Munkatárs.hányan_dolgoznak_még()
másik_munkatárs.vége_a_műszaknak()
Munkatárs.hányan_dolgoznak_még()