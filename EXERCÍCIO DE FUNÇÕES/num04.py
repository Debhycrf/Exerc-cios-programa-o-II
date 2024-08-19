'''Crie um programa de câmbio. Nesse programa adicione funções que
realizem conversões de real para dólar, real para euro e real para peso
argentino, conforme o nome do país fornecido pelo usuário. Utilize os valores:
1,00 real = 0,18 dólar para Estados Unidos;
1,00 real = 0,16 euro para Portugal;
1,00 real = 0,0061 peso para Argentina;'''

def converter_moeda(valor_reais, pais):
    taxas_de_cambio = {
        "Estados Unidos": 0.18,
        "Portugal": 0.16,
        "Argentina": 0.0061
    }
    if pais in taxas_de_cambio:
        valor_convertido = valor_reais * taxas_de_cambio[pais]
        return valor_convertido
    else:
        return "País não suportado para conversão."
valor_reais = float(input("Digite o valor em reais a ser convertido: "))
pais = input("Digite o nome do país (Estados Unidos, Portugal, Argentina): ")
resultado = converter_moeda(valor_reais, pais)
print(f"O valor convertido é: {resultado}")