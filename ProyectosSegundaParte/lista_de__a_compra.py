# Programa Lista de la compra
import os
import time

print('Lista de la compra')

lista = []
vuelta = 1

while "Q" not in lista:  # Ciclo de la lista
    if vuelta == 2:
        print(f'Carrito de compra: {lista}')
    elif len(lista) == 0:
        vuelta += 1

    comprar = input("¿Que deseas comprar? ([Q] para salir)\n"
                    "----> ")
    if comprar == "Q":  # Salir del while
        break
    if comprar in lista:  # Articulos repetidos
        print(f'[/] {comprar} ya está en la lista...')
        time.sleep(1.5)
        os.system("cls")
    elif comprar != "Q":  # Agregar o no el articulo a la lista
        if input(f'Seguro que quieres añadir {comprar} a la lista de la compra [S/N] ') == "S":
            lista.append(comprar)
            print(f'[+] {comprar} ha sido añadido a la lista de la compra.')
            time.sleep(1)
            os.system("cls")
        else:
            print(f'[-] {comprar} no se ha añadido en la lista...')
            time.sleep(1)
            os.system("cls")
# La lista es...
print(f'La lista de la compra es: \n'
      f'-------------------------')
for item in lista:
    print(f'- {item}')
time.sleep(len(lista) + 1)
