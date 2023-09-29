''' Függvény létrehozása a "def"-fel kezdődik, majd megadunk egy nevet a függvénynek, mjad a zárújelek közés be tudjuk adni az elemeket'''

def fuggveny ():
    print("Hello")

fuggveny()


# 5
# 5 + 4 + 3 + 2 + 1

""" def elso_n_szam_osszege(x):
    eredmeny = 0
    while x != 1:
        eredmeny = eredmeny + x
        x=x-1

elso_n_szam_osszege(5)
print(eredmeny) """

def elso_n_szam_osszege(x):
    osszeg = 0
    for i in range(1, x+1):
        osszeg += i
    print("az első", x, "szám összege: ", osszeg)

elso_n_szam_osszege(int(input( "írj be egy számot: ")))


""" Első n darab szám összege rekurzióval
A rekurzív függvény arról híres, hogy önmagát hívja meg  """
def elso_n_szam_osszege_r(x):
    pass

elso_n_szam_osszege_r(int(input( "írj be egy számot: ")))