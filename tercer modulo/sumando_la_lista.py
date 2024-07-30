"""
Ejercicio 2: Sumando la lista
Crea una función que sume una lista de números, no se vale usar la función sum()
Ejemplo:
suma([1, 2, 3, 4, 5])
> 15
"""


def suma(num):
    total = 0
    for n in num:
        total += n
    print(f'La suma de la lista es: {total}')


def main():
    suma([1, 2, 3, 4, 5])


if __name__ == '__main__':
    main()
