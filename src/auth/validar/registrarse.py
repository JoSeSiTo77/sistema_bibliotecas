def validar_registro(nombres, documento, usuarios):
    if not nombres.strip():
        return "Los nombres no pueden estar vacíos."
    if not documento.strip():
        return "El documento no puede estar vacío."
    if documento.strip() in usuarios["documento"].str.strip().values:
        return "Ya existe un usuario con ese documento."
    return ""


def validar_rol(opcion):
    if opcion == "1":
        return "Aprendiz"
    if opcion == "2":
        return "Instructor"
    return ""
