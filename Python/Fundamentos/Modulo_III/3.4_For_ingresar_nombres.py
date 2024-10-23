N = int(input("Ingrese la cantidad de alumnos: "))  # ejemplo 3
for i in range(N):
    nombre = input("Nombre {}: ".format(i+1))
    print(f"El alumno {nombre} fue ingresado correctamente: ")
