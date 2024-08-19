'''Faça um programa que converta da notação de 24 horas para a notação de 12
horas. Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é
dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer a
conversão e uma para personalizar a saída.'''

def converter_para_12h(hora, minuto):
    if hora == 0:
        hora_12h = 12
        periodo = "AM"
    elif hora < 12:
        hora_12h = hora
        periodo = "AM"
    elif hora == 12:
        hora_12h = 12
        periodo = "PM"
    else:
        hora_12h = hora - 12
        periodo = "PM"
    return hora_12h, minuto, periodo
def personalizar_saida(hora_12h, minuto, periodo):
    return f"{hora_12h}:{minuto:02d} {periodo}"
hora = 14
minuto = 25
hora_12h, minuto, periodo = converter_para_12h(hora, minuto)
saida = personalizar_saida(hora_12h, minuto, periodo)
print(saida) 