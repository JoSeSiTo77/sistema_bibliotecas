from src.styles import blue, error, green
from src.usuarios.buscar import buscar
from src.sanciones.listar import listar_sancionados
from src.usuarios.listar import listar
from src.usuarios.modificar import modificar
from src.usuarios.registrar import registrar


def mostrar_menu_usuarios():
    print(green(
        "========================================\n"
        "          GESTIÓN DE USUARIOS\n"
        "========================================"
    ))
    while True:
        print("\n[1] Registrar usuario\n[2] Listar usuarios\n[3] Buscar usuario"
              "\n[4] Modificar usuario\n[5] Usuarios sancionados\n[0] Volver\n")
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
                listar_sancionados()
            else:
                print(error("Opción inválida. Intente nuevamente."))
        except (OSError, ValueError) as problema:
            print(error(f"No se pudo completar la operación: {problema}"))
