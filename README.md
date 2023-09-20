# OCR con tesseract y python

Este folder contiene las herramientas para extraer texto de archivos PDF.

El principal archivo es libreta_de_OCR.ipynb, donde está el código ejecutable con sus respectivas instrucciones.

A continuación un resumen de prerequisitos y después instrucciones detalladas.

## Prerequisitos

- Instalar Tesseract y añadir "tesseract" como comando en terminal
- Instalar Python 3, se recomienda una distribución Anaconda o Miniconda
- Tener un venv o ambiente virtual de Anaconda con las necesarias librerías
- Crear un kernel para el jupyter notebook

## Instalar Tesseract

Tesseract es un motor de reconocimiento de texto de código-libre y gratuito. Aquí la [guía oficial](https://tesseract-ocr.github.io/tessdoc/Installation.html). Por default, Tesseract viene sólo con inglés, [esta guía](https://ocrmypdf.readthedocs.io/en/v12.0.2/languages.html) incluye instrucciones para agregar otros idiomas.

## Instalar Python 3

Se recomienda descargar la distribución de [Anaconda](https://docs.anaconda.com/free/anaconda/install/) si la memoria de su equipo no es consideración, o [Miniconda](https://docs.conda.io/projects/miniconda/en/latest/) si desea ahorrar espacio. Conda permite crear ambientes virtuales con todas las librerías necesarias.

## Crear el ambiente virtual

Una vez tenga Anaconda o Miniconda, abra Anaconda Prompt o la terminal en este folder y ejecute la siguiente línea
```
conda env create -f OCRenv.yml
```
y verifique que funcionó con
```
conda activate OCRenv
```

## Crear el kernel

En la terminal, con el ambiente OCRenv activado, ejecute la línea
```
python -m ipykernel install --user --name=OCRenv
```

## Abrir libreta_OCR.ipynb

Listo, ahora puede abrir la libreta en browser (y con el ambiente OCRenv activado) abriendo la terminal en este folder y ejecutando la línea
```
jupyter notebook
```
o, alternativamente, puede solo abrir este folder en un editor como vscode.