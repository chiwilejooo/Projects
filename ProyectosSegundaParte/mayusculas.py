# Programa que lee las letras mayusculas de un texto...
import string
texto_usuario = input('Escriba aquí ----> ')
mayusculas = 0

for letra in texto_usuario:
    if letra in string.ascii_uppercase:
        mayusculas += 1

print(f'Hay {mayusculas} letras mayusculas en el texto')

