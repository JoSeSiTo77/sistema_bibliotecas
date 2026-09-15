import pandas as pd

from src.styles import green, warning
from src.sanciones.verificar import verificar_sancion


def mostrar_usuario(usuario):
    verificar_sancion(usuario)
    print(f"ID: {usuario['id']}")
    print(f"Nombres: {usuario['nombres']}")
    print(f"Documento: {usuario['documento']}")
    print(f"Rol: {usuario['tipoRol']}")
    print(f"Estado de sanción: {usuario['estadoSancion']}")
    print(f"Fecha fin de sanción: {usuario['fechaFinSancion']}")
    print()


def listar():
    usuarios = pd.read_csv("data/usuarios.csv", dtype=str,
                           keep_default_na=False, encoding="utf-8")
    print(green("USUARIOS"))
    if usuarios.empty:
        print(warning("No hay usuarios registrados."))
        return
    for usuario in usuarios.to_dict(orient="records"):
        mostrar_usuario(usuario)
