"""EZT A FELADATOT MÉG NEM FEJEZTEM BE"""

# Mennyi a kancsók űrtartalma, vagyis maximum mennyi víz fér beléjük?
aKancsoMax=8
bKancsoMax=5
cKancsoMax=3

# A Kancsók aktuális tartalmának változói:
aKancso=8
bKancso=0
cKancso=0

# Adott pillanatban mennyivel csökken, vagy nő a kancsó tartalma?
aKancsoValtozas=0
bKancsoValtozas=0
cKancsoValtozas=0

#Függvények amika változásokat eredményezik:
def AbolBbe(aKancso,bKancso,cKancso,aKancsoMax,bKancsoMax,cKancsoMax,aKancsoValtozas,bKancsoValtozas,cKancsoValtozas):
    if aKancso>bKancsoMax-bKancso:
        aKancsoValtozas=bKancsoMax-bKancso
    else:
        aKancsoValtozas=aKancso
    return aKancsoValtozas
    
    
    
print (aKancso,bKancso)
AbolBbe(aKancso,bKancso,cKancso,aKancsoMax,bKancsoMax,cKancsoMax,aKancsoValtozas,bKancsoValtozas,cKancsoValtozas)
print (aKancso,bKancso,cKancso)