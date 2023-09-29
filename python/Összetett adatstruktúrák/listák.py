""" LISTÁK KEZELÉSE """
# A lista elemeit [ ] zárójelbe tesszük

marvel = ["Spiderman", "Iron Man", "Captain America", "Black Widow", "Thor"]
print(marvel)

#LISTAELEM HOZZÁADÁS: "append()" fügvénnyeL, ami a lista végére teszi az új elemet:
marvel.append("Loki")
print(marvel)

#LISTAELEM TÖRLÉS: az elem pontos megadásával, "remove()" függvénnyel:
marvel.remove("Spiderman")
print(marvel)

# LISTAELEM BESZÚRÁS: "insert(hányadik indexre, "mit")" függvénnyel:
marvel.insert(0,"Spiderman")
marvel.insert(3,"Hulk")
print(marvel)

#LISTAELEM TÖRLÉS: az elem indexének megadásával "pop(index sorszáma)" függvénynel:
marvel.append("Superman") #Hozzá adjuk Superman-t, hogy utána eltávolíthassuk
marvel.pop(7) # Itt eltávolítjuk Superman-t
print(marvel)

#LISTA KIÜRÍTÉSE: "clear()" függvénnyel:
marvel.clear()
print(marvel)