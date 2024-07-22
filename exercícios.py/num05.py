'''Escreva um programa que possa cadastrar clientes ou funcionários para uma
loja. Se o usuário quiser cadastrar um cliente, dados de nome, endereço,
CPF devem ser solicitados. Caso o usuário prefira adicionar um novo
funcionário, dados de nome, salário, cargo e CPF devem ser requisitados.
Utilize comandos de manipulação de string para personalizar a saída.'''
def cadastrar_cliente():
    nome = input("Digite o nome do cliente: ")
    endereco = input("Digite o endereço do cliente: ")
    cpf = input("Digite o CPF do cliente: ")
    return f"Cliente cadastrado:\nNome: {nome}\nEndereço: {endereco}\nCPF: {cpf}"
def cadastrar_funcionario():
    nome = input("Digite o nome do funcionário: ")
    salario = input("Digite o salário do funcionário: ")
    cargo = input("Digite o cargo do funcionário: ")
    cpf = input("Digite o CPF do funcionário: ")
    return f"Funcionário cadastrado:\nNome: {nome}\nSalário: R${salario}\nCargo: {cargo}\nCPF: {cpf}"
tipo_cadastro = input("Você quer cadastrar um cliente ou um funcionário? (Digite 'cliente' ou 'funcionário'): ").strip().lower()
if tipo_cadastro == "cliente":
    resultado = cadastrar_cliente()
elif tipo_cadastro == "funcionário":
    resultado = cadastrar_funcionario()
else:
    resultado = "Tipo de cadastro inválido. Por favor, digite 'cliente' ou 'funcionário'."
print(resultado)