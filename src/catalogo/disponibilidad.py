import pandas as pd

from src.styles import error, success, warning


def consultar_disponibilidad():
    isbn = input("ISBN: ").strip()
    libros = pd.read_csv("data/libros.csv", dtype=str, keep_default_na=False, encoding="utf-8")
    coincidencias = libros[libros["ISBN"] == isbn]
    if coincidencias.empty:
        print(error("No existe un libro con ese ISBN."))
        return

    libro = coincidencias.iloc[0]
    ejemplares = pd.read_csv("data/ejemplares.csv", dtype=str,
                             keep_default_na=False, encoding="utf-8")
    ejemplares_libro = ejemplares[ejemplares["idLibro"] == isbn]
    disponibles = (ejemplares_libro["estadoFisico"] == "Disponible").sum()
    prestados = (ejemplares_libro["estadoFisico"] == "Prestado").sum()
    deteriorados = (ejemplares_libro["estadoFisico"] == "Deteriorado").sum()

    print(f"Título: {libro['titulo']}")
    print(f"ISBN: {isbn}")
    print(f"Total de ejemplares: {len(ejemplares_libro)}")
    print(f"Disponibles: {disponibles}")
    print(f"Prestados: {prestados}")
    print(f"Deteriorados: {deteriorados}")
    if disponibles > 0:
        print(success("Disponibilidad: Disponible"))
    else:
        print(warning("Disponibilidad: No disponible"))
