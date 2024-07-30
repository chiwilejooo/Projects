
SALIDA = "SALIR"
ARCHIVO = "lista_compra.txt"


def preguntar_producto_usuario():
    return input(f"Introduce un producto [{SALIDA} para salir de la lista")


def guardado_lista_compra_a_disco(lista_compra):
    # 1ra forma de hacer un fichero
    # a = open("nombre.txt", "w")
    # a.write("\n".join(lista_compra))
    # a.close()
    with open(ARCHIVO, "w") as mi_archivo:  # forma reducida
        mi_archivo.write("\n".join(lista_compra))


def guardar_item_en_lista(lista_compra, item_a_guardar):
    if item_a_guardar.lower() in [a.lowe() for a in lista_compra]:
        print("El producto ya existe!")
    else:
        lista_compra.append(item_a_guardar)


def cargar_o_crear_lista():
    lista_compra = []
    if input("¿Quieres cargar la última lista de la compra? [S/N]: ") == "S":
        try:
            with open(ARCHIVO, "r") as a:
                lista_compra = a.read().split("\n")
        except FileNotFoundError or FileExistsError:
            print("No existe el archivo de la compra...")
    return lista_compra


def mostrar_lista(lista_compra):
    print("\n".join(lista_compra))


def main():
    lista_compra = cargar_o_crear_lista()
    mostrar_lista(lista_compra)
    input_usuario = preguntar_producto_usuario()

    while input_usuario != SALIDA:
        guardar_item_en_lista(lista_compra, input_usuario)
        input_usuario = preguntar_producto_usuario()
    mostrar_lista(lista_compra)
    guardado_lista_compra_a_disco(lista_compra)


if __name__ == "__main__":
    main()
