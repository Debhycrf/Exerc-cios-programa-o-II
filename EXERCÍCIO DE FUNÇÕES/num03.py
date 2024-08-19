'''Faça um programa que receba três números do usuário, e identifique o maior
através de uma função e o menor número através de outra função.'''

def encontrar_maior_numero(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

def encontrar_menor_numero(num1, num2, num3):
    if num1 <= num2 and num1 <= num3:
        return num1
    elif num2 <= num1 and num2 <= num3:
        return num2
    else:
        return num3

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

maior_numero = encontrar_maior_numero(num1, num2, num3)
menor_numero = encontrar_menor_numero(num1, num2, num3)

print(f"O maior número é: {maior_numero}")
print(f"O menor número é: {menor_numero}")