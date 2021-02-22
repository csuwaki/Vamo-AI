numero_dia_semana = 1

def dia_semana(numero_dia_semana):
    if (numero_dia_semana == 1):
        return "domingo"
    elif (numero_dia_semana == 2):
        return "segunda"
    elif (numero_dia_semana == 3):
        return "terça"
    elif (numero_dia_semana == 4):
        return "quarta"
    elif (numero_dia_semana == 5):
        return "quinta"
    elif (numero_dia_semana == 6):
        return "sexta"
    elif (numero_dia_semana == 7):
        return "sábado"
    else:
        return ""

print(dia_semana(numero_dia_semana))