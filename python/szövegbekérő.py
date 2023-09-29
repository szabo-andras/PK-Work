
print("1. Kérj be egy szöveget a felhasználótól, majd írasd ki a szöveg karaktereit egymás alá. Készítsd el ezt az algoritmus a for és a while ciklus segítségével is.")

szoveg=input("Adj meg egy tetszőleges szöveget: ")

for betuk in szoveg:
    print(betuk)

i=0
while i<len(szoveg):
    print(szoveg[i])
    i+=1
