
respuesta = None

while respuesta != "A" and respuesta != "B" and respuesta != "C":
    respuesta = input("¿Qué opcion preieres [A, B, C]?\n"
                      "----> ")
    print("Responde alguna de las opciones validas o activa las mayusculas")

if respuesta == "A":
    print("Has elegido bien")
elif respuesta == "B":
    print("Podrias haber elegido mejor")
else:
    print("Elegiste mal")

