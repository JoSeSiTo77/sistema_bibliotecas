import pandas as pd

from src.styles import blue, error, success


def modificar_estado():
    codigo = input("Código de inventario: ").strip()
    ejemplares = pd.read_csv("data/ejemplares.csv", dtype=str, keep_default_na=False, encoding="utf-8")
    coincidencias = ejemplares[ejemplares["codigoInventario"] == codigo]
    if coincidencias.empty:
        print(error("No existe un ejemplar con ese código de inventario."))
        return
    while True:
        print("\n[1] Disponible\n[2] Prestado\n[3] Deteriorado\n[0] Cancelar")
        opcion = input(blue("Seleccione una opción: ")).strip()
        if opcion == "0":
            return
        if opcion in ("1", "2", "3"):
            break
        print(error("Opción inválida. Intente nuevamente."))
    estados = {"1": "Disponible", "2": "Prestado", "3": "Deteriorado"}
    ejemplares.loc[coincidencias.index[0], "estadoFisico"] = estados[opcion]
    ejemplares.to_csv("data/ejemplares.csv", index=False, encoding="utf-8")
    print(success("Estado físico modificado correctamente."))
