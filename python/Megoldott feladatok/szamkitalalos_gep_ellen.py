import random
print()
print("SZÁM KITALÁLÓS JÁTÉK")
print()
print("Gondoltam egy számot 1 és 100 között. Kitalálod?")
SZAM = random.randint(1,100)

tipp_jatekos=0
jatekos_seged1=1
jatekos_seged2=100
f=0
while SZAM!=tipp_jatekos:
    
    try:
        tipp_jatekos = int(input("Add meg a tipped:"))
    except:
        print("Számot adj meg")
    if tipp_jatekos > SZAM:
        print ("A szám kisebb, mint", tipp_jatekos, "de nagyobb,mint", jatekos_seged1)
        jatekos_seged2=tipp_jatekos
 
    elif tipp_jatekos < SZAM:
        print("A szám nagyobb, mint", tipp_jatekos, "de kisebb, mint" ,jatekos_seged2)
        jatekos_seged1=tipp_jatekos
      
    f+=1
print("BRAVÓ!!!",f,"Lépésből kitaláltad", SZAM,"=",tipp_jatekos)


print()
print("MOST ÉN JÖVÖK:")
print()
seged1=1
seged2=100
tipp_gep = random.randint(seged1,seged2)
i = 0
while SZAM != tipp_gep:
    
    if tipp_gep > SZAM:
        print ("A szám kisebb, mint", tipp_gep)
        seged2=tipp_gep-1
        tipp_gep=random.randint(seged1,seged2)
       
    elif tipp_gep < SZAM:
        print("A szám nagyobb, mint", tipp_gep)
        seged1=tipp_gep+1
        tipp_gep=random.randint(seged1,seged2)
        
    i += 1
print("Én",i,"lépésből találtam ki",tipp_gep,"=",SZAM)

print()
if i>f:
    print("Gratulálok! Te nyertél")
elif i<f:
    print("Most vesztettél")
else:
    print("Döntetlen")