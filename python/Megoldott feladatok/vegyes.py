""" Változók hatóköre """
a = 12 # Ez egy globális változó

def f():
    
    a = 55 # Ez egy belső változó, tehát a globális (a függvényen kívüli) változó értékét nem változtatja meg
    print("A függvényben szereplő a valtozó értéke: ", a)
 
f()
print('A függvényen kívüli "a" értéke: ', a) #ez a globális változó nem változott meg, annak ellenére sem, hogy a függvényben használtam egy ugyanilyan "a" nevű változót
# de ze a belső (függványen belüli) "a" változó nem volt egyenlő a globális "a" változóval

'''Amennyiben szeretnénk a függvényen belül megváltoztatni a globális változó értékét, úgy
a függvényen belül meg kell hívnunk először a globális változót, majd utána módosythatjuk.
Így már a függvényen kívüli változó értéke is változni fog:'''

a = 12

def fuggveny():
    global a #itt hívjuk meg a globális "a" változót
    a = 55
    print("A függvényben szereplő a valtozó értéke: ", a)

fuggveny()
print('A függvényen kívüli "a" értéke: ', a)

print("\n")
''' A beépített, és az importált matematikai függvények használata:'''

a = -12 
b = 24
c = max(a, b)
print("a megadott változók: a:", a, "és b:", b)
print('az "a" és "b" változók közül a legnagyobb a: ',c)

print ("\n")
       

c = min(a, b)
print('az "a" és "b" változók közül a legkisebb a: ',c)

print ("\n")



c = abs(a)
print('az "a" változó abszolút értéke (nullától való távolsága): ',c)

print ("\n")

'''Hatványozás a "pow" függvénnyel:'''

a = -4 
b = 2
print("a megadott változók: a:", a, "és b:", b)

c = pow(a,b) #"a" változó a "b"-edik hatványon
print('az "a" változó a "b"-edik hatványon: ',c)

print ("\n")

'''Gyökvonás szintén a "pow" függvénnyel, de a tört hatványra kell emelni (pl 1/2-ik hatvány = 0.5 hatvány = négyzetgyök):'''

c = pow(a,0.5) #"a" változó a "b"-edik hatványon
print('az "a" változó a négyzetgyöke: ',c)



''' Importált "math" Python MODUL'''
import math

'''ebben az esetben egy szám négyzetgyökét az "math.sqrt" függvénnyel kaphatunk meg:  '''

