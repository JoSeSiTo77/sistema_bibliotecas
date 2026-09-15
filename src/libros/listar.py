import pandas as pd

from src.styles import green, warning


def mostrar_libro(libro):
    print(f"ISBN: {libro['ISBN']}")
    print(f"Título: {libro['titulo']}")
    print(f"Autor: {libro['autor']}")
    print(f"Editorial: {libro['editorial']}")
    print(f"Categoría: {libro['categoria']}")
    print()


def listar():
    libros = pd.read_csv("data/libros.csv", dtype=str, keep_default_na=False, encoding="utf-8")
    print(green("LIBROS"))
    if libros.empty:
        print(warning("No hay libros registrados."))
        return
    for libro in libros.to_dict(orient="records"):
        mostrar_libro(libro)
