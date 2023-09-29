print("Készíts egy olyan algoritmust, amely képes értéket adni egy 3 x 3 -as táblázat minden egyes cellájának. (Ehhez két ciklusra lesz szükséges, amelyek egymásba vannak ágyazva. Az egyik lépkedjen végig a táblázat sorain, a másik pedig az oszlopain.)")

table=[["a","b","c"],["d","e","f"],["g","h","i"]]
print(table)

col=0
row=0
print()
print("Most átírjuk a táblázat elemeit lépésenként:")
print()
while row<len(table):
    while col<len(table):
        table[row][col]=col+1   
        col+=1
    row+=1
    col=0
print()
print(table)

print("vége")