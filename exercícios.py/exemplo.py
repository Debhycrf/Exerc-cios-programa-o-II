'''Faça um programa para imprimir:
 1
2 2
3 3 3'''
def repeticao(a):
    for i in range(a+1):
     print(str(i) * i) 
repeticao(int(input("Digite um número:"))) 