# tuples

a = 12
b = 34
c = a, b
print(c)

# hagyományos csere módszer
print(f"A={a}, B={b}")
temp = a
a = b
b = temp
print(f"A={a}, B={b}")

# python módszer
a, b = b, a
print(f"A={a}, B={b}")

def két_változót_adok_vissza():
    return (123, "szöveg")

x, y = két_változót_adok_vissza()
print(f"X={x}, Y={y}")

# egy soros if (vagy egyéb struktúra)
if True: print("Igaz!")

# lista értelmezés
lista_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lista_2 = [i for i in lista_1 if i % 2 == 0]
print(lista_2)

# változó számú paraméter átadás függvényeknek
def hatványösszeg(hatváy, *elemek):
    összeg = 0
    for i in elemek:
        összeg += pow(i, hatváy)
    return összeg

print(hatványösszeg(2, 2))
print(hatványösszeg(2, 2, 34, 22, 3))
print(hatványösszeg(2, 2, 34, 21, 2, 4, 5, 6, 33))
# a kulcsszavas paraméterekről később