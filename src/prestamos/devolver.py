from datetime import date

import pandas as pd

from src.styles import error, success, warning
from src.sanciones.calcular import calcular_sancion
from src.sanciones.verificar import verificar_sancion


def devolver():
    identificador = input("ID del préstamo: ").strip()
    prestamos = pd.read_csv("data/prestamos.csv", dtype=str, keep_default_na=False, encoding="utf-8")
    coincidencias = prestamos[prestamos["idPrestamo"] == identificador]
    if coincidencias.empty:
        print(error("No existe un préstamo con ese ID."))
        return
    indice = coincidencias.index[0]
    prestamo = coincidencias.iloc[0]
    if prestamo["fechaDevolucionEfectiva"] != "":
        print(warning("El préstamo ya fue devuelto."))
        return
    ejemplares = pd.read_csv("data/ejemplares.csv", dtype=str, keep_default_na=False, encoding="utf-8")
    coincidencias = ejemplares[ejemplares["codigoInventario"] == prestamo["idEjemplar"]]
    if coincidencias.empty:
        print(error("No existe el ejemplar relacionado con el préstamo."))
        return
    hoy = date.today()
    fecha_esperada = date.fromisoformat(prestamo["fechaDevolucionEsperada"])
    dias_mora = max(0, (hoy - fecha_esperada).days)
    if dias_mora > 0:
        usuarios = pd.read_csv("data/usuarios.csv", dtype=str, keep_default_na=False, encoding="utf-8")
        usuario_encontrado = usuarios[usuarios["id"] == prestamo["idUsuario"]]
        if usuario_encontrado.empty:
            print(error("No existe el usuario relacionado con el préstamo."))
            return
        usuario = usuario_encontrado.iloc[0].to_dict()
        inicio_sancion = hoy
        if verificar_sancion(usuario) and usuario["fechaFinSancion"] not in ("", "null"):
            inicio_sancion = date.fromisoformat(usuario["fechaFinSancion"])
        dias_sancion, fecha_fin = calcular_sancion(dias_mora, inicio_sancion)
    prestamos.loc[indice, "fechaDevolucionEfectiva"] = hoy.isoformat()
    prestamos.loc[indice, "diasMora"] = str(dias_mora)
    prestamos.to_csv("data/prestamos.csv", index=False, encoding="utf-8")
    ejemplares.loc[coincidencias.index[0], "estadoFisico"] = "Disponible"
    ejemplares.to_csv("data/ejemplares.csv", index=False, encoding="utf-8")
    if dias_mora > 0:
        usuarios.loc[usuario_encontrado.index[0], "estadoSancion"] = "True"
        usuarios.loc[usuario_encontrado.index[0], "fechaFinSancion"] = fecha_fin.isoformat()
        usuarios.to_csv("data/usuarios.csv", index=False, encoding="utf-8")
    print(success("Devolución registrada correctamente."))
    print(f"Días de mora: {dias_mora}")
    if dias_mora > 0:
        print(warning(f"Días de sanción: {dias_sancion}"))
        print(warning(f"Sanción hasta: {fecha_fin.isoformat()}"))
