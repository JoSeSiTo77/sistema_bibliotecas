import pandas as pd

from src.prestamos.listar import agregar_titulos
from src.styles import green, warning


def mostrar_libros_mas_prestados():
    prestamos = pd.read_csv("data/prestamos.csv", dtype=str, keep_default_na=False, encoding="utf-8")
    print(green("LIBROS MÁS PRESTADOS"))
    if prestamos.empty:
        print(warning("No hay préstamos registrados."))
        return
    listado = agregar_titulos(prestamos)
    cantidades = listado.groupby(["ISBN", "titulo"]).size().reset_index(name="cantidad")
    cantidades = cantidades.sort_values("cantidad", ascending=False)
    for libro in cantidades.to_dict(orient="records"):
        print(f"ISBN: {libro['ISBN']}")
        print(f"Título: {libro['titulo']}")
        print(f"Cantidad de préstamos: {libro['cantidad']}")
        print()
