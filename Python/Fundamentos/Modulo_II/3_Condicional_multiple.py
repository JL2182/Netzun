# crear un programa que permita ingresar un número e indicar si es positivo, negativo o cero.
x = int(input("Ingrese un número: "))
if x > 0:
    print("El número es positivo")
elif x < 0:
    print("El número es negativo")
else:
    print("El número es cero")
print(type(x))
