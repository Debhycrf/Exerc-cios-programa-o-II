'''.Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';'''

def valida_nome(nome):
    return len(nome) > 3
def valida_idade(idade):
    return 0 <= idade <= 150
def valida_salario(salario):
    return salario > 0
def valida_sexo(sexo):
    return sexo in ['f', 'm']
def valida_estado_civil(estado_civil):
    return estado_civil in ['s', 'c', 'v', 'd']
while True:
    nome = input("Digite o nome (mais que 3 caracteres): ").strip()
    if valida_nome(nome):
        break
    else:
        print("Nome inválido. Tente novamente.")
while True:
    try:
        idade = int(input("Digite a idade (entre 0 e 150): "))
        if valida_idade(idade):
            break
        else:
            print("Idade inválida. Tente novamente.")
    except ValueError:
        print("Por favor, digite um número válido.")
while True:
    try:
        salario = float(input("Digite o salário (maior que zero): "))
        if valida_salario(salario):
            break
        else:
            print("Salário inválido. Tente novamente.")
    except ValueError:
        print("Por favor, digite um valor numérico válido.")
while True:
    sexo = input("Digite o sexo ('f' para feminino, 'm' para masculino): ").strip().lower()
    if valida_sexo(sexo):
        break
    else:
        print("Sexo inválido. Tente novamente.")
while True:
    estado_civil = input("Digite o estado civil ('s' para solteiro, 'c' para casado, 'v' para viúvo, 'd' para divorciado): ").strip().lower()
    if valida_estado_civil(estado_civil):
        break
    else:
        print("Estado civil inválido. Tente novamente.")

print("Informações válidas cadastradas com sucesso!")