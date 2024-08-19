'''Crie uma função que receba um número indeterminado de valores inteiros e
depois apresente a soma deles na tela. Use: def nome_da_funcao (* parametro):'''

def soma_inteiros(*numeros):
    soma = sum(numeros)
    print(f"A soma dos números é: {soma}")
soma_inteiros(1, 2, 3, 4, 5) 
