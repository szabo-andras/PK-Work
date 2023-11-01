valamilyen_többsoros_szöveg = '''\
Ez egy több
soros
szöveg, amit beíratok
egy fájlba.

[András Szabó]
'''

file = open ("fajlnev.txt", "w")
file.write(valamilyen_többsoros_szöveg)
file.close()

file = open("fajlnev.txt") #alapértelmezetten read/olvasási mód

while True:
    egy_sor = file.readline()
    if len(egy_sor) == 0:
        break
    print(egy_sor, end="")
file.close()
