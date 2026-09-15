import pandas as pd

from src.sanciones.verificar import verificar_sancion
from src.styles import green, warning


def listar_sancionados():
    usuarios = pd.read_csv("data/usuarios.csv", dtype=str, keep_default_na=False, encoding="utf-8")
    print(green("USUARIOS SANCIONADOS"))
    hay_sancionados = False
    for usuario in usuarios.to_dict(orient="records"):
        if verificar_sancion(usuario):
            hay_sancionados = True
            print(f"Documento: {usuario['documento']}")
            print(f"Nombres: {usuario['nombres']}")
            print(f"Rol: {usuario['tipoRol']}")
            print(f"Fecha fin de sanción: {usuario['fechaFinSancion']}")
            print()
    if not hay_sancionados:
        print(warning("No hay usuarios con sanción activa."))
