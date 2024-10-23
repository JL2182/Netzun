# Crear un programa que permita ingresar los nombres de "N" alumnos y la cantidad de cursos por alumno.
N = int(input("Ingrese la cantidad de alumnos: "))  # ejemplo 3
for i in range(N):
    nombre = input("Alumno {}: ".format(i+1))
    M = int(input("Ingrese la cantidad de cursos: "))
    for j in range(M):
        nombre_curso = input("Curso {}: ".format(j+1))
        # print(f"El alumno {nombre} se ha inscrito en el curso {nombre_curso}")
