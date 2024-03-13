x = float (input("escribe un numero: "))
y = float (input("escribe otro numero:"))
z = float (input("es ribe el ultimo numero: "))
if x > y > z: 
    print(str(x) + " es el mayor numero")
elif z > y > x:
    print(str(z) + " es el mayor numero")
else:
    print(str(y) + " es el mayor numero")