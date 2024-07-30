import random
from os import system

i = 1
monto_total = 0
BRoja = 0

while i == 1:
    bolita = random.randint(1, 3)

    if bolita == 1:
        descuento = 0.4
        BRoja += 1
    elif bolita == 2:
        descuento = 0.25
    else:
        descuento = 0

    monto_compra = int(input(f"Ingrese el monto total de su compra (cliente {i}): "))
    monto_descuento = monto_compra * descuento
    monto_pagar = monto_compra - monto_descuento

    print(f"Monto a pagar (cliente {i + 1}): {monto_pagar}")
    monto_total += monto_pagar
    system("cls")

    i = int(input("[1] para seguir, [0] para cerrar \n"
              "---> "))
    system("cls")


print(f"Monto total a pagar por todos los clientes: {monto_total} \n"
      f"Ganancia de la tienda: {monto_total * 0.3}\n"
      f"Cantidad de veces que eligieron la bolita roja: {BRoja}")

