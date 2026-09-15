from datetime import date, timedelta


def calcular_sancion(dias_mora, fecha_inicio=None):
    dias_sancion = dias_mora * 2
    if fecha_inicio is None:
        fecha_inicio = date.today()
    fecha_fin = fecha_inicio + timedelta(days=dias_sancion)
    return dias_sancion, fecha_fin
