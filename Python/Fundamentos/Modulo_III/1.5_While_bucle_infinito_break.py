# Caso 2 - Bucle infinito con condicional True - No recomendado
iterador = 0
while True:
    print("Iteración: ", iterador)
    iterador += 1
    if iterador == 10:
        break
