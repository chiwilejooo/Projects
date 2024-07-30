import random
import os
import time


VIDA_INICIAL_PIKACHU = 80
VIDA_INICIAL_SQUIRTLE = 90

TAMAÑO_VIDA = 30

vida_pikachu = VIDA_INICIAL_PIKACHU
vida_squirtle = VIDA_INICIAL_SQUIRTLE
endgame = True
rendicion = False

os.system("cls")
nombre_de_usuario = input('¿Cuál es tu nombre de usuario?\n'
                          '----> ')
input("ENTER para continuar...")
os.system("cls")
while endgame:
    # Se desenvuelven los combates

    # Turno de pikachu
    print('Turno de Pikachu - CPU')
    time.sleep(1.5)
    ataque_pikachu = random.randint(1, 2)
    if ataque_pikachu == 1:
        # Bola voltio
        print('-- Pikachu ataca con bola voltio')
        vida_squirtle -= 10
    else:
        # Onda
        print('-- Pikachu ataca con onda Trueno')
        vida_squirtle -= 11

    if vida_pikachu < 0:
        vida_pikachu = 0
        endgame = False
    if vida_squirtle < 0:
        endgame = False

    time.sleep(1)
    barra_de_vida_pikachu = int(vida_pikachu * TAMAÑO_VIDA / VIDA_INICIAL_PIKACHU)
    barra_de_vida_squirtle = int(vida_squirtle * TAMAÑO_VIDA / VIDA_INICIAL_SQUIRTLE)
    print(f"[+] Vida Pikachu:    [{'*' * barra_de_vida_pikachu}{' ' * (TAMAÑO_VIDA - barra_de_vida_pikachu)}] ({vida_pikachu}/"
          f"{VIDA_INICIAL_PIKACHU}) ")
    print(f"[+] Vida Squirtle:   [{'*' * barra_de_vida_squirtle}{' ' * (TAMAÑO_VIDA - barra_de_vida_squirtle)}] ({vida_squirtle}/"
          f"{VIDA_INICIAL_SQUIRTLE}) ")
    os.system("color 47")
    time.sleep(0.2)
    os.system("color 07")
    time.sleep(0.2)
    input('ENTER para continuar...')
    os.system("cls")

    # Turno Squirtle
    print('Turno de Squirtle - P1')
    time.sleep(1)
    ataque_squirtle = None

    while ataque_squirtle != "P" and ataque_squirtle != "A" and ataque_squirtle != "B" and ataque_squirtle != "N" and \
            ataque_squirtle != "Q":
        print(f'- {nombre_de_usuario} ¿Qué ataque deseas realizar? [P]lacaje / Pistola de [A]gua / [B]urbujas / [N]ada '
              f'/ [Q]uit')
        ataque_squirtle = input('----> ')
    time.sleep(1.5)
    if ataque_squirtle == "P":
        print('-- Squirtle ataca con placaje')
        vida_pikachu -= 10
    elif ataque_squirtle == "A":
        print('-- Squirtle ataca con Pistola de Agua')
        vida_pikachu -= 120
    elif ataque_squirtle == "B":
        print('-- Squirtle ataca con Burbuja')
        vida_pikachu -= 11
    elif ataque_squirtle == "Q":
        rendicion = True
        break
    else:
        print(f'-- {nombre_de_usuario} ha decidido que Squirtel no haga nada')
    os.system("cls")

    if vida_pikachu < 0:
        vida_pikachu = 0
        endgame = False
    if vida_squirtle < 0:
        vida_squirtle = 0
        endgame = False
    time.sleep(1)
    barra_de_vida_pikachu = int(vida_pikachu * TAMAÑO_VIDA / VIDA_INICIAL_PIKACHU)
    barra_de_vida_squirtle = int(vida_squirtle * TAMAÑO_VIDA / VIDA_INICIAL_SQUIRTLE)
    print(f"[+] Vida Pikachu:    [{'*' * barra_de_vida_pikachu}{' ' * (TAMAÑO_VIDA - barra_de_vida_pikachu)}] ({vida_pikachu}/"
          f"{VIDA_INICIAL_PIKACHU}) ")
    print(
        f"[+] Vida Squirtle:   [{'*' * barra_de_vida_squirtle}{' ' * (TAMAÑO_VIDA - barra_de_vida_squirtle)}] ({vida_squirtle}/"
        f"{VIDA_INICIAL_SQUIRTLE}) ")

    input('ENTER para continuar...')
    os.system("cls")


if rendicion:
    print('\n')
    time.sleep(0.5)
    print("     ****************************************")
    time.sleep(0.5)
    print("     *                Cobarde               *")
    time.sleep(0.5)
    print("     *                                      *")
    time.sleep(0.5)
    print("     *          Te has rendido :,(          *")
    time.sleep(0.5)
    print("     ****************************************")
    print('\n')
    time.sleep(2.5)
elif vida_pikachu > vida_squirtle:
    print('\n')
    time.sleep(0.5)
    print("     ****************************************")
    time.sleep(0.5)
    print("     *              Lastima :(              *")
    time.sleep(0.5)
    print("     *                                      *")
    time.sleep(0.5)
    print("     *        Pikachu te ha vencido         *")
    time.sleep(0.5)
    print("     ****************************************")
    print('\n')
    time.sleep(2.5)
else:
    print('\n')
    time.sleep(0.5)
    print("     ****************************************")
    time.sleep(0.5)
    print("     *           ¡¡FELICIDADES!!            *")
    time.sleep(0.5)
    print("     *                                      *")
    time.sleep(0.5)
    print("     *      ¡¡Squirtle es el ganador!!      *")
    time.sleep(0.5)
    print("     ****************************************")
    print('\n')
    time.sleep(2.5)

