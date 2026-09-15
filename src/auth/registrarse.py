import os
from getpass import getpass

import bcrypt
import pandas as pd

from src.auth.validar.clave import validar_clave
from src.auth.validar.registrarse import validar_registro, validar_rol
from src.styles import blue, error, success


def crear_usuarios_csv():
    os.makedirs("data", exist_ok=True)
    if os.path.exists("data/usuarios.csv"):
        usuarios = pd.read_csv("data/usuarios.csv", dtype=str,
                               keep_default_na=False, encoding="utf-8")
        if "estado" not in usuarios.columns:
            usuarios.insert(5, "estado", "Activo")
            usuarios.to_csv("data/usuarios.csv", index=False, encoding="utf-8")
        return

    clave_root = bcrypt.hashpw(b"admin123", bcrypt.gensalt()).decode("utf-8")
    usuarios = pd.DataFrame([{
        "id": "1",
        "nombres": "root",
        "documento": "1",
        "clave": clave_root,
        "tipoRol": "Administrador",
        "estado": "Activo",
        "estadoSancion": "null",
        "fechaFinSancion": "null",
    }])
    usuarios.to_csv("data/usuarios.csv", index=False, encoding="utf-8")


def registrarse():
    registrar_usuario()


def seleccionar_rol(permitir_administrador=False):
    while True:
        print("\nSeleccione el rol:\n[1] Aprendiz\n[2] Instructor")
        if permitir_administrador:
            print("[3] Administrador")
        opcion = input(blue("Seleccione una opción: ")).strip()
        if permitir_administrador and opcion == "3":
            return "Administrador"
        tipo_rol = validar_rol(opcion)
        if tipo_rol:
            return tipo_rol
        print(error("Rol inválido. Seleccione una de las opciones disponibles."))


def registrar_usuario(permitir_administrador=False):
    try:
        usuarios = pd.read_csv("data/usuarios.csv", dtype=str,
                               keep_default_na=False, encoding="utf-8")
        nombres = input("Nombres completos: ").strip()
        documento = input("Documento: ").strip()
        mensaje = validar_registro(nombres, documento, usuarios)
        if mensaje:
            print(error(mensaje))
            return

        clave = getpass("Contraseña: ")
        confirmacion = getpass("Confirmar contraseña: ")
        mensaje = validar_clave(clave, confirmacion)
        if mensaje:
            print(error(mensaje))
            return

        tipo_rol = seleccionar_rol(permitir_administrador)

        siguiente_id = 1 if usuarios.empty else int(usuarios["id"].astype(int).max()) + 1
        clave_hash = bcrypt.hashpw(clave.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
        usuarios.loc[len(usuarios)] = {
            "id": str(siguiente_id),
            "nombres": nombres,
            "documento": documento,
            "clave": clave_hash,
            "tipoRol": tipo_rol,
            "estado": "Activo",
            "estadoSancion": "null",
            "fechaFinSancion": "null",
        }
        usuarios.to_csv("data/usuarios.csv", index=False, encoding="utf-8")
    except (EOFError, KeyboardInterrupt):
        print(error("\nRegistro cancelado."))
        return
    except (OSError, ValueError) as problema:
        print(error(f"No se pudo registrar el usuario: {problema}"))
        return

    print(success("Usuario registrado correctamente."))
