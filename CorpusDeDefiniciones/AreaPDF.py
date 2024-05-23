import tkinter as tk
from tkinter import ttk
import subprocess

# Diccionario para mapear cada opción a una ruta
rutas_compendios = {
    "Salud": "Compendios/Salud",
    "Ingenieria, manufactura y construcción": "Compendios/IngenieriaManufacturaConstruccion",
    "Derecho": "Compendios/Derecho",
    "Ciencias sociales" : "Compendios/CienciasSociales",
    "Artes y humanidades": "Compendios/ArtesHumanidades",
    "Agronomia y veterinaria": "Compendios/AgronomiaVeterinaria",
    "Ciencias exactas y de la computacion": "Compendios/CienciasExactasComputacion"
}
ruta_salida = None

def abrir_area_pdf():
    def seleccionar_ruta_pdf():
        global ruta_salida
        opcion = combo.get()
        if opcion in rutas_compendios:
            ruta_salida = rutas_compendios[opcion]
            print(f"Ruta seleccionada para salida: {ruta_salida}")  # Solo para verificación
            area_pdf.destroy()  # Cerrar la ventana actual
            abrir_seleccionar_pdf()
       

    area_pdf = tk.Toplevel()
    area_pdf.title("Selección de Compendio")
    area_pdf.geometry("500x200")
    
    # Centrar la ventana en la pantalla
    area_pdf.update_idletasks()
    ancho_ventana = area_pdf.winfo_width()
    alto_ventana = area_pdf.winfo_height()
    posicion_x = (area_pdf.winfo_screenwidth() // 2) - (ancho_ventana // 2)
    posicion_y = (area_pdf.winfo_screenheight() // 2) - (alto_ventana // 2)
    area_pdf.geometry(f"+{posicion_x}+{posicion_y}")
    
    # Etiqueta
    label = tk.Label(area_pdf, text="Seleccione el compendio deseado:", font=("Arial", 12))
    label.pack(pady=20)
    
    # Crear un combobox
    combo = ttk.Combobox(area_pdf, values=["Seleccione una opción"] + list(rutas_compendios.keys()), state="readonly")
    combo.pack(pady=10)
    
    # Establecer valor predeterminado
    combo.current(0)

    # Botón para confirmar la selección
    boton_confirmar = tk.Button(area_pdf, text="Confirmar", command=seleccionar_ruta_pdf)
    boton_confirmar.pack(pady=10)

    area_pdf.mainloop()

def abrir_seleccionar_pdf():
    subprocess.run(["python3", "SeleccionarPDF.py",ruta_salida])

# Llamar a la función abrir_area_pdf para iniciar el proceso
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal
    abrir_area_pdf()
