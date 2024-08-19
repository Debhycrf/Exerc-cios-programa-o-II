'''Crie um sistema de conversão brasileiro. Nesse sistema, o usuário acessará
uma interface onde poderá selecionar qual conversão deseja fazer:
Comprimento (centímetro, metro, quilometro), Volume (mililitro, litro) , Massa
(grama, kilograma, tonelada), Temperatura (Celsius, Fahrenheit, Kelvin) ou
Área (centímetro quadrado, metro quadrado, hectare).'''

def converter_comprimento(valor, de_unidade, para_unidade):
    conversao = {
        'centímetro': 1,
        'metro': 100,
        'quilometro': 100000
    }
    return valor * conversao[de_unidade] / conversao[para_unidade]

def converter_volume(valor, de_unidade, para_unidade):
    conversao = {
        'mililitro': 1,
        'litro': 1000
    }
    return valor * conversao[de_unidade] / conversao[para_unidade]

def converter_massa(valor, de_unidade, para_unidade):
    conversao = {
        'grama': 1,
        'kilograma': 1000,
        'tonelada': 1000000
    }
    return valor * conversao[de_unidade] / conversao[para_unidade]

def converter_temperatura(valor, de_unidade, para_unidade):
    if de_unidade == 'Celsius':
        if para_unidade == 'Fahrenheit':
            return (valor * 9/5) + 32
        elif para_unidade == 'Kelvin':
            return valor + 273.15
    elif de_unidade == 'Fahrenheit':
        if para_unidade == 'Celsius':
            return (valor - 32) * 5/9
        elif para_unidade == 'Kelvin':
            return (valor - 32) * 5/9 + 273.15
    elif de_unidade == 'Kelvin':
        if para_unidade == 'Celsius':
            return valor - 273.15
        elif para_unidade == 'Fahrenheit':
            return (valor - 273.15) * 9/5 + 32

def converter_area(valor, de_unidade, para_unidade):
    conversao = {
        'centímetro quadrado': 1,
        'metro quadrado': 10000,
        'hectare': 100000000
    }
    return valor * conversao[de_unidade] / conversao[para_unidade]

def solicitar_unidade(conversao_tipo):
    unidades = {
        'comprimento': ['centímetro', 'metro', 'quilometro'],
        'volume': ['mililitro', 'litro'],
        'massa': ['grama', 'kilograma', 'tonelada'],
        'temperatura': ['Celsius', 'Fahrenheit', 'Kelvin'],
        'área': ['centímetro quadrado', 'metro quadrado', 'hectare']
    }
    print(f"Escolha a unidade de {conversao_tipo}:")
    for i, unidade in enumerate(unidades[conversao_tipo], 1):
        print(f"{i} - {unidade}")
    escolha = int(input("Digite o número correspondente: "))
    return unidades[conversao_tipo][escolha - 1]

def sistema_conversao():
    nome = input("Qual é o seu nome? ")
    print(f"Olá, {nome}! Bem-vindo ao sistema de conversão brasileiro.")
    
    while True:
        print("\nQue tipo de conversão você deseja fazer?")
        print("1 - Comprimento")
        print("2 - Volume")
        print("3 - Massa")
        print("4 - Temperatura")
        print("5 - Área")
        escolha = int(input("Digite o número correspondente: "))
        
        tipos_conversao = ['comprimento', 'volume', 'massa', 'temperatura', 'área']
        conversao_tipo = tipos_conversao[escolha - 1]
        
        de_unidade = solicitar_unidade(conversao_tipo)
        para_unidade = solicitar_unidade(conversao_tipo)
        valor = float(input(f"Digite o valor a ser convertido de {de_unidade} para {para_unidade}: "))
        
        if conversao_tipo == 'comprimento':
            resultado = converter_comprimento(valor, de_unidade, para_unidade)
        elif conversao_tipo == 'volume':
            resultado = converter_volume(valor, de_unidade, para_unidade)
        elif conversao_tipo == 'massa':
            resultado = converter_massa(valor, de_unidade, para_unidade)
        elif conversao_tipo == 'temperatura':
            resultado = converter_temperatura(valor, de_unidade, para_unidade)
        elif conversao_tipo == 'área':
            resultado = converter_area(valor, de_unidade, para_unidade)
        
        print(f"\n{valor} {de_unidade} é igual a {resultado} {para_unidade}.")
        
        nova_conversao = input(f"{nome}, você gostaria de realizar outra conversão? (sim/não): ").strip().lower()
        if nova_conversao != 'sim':
            print(f"Obrigado por usar o sistema de conversão, {nome}! Até logo.")
            break
sistema_conversao() 

