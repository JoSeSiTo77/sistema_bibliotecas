import pandas as pd

from src.styles import blue, error, success


def modificar():
    isbn = input("ISBN: ").strip()
    libros = pd.read_csv("data/libros.csv", dtype=str, keep_default_na=False, encoding="utf-8")
    coincidencias = libros[libros["ISBN"] == isbn]
    if coincidencias.empty:
        print(error("No existe un libro con ese ISBN."))
        return
    while True:
        print("\n[1] Título\n[2] Autor\n[3] Editorial\n[4] Categoría\n[0] Cancelar")
        opcion = input(blue("Seleccione una opción: ")).strip()
        if opcion == "0":
            return
        if opcion in ("1", "2", "3", "4"):
            break
        print(error("Opción inválida. Intente nuevamente."))
    campos = {"1": "titulo", "2": "autor", "3": "editorial", "4": "categoria"}
    nuevo_valor = input("Nuevo valor: ").strip()
    if not nuevo_valor:
        print(error("El campo no puede estar vacío."))
        return
    libros.loc[coincidencias.index[0], campos[opcion]] = nuevo_valor
    libros.to_csv("data/libros.csv", index=False, encoding="utf-8")
    print(success("Libro modificado correctamente."))
