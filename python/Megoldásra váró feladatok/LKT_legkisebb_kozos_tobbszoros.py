#8 Írjon Python programot két pozitív egész szám legkisebb közös többszörösének kiszámításához.
szam1 = False
szam2 = False

print(
    "\n\nKét egész szám legnagyobb közös osztójának (LKO) megtalálása Euklideszi algoritmussal:",
    end="\n\n")

#Adatbekérés kivételkezeléssel
while szam1 == False:
  try:
    szam1 = int(input("Adj meg egy egész számot (x): "))
  except:
    print(
        "\nHIBA HIBA HIBA\n Szerintem ez nem  egész szám. Próbáld meg még egyszer!",
        end="\n\n")
while szam2 == False:
  try:
    szam2 = int(input("Adj meg egy másik egész számot (y): "))
  except:
    print(
        "\nHIBA HIBA HIBA\n Szerintem ez nem  egész szám. Próbáld meg még egyszer!",
        end="\n\n")


#Függvény:

def LKT (szam1, szam2):
    '''Addig kell növelni a nagyobb számot 1-el, ameddig osztható nem lesz a kisebb számmal'''

