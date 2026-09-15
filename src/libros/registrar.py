import os

import pandas as pd

from src.styles import error, success


def crear_libros_csv():
    os.makedirs("data", exist_ok=True)
    if not os.path.exists("data/libros.csv"):
        libros = pd.DataFrame(columns=["ISBN", "titulo", "autor", "editorial", "categoria"])
        libros.to_csv("data/libros.csv", index=False, encoding="utf-8")


def registrar():
    libros = pd.read_csv("data/libros.csv", dtype=str, keep_default_na=False, encoding="utf-8")
    isbn = input("ISBN: ").strip()
    if not isbn:
        print(error("El ISBN no puede estar vacío."))
        return
    if isbn in libros["ISBN"].values:
        print(error("Ya existe un libro con ese ISBN."))
        return
    titulo = input("Título: ").strip()
    autor = input("Autor: ").strip()
    editorial = input("Editorial: ").strip()
    categoria = input("Categoría: ").strip()
    if not all([titulo, autor, editorial, categoria]):
        print(error("Todos los campos son obligatorios."))
        return
    libros.loc[len(libros)] = [isbn, titulo, autor, editorial, categoria]
    libros.to_csv("data/libros.csv", index=False, encoding="utf-8")
    print(success("Libro registrado correctamente."))
