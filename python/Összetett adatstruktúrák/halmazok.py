# A halmazok elemeit { } zárójelbe tesszük:

"""!!!A halmazban egy elem, csakis kizárólag egyszer szerepelhet!!!
Ha kétszer írjuk be, akkor a másodikat figyelmen kívül hagyja"""

marvel2 = {"Spider Man", "Iron Man", "Captain America", "Captain America"}
print(marvel2)
print(len(marvel2))

# A halmaz elemei NEM indexeltek, vagyis nem tudjuk , hogy melyik a 2., 3. elem.

if "Iron Man" in marvel2:
    print("Vasember benne van a halmazban")
if "Superman" not in marvel2:
    print("Superman nincs a listában")
