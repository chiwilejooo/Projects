# Lea lista de numero de ususario  diga de todos los numero cual es el mayo y cual es el menor.
"""# Opcion 1
import os
lista_numeros = []
numeros = None
while numeros != 0.0:
    print(lista_numeros)
    numeros = int(input('[00] para salir\n'
                        'Números ----> '))
    if numeros != 0.0:
        lista_numeros.append(numeros)
        os.system("cls")
    elif numeros == 0.0:
        break
print(f'El numero de mayor valor en tu lista es: {max(lista_numeros)}\n'
      f'El numero de menor valor en tu lista es: {min(lista_numeros)}')"""

# Opcion 2


numeros_introducidos = input("Introduzca los numero separados por coma: ")
numeros_de_usuario = [int(numero) for numero in numeros_introducidos.split(",")]  # Otras funciones del for...

num_chico = numeros_de_usuario[0]
num_grande = numeros_de_usuario[0]
for numero in numeros_de_usuario[1:]:
    if num_chico > numero:
        num_chico = numero
    if num_grande < numero:
        num_grande = numero
print(f'Numero mas grande: {num_grande}, Numero mas pequeño. {num_chico}')
# Resultado mas corto comparado al anterior

