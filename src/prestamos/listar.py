import pandas as pd

from src.styles import green, warning


def agregar_titulos(prestamos):
    ejemplares = pd.read_csv("data/ejemplares.csv", dtype=str, keep_default_na=False, encoding="utf-8")
    libros = pd.read_csv("data/libros.csv", dtype=str, keep_default_na=False, encoding="utf-8")
    listado = prestamos.merge(ejemplares, left_on="idEjemplar", right_on="codigoInventario", how="left")
    return listado.merge(libros, left_on="idLibro", right_on="ISBN", how="left")


def listar():
    prestamos = pd.read_csv("data/prestamos.csv", dtype=str, keep_default_na=False, encoding="utf-8")
    activos = prestamos[prestamos["fechaDevolucionEfectiva"] == ""]
    print(green("PRÉSTAMOS ACTIVOS"))
    if activos.empty:
        print(warning("No hay préstamos activos."))
        return
    usuarios = pd.read_csv("data/usuarios.csv", dtype=str, keep_default_na=False, encoding="utf-8")
    listado = agregar_titulos(activos).merge(usuarios, left_on="idUsuario", right_on="id", how="left")
    for prestamo in listado.to_dict(orient="records"):
        print(f"ID préstamo: {prestamo['idPrestamo']}")
        print(f"Documento del usuario: {prestamo['documento']}")
        print(f"Nombre del usuario: {prestamo['nombres']}")
        print(f"Código del ejemplar: {prestamo['idEjemplar']}")
        print(f"Título del libro: {prestamo['titulo']}")
        print(f"Fecha de emisión: {prestamo['fechaEmision']}")
        print(f"Fecha de devolución esperada: {prestamo['fechaDevolucionEsperada']}")
        print()
