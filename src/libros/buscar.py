import pandas as pd

from src.libros.listar import mostrar_libro
from src.styles import blue, error


def buscar():
    while True:
        print("\n[1] ISBN\n[2] Título\n[3] Autor\n[4] Categoría\n[0] Volver")
        opcion = input(blue("Seleccione una opción: ")).strip()
        if opcion == "0":
            return
        if opcion not in ("1", "2", "3", "4"):
            print(error("Opción inválida. Intente nuevamente."))
            continue
        campos = {"1": "ISBN", "2": "titulo", "3": "autor", "4": "categoria"}
        campo = campos[opcion]
        consulta = input("Buscar: ").strip()
        if not consulta:
            print(error("Escriba un valor para buscar."))
            continue
        libros = pd.read_csv("data/libros.csv", dtype=str, keep_default_na=False, encoding="utf-8")
        if campo == "ISBN":
            resultados = libros[libros["ISBN"] == consulta]
        else:
            resultados = libros[libros[campo].str.contains(consulta, case=False, regex=False)]
        if resultados.empty:
            print(error("No se encontraron libros."))
        else:
            for libro in resultados.to_dict(orient="records"):
                mostrar_libro(libro)
