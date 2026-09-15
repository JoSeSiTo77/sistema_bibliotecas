import pandas as pd

from src.styles import error
from src.usuarios.listar import mostrar_usuario


def buscar():
    documento = input("Documento: ").strip()
    usuarios = pd.read_csv("data/usuarios.csv", dtype=str,
                           keep_default_na=False, encoding="utf-8")
    coincidencias = usuarios[usuarios["documento"].str.strip() == documento]
    if coincidencias.empty:
        print(error("No existe un usuario con ese documento."))
        return
    mostrar_usuario(coincidencias.iloc[0])
