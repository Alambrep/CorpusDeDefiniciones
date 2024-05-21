def agregar_palabra(archivo, palabra):
    with open(archivo, 'a') as f:
        f.write(palabra + '\n')

def obtener_palabra_usuario():
    while True:
        palabra = input("Ingrese una palabra para agregar al listado (o 'salir' para terminar): ").strip()
        if palabra.lower() == 'salir':
            return 'salir'
        elif palabra:  # Comprueba si la palabra no está vacía
            return palabra
        else:
            print("¡No se puede agregar una palabra vacía!")

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
    archivo = 'corpus_descartes.txt'
    ejecutar_programa(archivo)

if __name__ == "__main__":
    main()
