"""
Ejercicio 1: La string más larga
Crea una funcion que reciba una lista de strings como entrada y te diga cual es la más larga de todas
Ejemplo:
string_mas_larga("hola", "como", "estas")
> "estas\"
"""


def string_mas_larga(*args):
    palabras = []
    for n in args:
        palabras.append(n)
    for palabra in palabras:
        mas_largo = 1
        palabra_mas_larga = ""
        if len(palabra) > mas_largo:
            mas_largo = len(palabra)
            palabra_mas_larga = palabra
    return mas_largo, palabra_mas_larga


def main():
    print(string_mas_larga("hola", "como", "estas"))


if __name__ == '__main__':
    main()
