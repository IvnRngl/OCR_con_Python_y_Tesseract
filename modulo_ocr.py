import cv2
from PIL import Image
import pytesseract
import pandas as pd
import numpy as np
import os
import re
from pdf2image import convert_from_path

pdf_ruta_folder = "pdf_folder"

jpg_folder = "imagenes_convertidas_a_jpg"

byn_folder = "imagenes_a_byn"

archivo_txt = "texto.txt"

#se convierten las páginas de un pdf en imágenes individuales, las imágenes son guardadas en un folder /imagenes_convertidas_a_jpg con su repectivo número de página:
def pdf_a_jpg_y_guardar(pdf_nombre: str, pdf_ruta_folder: str = pdf_ruta_folder, ruta_destino: str = jpg_folder, primer_numero_de_pagina: int = 1, dpi: int = 350) -> None:
    '''
    pdf_nombre: nombre (con extensión) del pdf que será convertido en imágenes jpg\n
    pdf_ruta_folder: nombre del folder donde está guardado el pdf\n
    ruta_destino: nombre del folder donde se guardarán las páginas individuales como imágenes jpg\n
    primer_numero_de_pagina: número con que se desea que sea marcada la primera página; 
    las subsecuentes incrementarán en 1\n
    dpi: Dots Per Inch, puede incrementarse para crear imágenes con más contraste. Por default está en 350
    '''
    paginas = convert_from_path(f"{pdf_ruta_folder}/{pdf_nombre}", dpi=dpi)

    i = primer_numero_de_pagina
    for pagina in paginas:
        ruta_y_nombre_de_pagina = f"{ruta_destino}/pagina_{i}.jpg"
        pagina.save(ruta_y_nombre_de_pagina, "JPEG")
        i += 1

#función para pasar imágenes de bgr a escala de grises; es importante definir el número de la página en el parámetro numero_de_pagina
def jpg_a_byn_y_guardar(numero_de_pagina: int, ruta_imagen: str = jpg_folder, ruta_destino: str = byn_folder) -> None:
    '''
    numero_de_pagina: el numero de la página que será convertida a blanco y negro\n
    ruta_imagen: nombre del folder de donde se tomarán las imagen\n
    ruta_destino: nombre del folder donde se guardará la imagen en blanco y negro\n
    '''
    imagen = cv2.imread(f"{ruta_imagen}/pagina_{numero_de_pagina}.jpg")
    imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(f"{ruta_destino}/pagina_{numero_de_pagina}_gris.jpg", imagen_gris)

def obtener_texto(numero_de_pagina: int, ruta_imagen: str = byn_folder, idioma: str = "spa") -> None:
    '''
    numero_de_pagina: número de la página que será convertida a texto\n
    ruta_imagen: nombre del folder de donde se tomará las imagen\n
    nombre_txt: nombre (con extensión) del archivo .txt donde se vaciará el texto de la imagen\n
    idioma: establece el idioma que se espera leer en la imagen; ejemplos incluyen\n
        "spa" = español

        "eng" = inglés
        
        "fra" = francés

        "ita" = italiano

        "deu" = alemán\n
    para usar otros idiomas, éstos deberán ser instalados.
    '''
    texto = pytesseract.image_to_string(Image.open(f"{ruta_imagen}/pagina_{numero_de_pagina}_gris.jpg"), lang=idioma)
    texto: str
    # with open(nombre_txt, mode="w", encoding="utf-8") as file:
    #     file.write(texto)
    print(texto)