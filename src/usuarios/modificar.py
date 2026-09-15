import pandas as pd

from src.auth.registrarse import seleccionar_rol
from src.auth.validar.registrarse import validar_registro
from src.styles import blue, error, success


def modificar():
    documento = input("Documento: ").strip()
    usuarios = pd.read_csv("data/usuarios.csv", dtype=str,
                           keep_default_na=False, encoding="utf-8")
    coincidencias = usuarios[usuarios["documento"].str.strip() == documento]
    if coincidencias.empty:
        print(error("No existe un usuario con ese documento."))
        return
    indice = coincidencias.index[0]

    while True:
        print("\n[1] Nombres\n[2] Documento\n[3] Rol\n[0] Cancelar")
        opcion = input(blue("Seleccione una opción: ")).strip()
        if opcion == "0":
            return
        if opcion in ("1", "2", "3"):
            break
        print(error("Opción inválida. Intente nuevamente."))

    if opcion == "1":
        nombres = input("Nombres completos: ").strip()
        if not nombres:
            print(error("Los nombres no pueden estar vacíos."))
            return
        usuarios.loc[indice, "nombres"] = nombres
    elif opcion == "2":
        nuevo_documento = input("Nuevo documento: ").strip()
        mensaje = validar_registro(usuarios.loc[indice, "nombres"], nuevo_documento,
                                   usuarios.drop(index=indice))
        if mensaje:
            print(error(mensaje))
            return
        usuarios.loc[indice, "documento"] = nuevo_documento
    else:
        usuarios.loc[indice, "tipoRol"] = seleccionar_rol(permitir_administrador=True)

    usuarios.to_csv("data/usuarios.csv", index=False, encoding="utf-8")
    print(success("Usuario modificado correctamente."))
