""" 8. Jelszó generátor! """

import random

# Megadok egy listát, aminek elemeiből lehet generálni a jelszót
karakterek_listaja=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0","§","+","!","%","/","="]
jelszo=[] #üres lista, amibe bekerülnek majd a karakterek

#bekérem, hogy hány karakterá legyen a jelszó

try:
    karakterszam=int(input("Hány karakterű jelszót szeretnél?"))
except:
    print("Számot adj meg!")
    
print("",end="\n\n")

#random kiválasztom a listából a karaktereket

while karakterszam>0:
    jelszoelem=karakterek_listaja[random.randint(1,len(karakterek_listaja))]
    jelszo.append(jelszoelem)
    karakterszam -=1

separator=""
kiirt_jelszo=separator.join(jelszo)
print("Az általam létrehozott jelszó: ",kiirt_jelszo)