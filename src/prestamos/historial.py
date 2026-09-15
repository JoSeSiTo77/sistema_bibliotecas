import pandas as pd

from src.prestamos.listar import agregar_titulos
from src.styles import error, green, warning


def consultar_historial(usuario=None):
    if usuario is None:
        documento = input("Documento del usuario: ").strip()
        usuarios = pd.read_csv("data/usuarios.csv", dtype=str, keep_default_na=False, encoding="utf-8")
        coincidencias = usuarios[usuarios["documento"] == documento]
        if coincidencias.empty:
            print(error("No existe un usuario con ese documento."))
            return
        usuario = coincidencias.iloc[0]
    prestamos = pd.read_csv("data/prestamos.csv", dtype=str, keep_default_na=False, encoding="utf-8")
    historial = prestamos[prestamos["idUsuario"] == usuario["id"]]
    print(green("HISTORIAL DE PRÉSTAMOS"))
    if historial.empty:
        print(warning("El usuario no tiene préstamos."))
        return
    for prestamo in agregar_titulos(historial).to_dict(orient="records"):
        print(f"ID préstamo: {prestamo['idPrestamo']}")
        print(f"Título del libro: {prestamo['titulo']}")
        print(f"Código del ejemplar: {prestamo['idEjemplar']}")
        print(f"Fecha de emisión: {prestamo['fechaEmision']}")
        print(f"Fecha esperada: {prestamo['fechaDevolucionEsperada']}")
        print(f"Fecha efectiva: {prestamo['fechaDevolucionEfectiva']}")
        print(f"Días de mora: {prestamo['diasMora']}")
        print()
