""" Torpedó """

#A játéktér elkészítése:
#Készítek egy x*y méretű "táblázatot"

tablazat=[]
oszlop=[]
sor=[]

sorokSzama=False
oszlopokSzama=False

elem=1


while sorokSzama==False:
    try:
        sorokSzama=int(input("Hány sort szeretnél? "))
    except:
        print("Számot adj meg!")
while oszlopokSzama==False:
    try:
        oszlopokSzama=int(input("Hány oszlopot szeretnél? "))
    except:
        print("Pozitív számot adj meg")



for sorelem in range(1,sorokSzama*oszlopokSzama):
    while sorokSzama!=0:
        oszlopokSzamaValtozas=oszlopokSzama
        for o in range(0,oszlopokSzama):
            sor.append(elem)
            elem+=1
            oszlopokSzamaValtozas-=1
        tablazat.append(sor)
        sor=[]
        sorokSzama-=1

print(tablazat)   
