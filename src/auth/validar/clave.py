def validar_clave(clave, confirmacion):
    if len(clave) < 8:
        return "La contraseña debe tener mínimo 8 caracteres."
    if clave != confirmacion:
        return "Las contraseñas no coinciden."
    # bcrypt admite hasta 72 bytes por contraseña.
    if len(clave.encode("utf-8")) > 72:
        return "La contraseña excede el límite de 72 bytes de bcrypt."
    return ""
