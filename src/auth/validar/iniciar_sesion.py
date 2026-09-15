import bcrypt
import pandas as pd


def validar_credenciales(documento, clave):
    usuarios = pd.read_csv("data/usuarios.csv", dtype=str,
                           keep_default_na=False, encoding="utf-8")
    coincidencias = usuarios[usuarios["documento"] == documento.strip()]
    if coincidencias.empty:
        return None

    usuario = coincidencias.iloc[0].to_dict()
    if usuario["estado"] == "Inactivo":
        return None
    try:
        clave_correcta = bcrypt.checkpw(
            clave.encode("utf-8"), usuario["clave"].encode("utf-8")
        )
    except ValueError:
        return None
    if clave_correcta:
        return usuario
    return None
