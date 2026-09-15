from src.catalogo.buscar import buscar
from src.catalogo.disponibilidad import consultar_disponibilidad
from src.libros.listar import listar
from src.styles import blue, error, green


def mostrar_menu_catalogo():
    print(green("========================================\n"
                "             CATÁLOGO\n"
                "========================================"))
    while True:
        print("\n[1] Listar catálogo\n[2] Buscar libro"
              "\n[3] Consultar disponibilidad\n[0] Volver\n")
        opcion = input(blue("Seleccione una opción: ")).strip()
        try:
            if opcion == "0":
                return
            elif opcion == "1":
                listar()
            elif opcion == "2":
                buscar()
            elif opcion == "3":
                consultar_disponibilidad()
            else:
                print(error("Opción inválida. Intente nuevamente."))
        except (OSError, ValueError) as problema:
            print(error(f"No se pudo completar la consulta: {problema}"))
