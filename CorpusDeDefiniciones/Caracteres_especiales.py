def agregar_palabra(archivo, palabra):
    with open(archivo, 'a') as f:
        f.write(palabra + '\n')

def obtener_palabra_usuario():
    return input("Ingrese una palabra para agregar al listado (o 'salir' para terminar): ")

def ejecutar_programa(archivo):
    while True:
        palabra = obtener_palabra_usuario()
        if palabra.lower() == 'salir':
            break
        else:
            agregar_palabra(archivo, palabra)
            print(f'Palabra "{palabra}" agregada al listado.')

    print("Programa terminado.")

def main():
    archivo = 'listado_caracteres.txt'
    ejecutar_programa(archivo)

if __name__ == "__main__":
    main()
