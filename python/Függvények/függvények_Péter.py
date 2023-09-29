"""Függvény létrehozása"""
# Létrehozzuk a függvényt, ami a és b változó értékeit adja össze és kiírja az eredményt:

a=3 # Ez a változó globális, vagyis bárhol használhatjuk a kódban, akár függvényen belül is
b=4 # Ez a változó globális, vagyis bárhol használhatjuk a kódban, akár függvényen belül is

def matematika():
    """Amit ide beírok, azt a VSkód később is kiírja a leírásban, amikor meghívom a függvényt"""
    c=2 #ez egy lokális változó, vagyis csak itt a függvényen belül létezik
    d=a+b+c
    print(d)


matematika()

# Hogyan hozunk létre LOKÁLIS változóból GLOBÁLIS változót:
"""Ahhoz, hogy a függvényen belüli 'c' változó GLOBÁLIS változó legyen, be kell 
írni a függvénybe, hogy : global c """

def matematika2():
    """Ez a függvény összeadja a, b és c változókat"""
    
    global c # Ezzel elérjük, hogy más függvényekben is használhassuk ezt a változót
    c = 2
    
    d = a + b + c
    print(d)

matematika2
