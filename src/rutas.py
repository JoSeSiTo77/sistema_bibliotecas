"""
    Preparando las rutas y los archivos de datos para que funcionen
    correctamente tanto en Python como en el ejecutable.
"""
import os
import shutil
import sys


def preparar_rutas():
    if getattr(sys, "frozen", False):
        carpeta_aplicacion = os.path.dirname(sys.executable)
        carpeta_data = os.path.join(carpeta_aplicacion, "data")
        os.makedirs(carpeta_data, exist_ok=True)
        for nombre in ("usuarios.csv", "libros.csv", "ejemplares.csv", "prestamos.csv"):
            destino = os.path.join(carpeta_data, nombre)
            if not os.path.exists(destino):
                origen = os.path.join(sys._MEIPASS, "data", nombre)
                shutil.copyfile(origen, destino)
    else:
        carpeta_aplicacion = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Conserva las rutas data/... existentes fuera del directorio temporal de PyInstaller.
    os.chdir(carpeta_aplicacion)
