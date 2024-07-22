def data_valida(dia, mes, ano):

    if mes < 1 or mes > 12:
        return False
    if mes == 2:
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            if dia < 1 or dia > 29:
                return False
        else:
            if dia < 1 or dia > 28:
                return False
    elif mes in [4, 6, 9, 11]:
        if dia < 1 or dia > 30:
            return False
    else:
        if dia < 1 or dia > 31:
            return False

    return True

data = input("Digite uma data no formato dd/mm/aaaa: ")
dia, mes, ano = map(int, data.split('/'))
if data_valida(dia, mes, ano):
    print("A data é válida.")
else:
    print("A data é inválida.")

