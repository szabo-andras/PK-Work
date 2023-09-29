A=0
while(1>A or A>3):
    try:
        A=int(input('"A"-játékos: Írd be a tipped sorszámát!: 1. Kő, 2. Papír, 3. Olló '))
    except:
        print("Az alábbi számok közül válassz: 1,2 vagy 3")
    print("Az alábbi számok közül válassz: 1,2 vagy 3")
        
B=0
while(1>B or B>3):
    try:
        B=int(input('"B"-játékos: Írd be a tipped sorszámát!: 1. Kő, 2. Papír, 3. Olló '))
    except:
        print("Az alábbi számok közül válassz: 1,2 vagy 3")
    print("Az alábbi számok közül válassz: 1,2 vagy 3")


if (A==1):
    A="kő"
elif(A==2):
    A="papír"
else:
    A="olló"

if (B==1):
    B="kő"
elif(B==2):
    B="papír"
else:
    B="olló"

if (A==B):
    nyertes="Döntetlen"
elif (A==1 and B==2):
    nyertes="B-játékos"
elif (A==2 and B==3):
    nyertes="B-játékos"
elif (A==3 and B==1):
    nyertes="B-játékos"
else:
    nyertes="A-játékos"


print('"A"-játékos tippje:',A)
print('"B"-játékos tippje:',B)
print("A nyertes:",nyertes)

