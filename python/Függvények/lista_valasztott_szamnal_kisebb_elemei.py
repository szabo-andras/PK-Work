import random
""" Létrehozunk egy olyan 100 elemű listát, aminek egy általunk megadott intervallumból vett random elemei vannak """
lista=[]
try:
    intervallum_alja=int(input("Add meg az intervallum legkisebb elemét!"))
except:
    print("Számot adj meg!")

try:
    intervallum_teteje=int(input("Add meg az intervallum legnagyobb elemét!"))
except:
    print("Számot adj meg!")

for i in range(0,99):
    elem=random.randint(intervallum_alja,intervallum_teteje)
    lista.append(elem)

print(lista)

print("",end = "\n\n")   

try:
    valasztott_szam=int(input("Hánynál kisebb számokat szeretnéd kinyerni?"))
except:
    print("Számot adj meg!")

def valasztott_szamnal_kisebb_elemek(lista):
    """ Ez a függvény kiírja egy lista -nél kisebb elemeit, új sorokba, és egy új listát is készít belőle otnel_kisebbek_listaja néven"""
    valasztott_szamnal_kisebbek_listaja=[]
    print()
    for i in lista:
        if i<valasztott_szam:
            print(i)
            valasztott_szamnal_kisebbek_listaja.append(i)
    print(f"Választott szám = {valasztott_szam} kisebbek listája: ",valasztott_szamnal_kisebbek_listaja)
    
print("",end = "\n\n")         

valasztott_szamnal_kisebb_elemek(lista)