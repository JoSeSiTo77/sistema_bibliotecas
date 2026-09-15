from src.prestamos.devolver import devolver
from src.prestamos.historial import consultar_historial
from src.prestamos.listar import listar
from src.prestamos.registrar import registrar
from src.styles import blue, error, green


def mostrar_menu_prestamos():
    print(green("========================================\n"
                "       PRÉSTAMOS Y DEVOLUCIONES\n"
                "========================================"))
    while True:
        print("\n[1] Registrar préstamo\n[2] Registrar devolución"
              "\n[3] Listar préstamos activos\n[4] Consultar historial de usuario\n[0] Volver\n")
        opcion = input(blue("Seleccione una opción: ")).strip()
        try:
            if opcion == "0":
                return
            elif opcion == "1":
                registrar()
            elif opcion == "2":
                devolver()
            elif opcion == "3":
                listar()
            elif opcion == "4":
                consultar_historial()
            else:
                print(error("Opción inválida. Intente nuevamente."))
        except (OSError, ValueError) as problema:
            print(error(f"No se pudo completar la operación: {problema}"))
