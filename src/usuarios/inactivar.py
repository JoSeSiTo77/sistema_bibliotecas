import pandas as pd

from src.styles import error, success, warning


def inactivar():
    documento = input("Documento: ").strip()
    usuarios = pd.read_csv("data/usuarios.csv", dtype=str,
                           keep_default_na=False, encoding="utf-8")
    coincidencias = usuarios[usuarios["documento"].str.strip() == documento]
    if coincidencias.empty:
        print(error("No existe un usuario con ese documento."))
        return
    indice = coincidencias.index[0]
    # El ID inicial de root se conserva aunque se modifiquen su nombre o documento.
    if usuarios.loc[indice, "id"] == "1":
        print(error("No se puede inactivar al usuario root."))
        return
    if usuarios.loc[indice, "estado"] == "Inactivo":
        print(warning("El usuario ya está inactivo."))
        return
    usuarios.loc[indice, "estado"] = "Inactivo"
    usuarios.to_csv("data/usuarios.csv", index=False, encoding="utf-8")
    print(success("Usuario inactivado correctamente."))
