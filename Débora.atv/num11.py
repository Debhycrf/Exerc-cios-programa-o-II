num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
inicio = min(num1, num2)
fim = max(num1, num2)
print(f"Números no intervalo entre {inicio} e {fim}:")
for i in range(inicio, fim + 1):
    print(i, end=" ")
print()  