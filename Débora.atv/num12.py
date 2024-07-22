N = int(input("Digite a quantidade de números: "))
menor_valor = float('inf') 
maior_valor = float('-inf') 
soma = 0
for i in range(N):
    numero = float(input(f"Digite o {i+1}º número: "))
    if numero < menor_valor:
        menor_valor = numero
    if numero > maior_valor:
        maior_valor = numero
    soma += numero
print(f"Menor valor: {menor_valor}")
print(f"Maior valor: {maior_valor}")
print(f"Soma dos valores: {soma}")