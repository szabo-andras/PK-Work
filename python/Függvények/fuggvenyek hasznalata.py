# 5
# 5+4+3+2+1


""" def elso_n_szam_osszege(x):
    while x>0:
        x=x+(x-1) """

def elso_n_szam_osszege (x):
    """Ez a függvény összeadja az első 'x' számot"""
    z=0
    for i in range(0,x+1):
        z=z+i
    return z    

a=elso_n_szam_osszege(int(input("Adj meg egy számot: ")))
print(a)




