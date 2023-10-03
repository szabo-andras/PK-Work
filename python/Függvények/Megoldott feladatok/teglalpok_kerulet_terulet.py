"""Készítsünk téglalapokat, amelyeknek számoljuk ki a területeit
"""


class Teglalap:
    """ 
    def teglalapok_szama(self,darabszam):
        
        
        print("Jelenleg",darabszam ,"téglalapod van") """
    def __init__(self,a,b):
        self.a= a
        self.b= b
    
    def terulet(self):
        T=a*b
        print("A Téglalap területe=",T)
    
    def kerulet(self):
        K=2*(a+b)
        print("A Téglalap kerülete=",K)

    def oldalkiiratas(self,a,b):
        print("A oldal hossza:",a)
        print("B oldal hossza:",b)

a=False
b=False

while a==False:
    try:
        a=int(input("A oldal hossza:"))
    except:
        print("Egy pozitív számot adj meg légyszíves")
while b==False:
    try:
        b=int(input("B oldal hossza:"))
    except:
        print("Egy pozitív számot adj meg légyszíves")

egy_teglalap=Teglalap(a,b)
egy_teglalap.terulet()
# egy_teglalap.teglalapok_szama()

