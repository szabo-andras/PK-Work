# Tuple:
# A tuple elemeit ( ) zárójelbe tesszük


"""A tuple egy olyan lista, amiben nem lehet az elemeken közvetlenül változtatni
Előtte listává kell alakítani, amjd a listát
visszaalakíthatjuk
tuple-lé"""

DC = ("Batman", "Superman", "Wonder Woman", "The Flash", "Green Lantern")

print(DC)
print(type(DC))


# A DC nevű tuple-t listává konvertálással beletesszük egy DC_lista változóba:
DC_lista=list(DC)
print(DC_lista)
print(type(DC_lista))

# A DC_lista változóban levő listához hozzáadjuk append() függvénnyel az "Aquaman" elemet:
DC_lista.append("Aquaman")
print(DC_lista)
print(type(DC_lista))

# A DC_lista változót tuple-lé konvertáljuk a DC változóba:
DC=tuple(DC_lista)
print(DC)
print(type(DC))

#Végeredmény: az eredeti DC tuple-t átírtuk a belőle alakított, majd kiegészített listával.
