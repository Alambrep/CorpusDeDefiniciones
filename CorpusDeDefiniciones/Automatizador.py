import sys
import os
import subprocess
import shutil
from tkinter import messagebox

class Main:
    def __init__(self, ruta_pdf, ruta_salida):
        self.ruta_pdf = ruta_pdf
        self.ruta_archivo_csv_salida = "TextoExtraido/definiciones_mejoradas.csv"
        self.ruta_salida = ruta_salida

    def ejecutar(self):
        self.print_comprobar()
        self.extraer_pdf_a_texto()
        self.depurar_contenido()
        self.extraer_oraciones_con_palabras()
        self.extraer_definiciones()
        self.corregir_redaccion()
        self.limpiar_archivos()
        
    def print_comprobar(self):
        print(f"Ruta seleccionada para pdf transferida al automatizador: {self.ruta_pdf}")
        print(f"Ruta seleccionada para salida transferida al automatizador: {self.ruta_salida}")

    def extraer_pdf_a_texto(self):
        print(f"Ejecutando ExtractorDePDF.py para {self.ruta_pdf}...")
        resultado = subprocess.run(["python3", "ExtractorDePDF.py", self.ruta_pdf])
        if resultado.returncode != 0:
            print("Error al ejecutar ExtractorDePDF.py")
            sys.exit(1)
        print("ExtractorDePDF.py ejecutado exitosamente.") 

    def depurar_contenido(self):
        print("Ejecutando DepuradorDeContenido.py...")
        resultado = subprocess.run(["python3", "DepuradorDeContenido.py"])
        if resultado.returncode != 0:
            print("Error al ejecutar DepuradorDeContenido.py")
            sys.exit(1)
        print("DepuradorDeContenido.py ejecutado exitosamente.") 

    def extraer_oraciones_con_palabras(self):
        print("Ejecutando ExtractorDeOraciones.py...")
        resultado = subprocess.run(["python3", "ExtractorDeOraciones.py"])
        if resultado.returncode != 0:
            print("Error al ejecutar ExtractorDeOraciones.py")
            sys.exit(1)
        print("ExtractorDeOraciones.py ejecutado exitosamente.") 

    def extraer_definiciones(self):
        print("Ejecutando ExtractorDeDefiniciones.py...")
        resultado = subprocess.run(["python3", "ExtractorDeDefiniciones.py"])
        if resultado.returncode != 0:
            print("Error al ejecutar ExtractorDeDefiniciones.py")
            sys.exit(1)
        print("ExtractorDeDefiniciones.py ejecutado exitosamente.")

    def corregir_redaccion(self):
        print("Ejecutando CorrectorDeRedaccion.py...")
        resultado = subprocess.run(["python3", "CorrectorDeRedaccion.py"])
        if resultado.returncode != 0:
            print("Error al ejecutar CorrectorDeRedaccion.py")
            sys.exit(1)
        print("CorrectorDeRedaccion.py ejecutado exitosamente.")

    def limpiar_archivos(self):
        try:
            # Mover el archivo "definiciones_mejoradas.csv" a la ruta seleccionada
            shutil.move(self.ruta_archivo_csv_salida, os.path.join(self.ruta_salida, "definiciones_mejoradas.csv"))
            print(f"Archivo movido a la carpeta '{self.ruta_salida}'")
            messagebox.showinfo("Información","Se ha generado el archivo csv")

            # Eliminar archivos restantes en "TextoExtraido"
            for archivo in os.listdir("TextoExtraido"):
                ruta_archivo = os.path.join("TextoExtraido", archivo)
                os.remove(ruta_archivo)
                print(f"Archivo eliminado: {ruta_archivo}")
        except Exception as e:
            print(f"Error al limpiar archivos: {str(e)}")

# Instanciar y ejecutar la clase Main con la ruta del PDF y la ruta de salida pasadas como argumentos
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python Automatizador.py <ruta_pdf> <ruta_salida>")
        sys.exit(1)
    
    ruta_pdf = sys.argv[1]
    ruta_salida = sys.argv[2]
    main = Main(ruta_pdf, ruta_salida)
    main.ejecutar()
