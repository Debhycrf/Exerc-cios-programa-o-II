'''Crie um programa em Python que peça dois números ao usuário. Em
seguida, você vai mostrar a soma, subtração, multiplicação, divisão,
exponenciação e resto da divisão do primeiro número pelo segundo.'''

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2
exponenciacao = num1 ** num2
resto_divisao = num1 % num2
print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")
print(f"Exponenciação: {exponenciacao}")
print(f"Resto da divisão: {resto_divisao}")

