def agregar_palabra(archivo, palabra):
    # Agrega una palabra al archivo.
    with open(archivo, 'a') as f:
        f.write(palabra + '\n')


def obtener_palabra_usuario():
    # Obtiene una palabra ingresada por el usuario.
    return input("Ingrese una palabra para agregar al listado de palabras clave (o 'salir' para terminar): ")


def ejecutar_programa(archivo):
    # Ejecuta el programa principal.
    while True:
        palabra = obtener_palabra_usuario()
        if palabra.lower() == 'salir':
            break
        else:
            agregar_palabra(archivo, palabra)
            print(f'Palabra "{palabra}" agregada al listado.')

    print("Programa terminado.")


def main():
    # Función principal del programa: Generar o actualizar una lista de palabras clave.
    archivo = 'Listados/listado_palabras_clave.txt'
    ejecutar_programa(archivo)


if __name__ == "__main__":
    main()