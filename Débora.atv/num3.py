turno = input("Em que turno você estuda? Digite M para Matutino, V para Vespertino ou N para Noturno: ").upper()
if turno == 'M':
    print("Bom Dia!")
elif turno == 'V':
    print("Boa Tarde!")
elif turno == 'N':
    print("Boa Noite!")
else:
    print("Valor Inválido!")

