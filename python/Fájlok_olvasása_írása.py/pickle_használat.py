import pickle

#létrehozunk egy akármilyen változót, jelen esetben egy listát

ez_egy_lista = ["búbosvöcsök", 999, False]

fájl = open("tároló.dat", "wb") #Eddig ugyanaz

pickle.dump(ez_egy_lista, fájl) #elraktuk

fájl.close

del ez_egy_lista #töröltük az eredeti listát

fájl = open("tároló.dat","rb")
ez_egy_másik_lista = pickle.load(fájl)
fájl.close()

print("2:",ez_egy_másik_lista)