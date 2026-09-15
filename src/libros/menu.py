from src.libros.buscar import buscar
from src.libros.ejemplares.menu import mostrar_menu_ejemplares
from src.libros.listar import listar
from src.libros.modificar import modificar
from src.libros.registrar import registrar
from src.styles import blue, error, green


def mostrar_menu_libros():
    print(green("========================================\n"
                "           GESTIÓN DE LIBROS\n"
                "========================================"))
    while True:
        print("\n[1] Registrar libro\n[2] Listar libros\n[3] Buscar libro"
              "\n[4] Modificar libro\n[5] Gestión de ejemplares\n[0] Volver\n")
        opcion = input(blue("Seleccione una opción: ")).strip()
        try:
            if opcion == "0":
                return
            elif opcion == "1":
                registrar()
            elif opcion == "2":
                listar()
            elif opcion == "3":
                buscar()
            elif opcion == "4":
                modificar()
            elif opcion == "5":
                mostrar_menu_ejemplares()
            else:
                print(error("Opción inválida. Intente nuevamente."))
        except (OSError, ValueError) as problema:
            print(error(f"No se pudo completar la operación: {problema}"))
