from datetime import date

import pandas as pd

from src.prestamos.listar import agregar_titulos
from src.styles import green, warning


def mostrar_prestamos_vencidos():
    prestamos = pd.read_csv("data/prestamos.csv", dtype=str, keep_default_na=False, encoding="utf-8")
    hoy = date.today()
    activos = prestamos[prestamos["fechaDevolucionEfectiva"] == ""]
    vencidos = activos[activos["fechaDevolucionEsperada"] < hoy.isoformat()]
    print(green("PRÉSTAMOS VENCIDOS"))
    if vencidos.empty:
        print(warning("No hay préstamos vencidos."))
        return
    usuarios = pd.read_csv("data/usuarios.csv", dtype=str, keep_default_na=False, encoding="utf-8")
    listado = agregar_titulos(vencidos).merge(usuarios, left_on="idUsuario", right_on="id", how="left")
    for prestamo in listado.to_dict(orient="records"):
        retraso = (hoy - date.fromisoformat(prestamo["fechaDevolucionEsperada"])).days
        print(f"ID préstamo: {prestamo['idPrestamo']}")
        print(f"Documento: {prestamo['documento']}")
        print(f"Nombre del usuario: {prestamo['nombres']}")
        print(f"Código del ejemplar: {prestamo['idEjemplar']}")
        print(f"Título: {prestamo['titulo']}")
        print(f"Fecha de emisión: {prestamo['fechaEmision']}")
        print(f"Fecha esperada: {prestamo['fechaDevolucionEsperada']}")
        print(f"Días de retraso actuales: {retraso}")
        print()
