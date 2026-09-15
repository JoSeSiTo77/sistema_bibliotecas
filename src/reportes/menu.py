from src.reportes.dashboard import mostrar_dashboard
from src.reportes.libros_mas_prestados import mostrar_libros_mas_prestados
from src.reportes.prestamos_activos import mostrar_prestamos_activos
from src.reportes.prestamos_vencidos import mostrar_prestamos_vencidos
from src.reportes.usuarios_sancionados import mostrar_usuarios_sancionados
from src.styles import blue, error, green


def mostrar_menu_reportes():
    print(green("========================================\n"
                "               REPORTES\n"
                "========================================"))
    while True:
        print("\n[1] Préstamos activos\n[2] Préstamos vencidos\n[3] Usuarios sancionados"
              "\n[4] Libros más prestados\n[5] Resumen general\n[0] Volver\n")
        opcion = input(blue("Seleccione una opción: ")).strip()
        try:
            if opcion == "0":
                return
            elif opcion == "1":
                mostrar_prestamos_activos()
            elif opcion == "2":
                mostrar_prestamos_vencidos()
            elif opcion == "3":
                mostrar_usuarios_sancionados()
            elif opcion == "4":
                mostrar_libros_mas_prestados()
            elif opcion == "5":
                mostrar_dashboard()
            else:
                print(error("Opción inválida. Intente nuevamente."))
        except (OSError, ValueError) as problema:
            print(error(f"No se pudo generar el reporte: {problema}"))
