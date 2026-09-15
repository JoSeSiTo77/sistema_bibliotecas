from datetime import date

import pandas as pd


def verificar_sancion(usuario):
    estado = str(usuario["estadoSancion"]).strip().casefold()
    if estado in ("", "null", "false", "sin_sancion", "sin sancion", "inactivo"):
        return False
    fecha_fin = str(usuario["fechaFinSancion"]).strip()
    if fecha_fin in ("", "null"):
        return True
    if date.fromisoformat(fecha_fin) >= date.today():
        return True

    usuarios = pd.read_csv("data/usuarios.csv", dtype=str, keep_default_na=False, encoding="utf-8")
    indice = usuarios["id"] == usuario["id"]
    usuarios.loc[indice, "estadoSancion"] = "False"
    usuarios.loc[indice, "fechaFinSancion"] = "null"
    usuarios.to_csv("data/usuarios.csv", index=False, encoding="utf-8")
    usuario["estadoSancion"] = "False"
    usuario["fechaFinSancion"] = "null"
    return False
