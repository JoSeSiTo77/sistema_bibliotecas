from datetime import date

import pandas as pd

from src.sanciones.verificar import verificar_sancion
from src.styles import green


def mostrar_dashboard():
    usuarios = pd.read_csv("data/usuarios.csv", dtype=str, keep_default_na=False, encoding="utf-8")
    libros = pd.read_csv("data/libros.csv", dtype=str, keep_default_na=False, encoding="utf-8")
    ejemplares = pd.read_csv("data/ejemplares.csv", dtype=str, keep_default_na=False, encoding="utf-8")
    prestamos = pd.read_csv("data/prestamos.csv", dtype=str, keep_default_na=False, encoding="utf-8")
    activos = prestamos[prestamos["fechaDevolucionEfectiva"] == ""]
    vencidos = activos[activos["fechaDevolucionEsperada"] < date.today().isoformat()]
    sancionados = 0
    for usuario in usuarios.to_dict(orient="records"):
        if verificar_sancion(usuario):
            sancionados += 1

    print(green("========================================\n"
                "          RESUMEN GENERAL\n"
                "========================================"))
    print(f"Usuarios registrados: {len(usuarios)}")
    print(f"Libros registrados: {len(libros)}")
    print(f"Ejemplares registrados: {len(ejemplares)}")
    print()
    print(f"Ejemplares disponibles: {(ejemplares['estadoFisico'] == 'Disponible').sum()}")
    print(f"Ejemplares prestados: {(ejemplares['estadoFisico'] == 'Prestado').sum()}")
    print(f"Ejemplares deteriorados: {(ejemplares['estadoFisico'] == 'Deteriorado').sum()}")
    print()
    print(f"Préstamos activos: {len(activos)}")
    print(f"Préstamos vencidos: {len(vencidos)}")
    print(f"Usuarios sancionados: {sancionados}")
