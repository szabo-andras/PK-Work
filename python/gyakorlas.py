import math
print("Pitagorasz")
a=int(input("Add meg az első befogót (a)"))
b=int(input("Add meg az második befogót (b)"))
c=pow(pow(a,2)+pow(b,2),0.5)

print(round(c,2))

print("Kör kerülete, és területe (2r*Pi, r2*Pi)")

sugar=float(input("Add meg a kör sugarát:"))

print(math.pi)


print("terület = r2*Pi = ", pow(sugar,2),"*", math.pi,"=", round(pow(sugar,2)*math.pi,1),"cm")
print("kerület = 2*r*Pi = ", 2*sugar,"*", math.pi,"=", round(2*sugar*math.pi,1),"cm")

print("terület = r2*Pi = ", pow(sugar,2),"*", math.pi,"=", round(pow(sugar,2)*math.pi,3),"cm")
print("kerület = 2*r*Pi = ", 2*sugar,"*", math.pi,"=", round(2*sugar*math.pi,3),"cm")