
eredmeny="abbaaabaaabbabababbbaabbababb"

# megszámolom, hány db "a" van a string-ben
a=0
b=0
# megszámolom, hány db "a" van a string-ben
# megszámolom, hány db "b" van a string-ben
for i in eredmeny:
    if i=="a":
        a=a+1
    elif i=="b":
        b=b+1
print("a=",a,"b=",b)

# Összehasonlítom a-t b-vel
def vegeredmeny(a,b):
    if a>b:
        return f"'a' játékos nyert {a} : {b} arányban"
    elif b>a:
        return f"'b' játékos nyert {b} : {a} arányban"
    else:
        return f"Döntetlen {a} : {b}"
    
print(vegeredmeny(a,b))