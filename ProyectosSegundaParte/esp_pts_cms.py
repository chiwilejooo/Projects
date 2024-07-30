# Programa que de un texto introducido por el usuario lea cuantos espacios, cuantos puntos y cuantas comas tiene.
espacio = 0
puntos = 0
coma = 0
texto = input('Escribe aqui ---> ')

for letra in texto:
    if letra == " ":
        espacio += 1
    elif letra == ".":
        puntos += 1
    elif letra == ",":
        coma += 1
print(f'Se han encontrado un total de:\n'
      f'"{espacio}" espacios\n'
      f'"{puntos}" puntos y\n'
      f'"{coma}" comas en el texto.')
