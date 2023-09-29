#SZÓTÁR (JavaScriptben a neve "Objektum"): kulcs:érték párok

marvel_weakPoint = {"Spider Man":"Pókérzék", "Iron Man":"Elektromágneses zavarok", "Captain America":"Szuper Szérum", "Black Widow":"A múltja", "Thor":"Mjölnir"}
print(marvel_weakPoint)
print(type(marvel_weakPoint))

# nyomtassuk ki a Fekete Özvegy gyenge pontját:
print("Feketeözvegy gyenge pontja:",marvel_weakPoint["Black Widow"])

for hero in marvel_weakPoint:
    print(hero,"gyenge pontja:",marvel_weakPoint[hero])

# Példa a szótár használatára: Egy felhasználó:

Tony_Stark={
    "realN":"Andthony Edward Stark",
    "birthplace":"Long Island",
    "wife":"Pepper Pots"
}

# A szótár egyik kulcsához tartozó adat kinyerése:
print(Tony_Stark)
x = Tony_Stark["wife"]
print(Tony_Stark["realN"],"felesége:",x)


# A szótár kulcsainak kinyerése:
z = Tony_Stark.keys()
print(z)

# új érték hozzáadása a szótárhoz: "hero":"Iron Man"

Tony_Stark["hero"] = "Iron Man"
print(Tony_Stark)