'''Faça um programa que calcule a área de um terreno e imprima na tela.
'''
def calcular_area_terreno(comprimento, largura):
     area = comprimento * largura 
     return area 
comprimento = float(input("Digite o comprimento do terreno em metros: ")) 
largura = float(input("Digite a largura do terreno em metros: ")) 
area_terreno = calcular_area_terreno(comprimento, largura)
print(f"A área do terreno é de {area_terreno} metros.") 
