from src.auth.registrarse import registrarse
from src.auth.iniciar_sesion import iniciar_sesion
from src.styles import blue, error, green


def mostrar_menu_principal():
    print(green(
        "========================================\n"
        "SISTEMA DE GESTIÓN DE BIBLIOTECA\n"
        "SENA CTM\n"
        "========"
    ))

    while True:
        print("\n[1] Iniciar sesión\n[2] Registrarse\n[0] Salir\n")
        opcion = input(blue("Seleccione una opción: ")).strip()

        if opcion == "0":
            print(green("Cerrando el sistema..."))
            return
        elif opcion == "1":
            iniciar_sesion()
        elif opcion == "2":
            registrarse()
        else:
            print(error("Opción inválida. Intente nuevamente."))
