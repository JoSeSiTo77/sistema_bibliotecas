from colorama import Fore, Style


def bold(text):
    return Style.BRIGHT + str(text) + Style.NORMAL


def red(text):
    return Fore.RED + str(text) + Fore.RESET


def green(text):
    return Fore.GREEN + str(text) + Fore.RESET


def yellow(text):
    return Fore.YELLOW + str(text) + Fore.RESET


def blue(text):
    return Fore.BLUE + str(text) + Fore.RESET


def cyan(text):
    return Fore.CYAN + str(text) + Fore.RESET


def magenta(text):
    return Fore.MAGENTA + str(text) + Fore.RESET


def white(text):
    return Fore.WHITE + str(text) + Fore.RESET


# Estilos semánticos generales de la aplicación.
def error(text):
    return bold(red(text))


def success(text):
    return bold(green(text))


def warning(text):
    return bold(yellow(text))
