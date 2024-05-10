import fitz
import os
import re

# Ruta al archivo PDF de entrada
ruta_archivo_pdf = "/Users/adielherrera/Downloads/Anatomia .pdf"
# Directorio de salida para el archivo de texto
directorio_salida_texto = "/Users/adielherrera/Downloads/paginas"

# Patrón para reconocer números de página
patron_numeros_pagina = re.compile(r'\d+$')
# Patrón para reconocer pies de página
patron_pies_pagina = re.compile(r'^(?![A-ZÁÉÍÓÚÜ]+[a-záéíóúü]*\d+$)[A-Z]\s*\d+$')

# Función para convertir números romanos a números arábigos
def romano_a_arabigo(numero_romano):
    """
    Convierte un número romano en un número arábigos.

    Args:
        numero_romano (str): El número romano a convertir.

    Returns:
        int: El número arábigos equivalente.
    """
    valores_romanos_a_arabigos = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    numero_arabigo = 0
    prev_valor = 0
    for letra in numero_romano[::-1]:
        valor = valores_romanos_a_arabigos[letra]
        if valor < prev_valor:
            numero_arabigo -= valor
        else:
            numero_arabigo += valor
        prev_valor = valor
    return numero_arabigo

# Función para extraer texto de una página y filtrar elementos no deseados
def extraer_texto_pagina(pagina):
    """
    Extrae el texto de una página y filtra elementos no deseados.

    Args:
        pagina: La página PDF de la que se extraerá el texto.

    Returns:
        str: El texto filtrado de la página.
    """
    texto_pagina = pagina.get_text()
    lineas_texto = texto_pagina.split('\n')
    lineas_filtradas = []

    for linea in lineas_texto:
        # Filtrar números de página y pies de página
        if not patron_numeros_pagina.match(linea) and not patron_pies_pagina.match(linea):
            # Convertir números romanos a números arábigos
            numeros_romanos = re.findall(r'\b[IVXLCDM]+\b', linea)
            for numero_romano in numeros_romanos:
                numero_arabigo = romano_a_arabigo(numero_romano)
                linea = linea.replace(numero_romano, str(numero_arabigo))

            # Eliminar palabras en mayúsculas (suponiendo que son títulos)
            palabras_mayusculas = re.findall(r'\b[A-ZÁÉÍÓÚÜ]{3,}\b', linea)
            for palabra in palabras_mayusculas:
                linea = linea.replace(palabra, '')

            lineas_filtradas.append(linea)
    texto_filtrado = '\n'.join(lineas_filtradas)

    return texto_filtrado

# Abrir el documento PDF
pdf_documento = fitz.open(ruta_archivo_pdf)

texto_final = ''
# Iterar sobre cada página del PDF
for numero_pagina in range(pdf_documento.page_count):
    pagina_actual = pdf_documento[numero_pagina]
    # Extraer y filtrar el texto de la página
    texto_pagina_actual = extraer_texto_pagina(pagina_actual)
    texto_final += texto_pagina_actual + '\n'

# Ruta para el archivo de texto de salida
ruta_archivo_texto_final = "texto_extraido.txt"

# Escribir el texto filtrado en un archivo de texto
with open(ruta_archivo_texto_final, 'w', encoding='utf-8') as archivo_texto_final:
    archivo_texto_final.write(texto_final)

# Cerrar el documento PDF
pdf_documento.close()

print('Texto extraído y guardado en:', ruta_archivo_texto_final)