"""20. Kérj be egy egész számot a felhasználótól és döntsd el, hogy 
pozitív vagy negatív vagy nulla. 
Először folyamatábrát rajzolj, utána írd meg a programot.
"""
szam="False"

while szam=="False":
    try:
        szam=int(input("Adj meg egy számot"))
    except:
        print("Számot adj meg!!!")
    
if szam<0:
    print("A szám negatív")
elif szam>0:
    print("A szám pozitív")
else:
    print("A szám 0")