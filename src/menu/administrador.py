from src.styles import blue, error, green, success
from src.usuarios.menu import mostrar_menu_usuarios
from src.libros.menu import mostrar_menu_libros
from src.prestamos.menu import mostrar_menu_prestamos
from src.reportes.menu import mostrar_menu_reportes


def mostrar_menu_administrador():
    print(green(
        "========================================\n"
        "          MENÚ ADMINISTRADOR\n"
        "========================================"
    ))

    while True:
        print("\n[1] Gestión de usuarios\n[2] Gestión de libros"
              "\n[3] Préstamos y devoluciones\n[4] Reportes\n[0] Cerrar sesión\n")
        opcion = input(blue("Seleccione una opción: ")).strip()
        if opcion == "0":
            print(success("Sesión cerrada correctamente."))
            return
        elif opcion == "1":
            mostrar_menu_usuarios()
        elif opcion == "2":
            mostrar_menu_libros()
        elif opcion == "3":
            mostrar_menu_prestamos()
        elif opcion == "4":
            mostrar_menu_reportes()
        else:
            print(error("Opción inválida. Intente nuevamente."))
