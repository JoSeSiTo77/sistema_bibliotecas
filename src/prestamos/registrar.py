import os
from datetime import date

import pandas as pd

from src.styles import error, success
from src.sanciones.verificar import verificar_sancion


def crear_prestamos_csv():
    os.makedirs("data", exist_ok=True)
    if not os.path.exists("data/prestamos.csv"):
        prestamos = pd.DataFrame(columns=[
            "idPrestamo", "idEjemplar", "idUsuario", "fechaEmision",
            "fechaDevolucionEsperada", "fechaDevolucionEfectiva", "diasMora"
        ])
        prestamos.to_csv("data/prestamos.csv", index=False, encoding="utf-8")


def registrar():
    documento = input("Documento del usuario: ").strip()
    usuarios = pd.read_csv("data/usuarios.csv", dtype=str, keep_default_na=False, encoding="utf-8")
    coincidencias = usuarios[usuarios["documento"] == documento]
    if coincidencias.empty:
        print(error("No existe un usuario con ese documento."))
        return
    usuario = coincidencias.iloc[0]
    hoy = date.today()
    if verificar_sancion(usuario):
        print(error("El usuario tiene una sanción activa."))
        print(error(f"Sanción hasta: {usuario['fechaFinSancion']}"))
        return
    codigo = input("Código de inventario del ejemplar: ").strip()
    ejemplares = pd.read_csv("data/ejemplares.csv", dtype=str, keep_default_na=False, encoding="utf-8")
    coincidencias = ejemplares[ejemplares["codigoInventario"] == codigo]
    if coincidencias.empty:
        print(error("No existe un ejemplar con ese código de inventario."))
        return
    indice = coincidencias.index[0]
    if ejemplares.loc[indice, "estadoFisico"] != "Disponible":
        print(error("El ejemplar no está Disponible."))
        return
    prestamos = pd.read_csv("data/prestamos.csv", dtype=str, keep_default_na=False, encoding="utf-8")
    activos = prestamos[(prestamos["idEjemplar"] == codigo)
                        & (prestamos["fechaDevolucionEfectiva"] == "")]
    if not activos.empty:
        print(error("El ejemplar ya tiene un préstamo activo."))
        return
    texto_fecha = input("Fecha de devolución esperada: ").strip()
    try:
        fecha_esperada = date.fromisoformat(texto_fecha)
    except ValueError:
        print(error("Fecha inválida. Utilice YYYY-MM-DD."))
        return
    if fecha_esperada.isoformat() != texto_fecha or fecha_esperada <= hoy:
        print(error("La fecha debe usar YYYY-MM-DD y ser posterior a la emisión."))
        return
    siguiente_id = 1 if prestamos.empty else int(prestamos["idPrestamo"].astype(int).max()) + 1
    prestamos.loc[len(prestamos)] = [str(siguiente_id), codigo, usuario["id"],
                                    hoy.isoformat(), fecha_esperada.isoformat(), "", "0"]
    prestamos.to_csv("data/prestamos.csv", index=False, encoding="utf-8")
    ejemplares.loc[indice, "estadoFisico"] = "Prestado"
    ejemplares.to_csv("data/ejemplares.csv", index=False, encoding="utf-8")
    print(success("Préstamo registrado correctamente."))
