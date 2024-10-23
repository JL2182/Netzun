# Crear un programa que permita ingresar los nombres de "N" amumnos y la cantidad "M" de cursos por alumno.
N = int(input("Ingrese el número de alumnos: "))  # por ejemplo 3

i = 1
j = 0  # Variable auxiliar para contar los cursos

while N >= i:
    nombre = input("Ingrese el nombre del Alumno {}: ".format(i))
    M = int(input("Ingrese la cantidad de cursos: "))
    j = 0  # Variable auxiliar para contar los cursos
    while M > j:
        nombre_curso = input("Curso {}: ".format(j+1))
        j += 1
    i += 1
