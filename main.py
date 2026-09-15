from colorama import init

from src.auth.registrarse import crear_usuarios_csv
from src.libros.registrar import crear_libros_csv
from src.libros.ejemplares.registrar import crear_ejemplares_csv
from src.menu.principal import mostrar_menu_principal
from src.prestamos.registrar import crear_prestamos_csv
from src.rutas import preparar_rutas


# Colorama se inicializa aquí para habilitar los colores en toda la aplicación.
init()


def main():
    preparar_rutas()
    crear_usuarios_csv()
    crear_libros_csv()
    crear_ejemplares_csv()
    crear_prestamos_csv()
    mostrar_menu_principal()


if __name__ == "__main__":
    main()
