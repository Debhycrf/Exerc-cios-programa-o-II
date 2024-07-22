perguntas = [
    "Telefonou para a vítima?",
    "Esteve no local do crime?",
    "Mora perto da vítima?",
    "Devia para a vítima?",
    "Já trabalhou com a vítima?"
]
respostas_positivas = 0
for pergunta in perguntas:
    resposta = input(pergunta + " (S/N): ").strip().upper()
    if resposta == 'S':
        respostas_positivas += 1
if respostas_positivas == 2:
    classificacao = "Suspeita"
elif 3 <= respostas_positivas <= 4:
    classificacao = "Cúmplice"
elif respostas_positivas == 5:
    classificacao = "Assassino"
else:
    classificacao = "Inocente"
print(f"Classificação: {classificacao}")