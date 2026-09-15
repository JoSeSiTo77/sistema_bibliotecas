import pandas as pd

from src.styles import green, warning


def listar():
    ejemplares = pd.read_csv("data/ejemplares.csv", dtype=str, keep_default_na=False, encoding="utf-8")
    print(green("EJEMPLARES"))
    if ejemplares.empty:
        print(warning("No hay ejemplares registrados."))
        return
    libros = pd.read_csv("data/libros.csv", dtype=str, keep_default_na=False, encoding="utf-8")
    listado = ejemplares.merge(libros, left_on="idLibro", right_on="ISBN", how="left")
    for ejemplar in listado.to_dict(orient="records"):
        print(f"Código de inventario: {ejemplar['codigoInventario']}")
        print(f"ISBN: {ejemplar['idLibro']}")
        print(f"Título del libro: {ejemplar['titulo']}")
        print(f"Estado físico: {ejemplar['estadoFisico']}")
        print()
