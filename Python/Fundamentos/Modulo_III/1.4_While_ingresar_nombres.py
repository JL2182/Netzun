# Crear un programa que permita ingresar los nombres de "N" alumnos de un curso.
Num_alumnos = int(input("Ingrese el número de alumnos: "))
i = 1
while Num_alumnos >= i:
    nombre = input("Ingrese el nombre del alumno {}: ".format(i))
    i += 1
