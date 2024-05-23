import csv
import os
import sys
import subprocess
import tkinter as tk
from tkinter import messagebox, Menu
import unicodedata

class DefinicionBuscador:
    def __init__(self, archivo_csv):
        self.archivo_csv = archivo_csv
        if not os.path.isfile(self.archivo_csv):
            messagebox.showerror("Error", f"No se encontró el archivo: {self.archivo_csv}")
            raise FileNotFoundError(f"No se encontró el archivo: {self.archivo_csv}")

    def buscar_definicion(self, termino):
        termino = self.normalizar_texto(termino)
        try:
            with open(self.archivo_csv, newline='', encoding='utf-8') as csvfile:
                lector_csv = csv.reader(csvfile)
                for fila in lector_csv:
                    concepto, definicion = fila
                    concepto_normalizado = self.normalizar_texto(concepto)
                    if termino in concepto_normalizado:
                        return definicion.strip().strip('"')
            return "Definición no encontrada."
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al leer el archivo: {e}")
            return "Error al buscar la definición."

    @staticmethod
    def normalizar_texto(texto):
        texto = texto.lower()
        texto = unicodedata.normalize("NFKD", texto)
        texto = "".join([c for c in texto if not unicodedata.combining(c)])
        return texto
    
def salir():
    root.destroy
    
def volver_a_home():
    salir()
    subprocess.run(["python3", "Home.py"])

class InterfazBuscador:
    def __init__(self, master, archivo_csv):
        try:
            self.buscador = DefinicionBuscador(archivo_csv)
        except FileNotFoundError:
            master.destroy()
            return
        self.master = master
        self.master.title("Buscador de Definiciones")
        
        # Barra de menú
        barra_menu = tk.Menu(root)
        root.config(menu=barra_menu)

        # Menú "Opciones"
        menu_opciones = tk.Menu(barra_menu, tearoff=0)
        barra_menu.add_cascade(label="Opciones", menu=menu_opciones)
        menu_opciones.add_command(label="Home",command=volver_a_home)
        menu_opciones.add_command(label="Salir", command=salir)

        self.label = tk.Label(
            master, text="Ingrese el término que desea buscar:"
        )
        self.label.pack(pady=10)

        self.termino_entry = tk.Entry(master, width=50)
        self.termino_entry.pack(pady=10)

        self.boton_buscar = tk.Button(
            master, text="Buscar", command=self.buscar_definicion
        )
        self.boton_buscar.pack(pady=10)

        self.resultado_label = tk.Label(master, text="", wraplength=400)
        self.resultado_label.pack(pady=10)

    def buscar_definicion(self):
        termino = self.termino_entry.get().strip()
        if termino:
            definicion = self.buscador.buscar_definicion(termino)
            self.resultado_label.config(
                text=f"Definición de '{termino}': {definicion}"
            )
        else:
            messagebox.showwarning(
                "Entrada vacía", "Por favor, ingrese un término para buscar."
            )

def centrar_ventana(root, ancho=500, alto=200):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x_cordinate = int((screen_width / 2) - (ancho / 2))
    y_cordinate = int((screen_height / 2) - (alto / 2))

    root.geometry(f"{ancho}x{alto}+{x_cordinate}+{y_cordinate}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python3 BuscadorDeDefinicion.py <ruta_del_archivo_csv>")
        sys.exit(1)
    
    archivo_csv = sys.argv[1]
    archivo_csv = os.path.join(archivo_csv, "definiciones_mejoradas.csv")  

    root = tk.Tk()
    centrar_ventana(root)
    interfaz = InterfazBuscador(root, archivo_csv)
    root.mainloop()
