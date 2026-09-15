from getpass import getpass

from src.auth.validar.iniciar_sesion import validar_credenciales
from src.menu.administrador import mostrar_menu_administrador
from src.menu.aprendiz import mostrar_menu_aprendiz
from src.menu.instructor import mostrar_menu_instructor
from src.styles import error, success


def iniciar_sesion():
    print("\nINICIAR SESIÓN")
    while True:
        documento = input("Documento: ").strip()
        if documento == "0":
            return
        clave = getpass("Contraseña: ")
        usuario = validar_credenciales(documento, clave)
        if usuario is None:
            print(error("Documento o contraseña incorrectos."))
            continue

        print(success("Inicio de sesión exitoso."))
        print(f"Bienvenido, {usuario['nombres']}.")
        if usuario["tipoRol"] == "Administrador":
            mostrar_menu_administrador()
        elif usuario["tipoRol"] == "Instructor":
            mostrar_menu_instructor(usuario)
        elif usuario["tipoRol"] == "Aprendiz":
            mostrar_menu_aprendiz(usuario)
        return
