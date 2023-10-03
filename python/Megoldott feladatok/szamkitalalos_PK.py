from random import randint


def beker():
    flag = True
    while flag:  # vagy flag == True
        try:
            tipp = int(input('Mi a tipped? (1-100) '))
            if 0 < tipp <= 100:
                flag = False
        except:
            print('Nem megfelelő adatbevitel!')
    return tipp


def vizsgal(f, t):  # f: feladvány, t: tipp
    if f == t:
        return True
    elif f < t:
        print("Kisebb számra gondoltam!")
        return False
    else:
        print("Nagyobb számra gondoltam!")
        return False


def jatek():
    feladvany = randint(1, 100)
    while not vizsgal(feladvany, beker()):
        pass
    print("Eltaláltad!")


# Fő program kezdete
flag = input('Indulhat a játék? (i/n) ')
while flag == 'i':
    jatek()
    flag = input('Akarsz még játszani? (i/n) ')
print("Viszlát!")