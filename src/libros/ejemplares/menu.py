from src.libros.ejemplares.listar import listar
from src.libros.ejemplares.modificar_estado import modificar_estado
from src.libros.ejemplares.registrar import registrar
from src.styles import blue, error, green


def mostrar_menu_ejemplares():
    print(green("========================================\n"
                "        GESTIÓN DE EJEMPLARES\n"
                "========================================"))
    while True:
        print("\n[1] Registrar ejemplar\n[2] Listar ejemplares"
              "\n[3] Modificar estado físico\n[0] Volver\n")
        opcion = input(blue("Seleccione una opción: ")).strip()
        try:
            if opcion == "0":
                return
            elif opcion == "1":
                registrar()
            elif opcion == "2":
                listar()
            elif opcion == "3":
                modificar_estado()
            else:
                print(error("Opción inválida. Intente nuevamente."))
        except (OSError, ValueError) as problema:
            print(error(f"No se pudo completar la operación: {problema}"))
