print("",end="\n\n")
print("KŐ, PAPÍR, OLLÓ")
print("",end="\n\n")
A_nyertes=0
B_nyertes=0
global jatekok_szama
jatekok_szama=0
tovabbi_jatek="i"

def jatekszamolas ():
    global jatekok_szama
    jatekok_szama +=1
    return jatekok_szama

def vegeredmenyvizsgalat(A_nyertes,B_nyertes):
    # A végeredmény: A_nyertes és B_nyertes változók összehasonlításából ered 
    if A_nyertes<B_nyertes:
        print("Összesítésben 'B' játékos nyert")
    elif A_nyertes>B_nyertes:
        print("Összesítésben 'A' játékos nyert")
    else:
        print("Szerintem ez döntetlen",A_nyertes,":",B_nyertes)

while tovabbi_jatek=="i":
    
    while tovabbi_jatek=="i":
        lista={1:"kő", 2:"papír", 3:"olló"}

        A=False
        B=False
        

        while A==False:
            try:
                A=int(input("'A' játékos tipje: (1=Kő, 2=Papír, 3=Olló)"))
            except:
                print("számot adj meg!")
            if 0<A<4:
                pass
            else:
                print("Válassz a 3 lehetőség közül!")
                A=False
        while B==False:
            try:
                B=int(input("'B' játékos tipje: (1=Kő, 2=Papír, 3=Olló)"))
                
            except:
                print("számot adj meg!")
            if 0<B<4:
                pass
            else:
                print("Válassz a 3 lehetőség közül!")
                B=False

        def vizsgalat(A,B):
            #Ezzel a függvénnyel megvizsgáljuk, hogy melyik játékos nyer eredmeny==True, vagy False, amit később 'A' nyert, vagy 'B' nyert-re fogunk változtatni
            eredmeny="meg nincs eredmeny"
            if A==B:
                
                return 0
            elif (A==1 and B==3) or (A==2 and B==1) or (A==3 and B==2):
                return 1
            else:
                return 2    
            
            
           
        print("'A' játékos tippje:", lista[A])
        print("'B' játékos tippje:", lista[B]) 
        
        if vizsgalat(A,B)==0:
            print("Döntetlen")
        elif vizsgalat(A,B)==1:
            A_nyertes = A_nyertes+1
            print("A nyert")
        else:
            B_nyertes=B_nyertes+1
            print("B nyert")
        
        print("A nyertes játszmái:",A_nyertes,":",B_nyertes,":B nyertes játszmái")
        tovabbi_jatek="kerdes"
        
        while tovabbi_jatek !="i":
            tovabbi_jatek=input("Akartok tovább játszani? i=igen, n=nem: ")
            if tovabbi_jatek=="i":
                jatekszamolas()
            elif tovabbi_jatek=="n":
                print("Vége a játéknak")
                print("A játék végeredménye:", A_nyertes,":",B_nyertes)
                break
            else:
                print("'i', vagy 'n' közül válassz")
print("",end="\n\n")
print("lejátszott körök száma: ", jatekszamolas())

print("",end="\n\n")
vegeredmenyvizsgalat(A_nyertes,B_nyertes)