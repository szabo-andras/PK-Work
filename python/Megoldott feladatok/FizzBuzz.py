"""PY05: Oldd meg a FizzBuzz feladatot: Írd ki az összes pozitív egész számot 1-től 100-ig. Egészítsd ki a programot úgy, hogy minden 3-mal osztható szám helyett a Fizz szöveget írja ki a program. Egészítsd ki a programot úgy, hogy minden 5-tel osztható szám helyett a Buzz szöveget írja ki a program. Egészítsd ki a programot úgy, hogy minden 3-mal és 5-tel is osztható szám helyett a FizzBuzz szöveget írja ki a program. Munkád eredményét https://replit.com/ link segítségével posztold a homework csatornán."""

szamokListaja = []
for i in range(1, 100 + 1):
  if i % 3 == 0 and i % 5 == 0:
    szamokListaja.append("FizzBuzz")
  elif i % 3 == 0 and i % 5 != 0:
    szamokListaja.append("Fizz")
  elif i % 5 == 0 and i % 3 != 0:
    szamokListaja.append("Buzz")
  else:
    szamokListaja.append(i)

for i in szamokListaja:
  print (i)
