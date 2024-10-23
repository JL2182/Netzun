""" Crear un programa que permita ingresar la edad deuna persona
e indicar si es mayor de edad o menor de edad.
Si es menor de edad, validar si el valor es mayor a cero,
sino indicar que la edad no es correcta."""

edad = int(input("Ingrese su edad por favor: "))
if edad >= 18:
    print("Usted es mayor de edad")
else:
    if edad > 0:
        print("Usted es menor de edad")
    else:
        print("La edad ingresada no es correcta")
