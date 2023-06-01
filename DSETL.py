import re
import os

def transformar_archivo(nombre_archivo):
    lineas_transformadas = []

    with open(nombre_archivo, 'r') as archivo:
        mapudungun = ""
        for linea in archivo:
            if linea.startswith('M:'):
                mapudungun = linea.split(':')[1].strip()
            elif linea.startswith('C:'):
                castellano = linea.split(':')[1].strip()
                patron_efectos = r"<.*?>"
                patron_comas = r","
                patron_puntos = r"\."
                castellano = re.sub(patron_efectos, '', castellano)
                mapudungun = re.sub(patron_efectos, '', mapudungun)
                castellano = re.sub(patron_comas, '', castellano)
                mapudungun = re.sub(patron_comas, '', mapudungun)
                castellano = re.sub(patron_puntos, '', castellano)
                mapudungun = re.sub(patron_puntos, '', mapudungun)
                linea_transformada = castellano + ', ' + mapudungun
                lineas_transformadas.append(linea_transformada)

    return lineas_transformadas

def concatenar_linea(nombre_archivo, linea):
    with open(nombre_archivo, 'a') as archivo:
        archivo.write(linea + '\n')

def listar_archivos_txt(carpeta):
    archivos_txt = []
    for archivo in os.listdir(carpeta):
        if archivo.endswith(".txt"):
            archivos_txt.append(archivo)
    return archivos_txt


carpeta = "./input"  # Reemplaza con la ruta a la carpeta que deseas explorar
archivos_txt = listar_archivos_txt(carpeta)

for archivo in archivos_txt:
    resultado = transformar_archivo("./input/" + archivo)
    print("Transformando archivo: " + archivo + "...")
    for linea in resultado:
        print("Concatenando linea: " + linea + "...")
        concatenar_linea('output.txt', linea)