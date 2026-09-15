from src.styles import blue, error, green, success
from src.catalogo.menu import mostrar_menu_catalogo
from src.prestamos.historial import consultar_historial


def mostrar_menu_aprendiz(usuario):
    print(green(
        "========================================\n"
        "            MENÚ APRENDIZ\n"
        "========================================"
    ))

    while True:
        print("\n[1] Consultar catálogo\n[2] Historial de préstamos\n[0] Cerrar sesión\n")
        opcion = input(blue("Seleccione una opción: ")).strip()
        if opcion == "0":
            print(success("Sesión cerrada correctamente."))
            return
        elif opcion == "1":
            mostrar_menu_catalogo()
        elif opcion == "2":
            consultar_historial(usuario)
        else:
            print(error("Opción inválida. Intente nuevamente."))
