import os

import pandas as pd

from src.styles import error, success


def crear_ejemplares_csv():
    os.makedirs("data", exist_ok=True)
    if not os.path.exists("data/ejemplares.csv"):
        ejemplares = pd.DataFrame(columns=["codigoInventario", "idLibro", "estadoFisico"])
        ejemplares.to_csv("data/ejemplares.csv", index=False, encoding="utf-8")


def registrar():
    codigo = input("Código de inventario: ").strip()
    if not codigo:
        print(error("El código de inventario no puede estar vacío."))
        return
    ejemplares = pd.read_csv("data/ejemplares.csv", dtype=str, keep_default_na=False, encoding="utf-8")
    if codigo in ejemplares["codigoInventario"].values:
        print(error("Ya existe un ejemplar con ese código de inventario."))
        return
    isbn = input("ISBN del libro: ").strip()
    libros = pd.read_csv("data/libros.csv", dtype=str, keep_default_na=False, encoding="utf-8")
    if isbn not in libros["ISBN"].values:
        print(error("No existe un libro con ese ISBN."))
        return
    ejemplares.loc[len(ejemplares)] = [codigo, isbn, "Disponible"]
    ejemplares.to_csv("data/ejemplares.csv", index=False, encoding="utf-8")
    print(success("Ejemplar registrado correctamente."))
