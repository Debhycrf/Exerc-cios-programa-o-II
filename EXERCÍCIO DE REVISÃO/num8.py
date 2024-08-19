'''Para ter acesso a fila de prioridade, você deve ser idoso, gestante ou PCD.
Escreva um programa que pergunta a situação do usuário (se é idoso, se é
gestante, se é PCD ou nenhum destes) e diga se ele pode ter acesso a fila
prioridade ou não.'''

situacao = input("Você é idoso, gestante, PCD ou nenhum destes? ").strip().lower()
if situacao in ['idoso', 'gestante', 'pcd']:
    print("Você tem acesso à fila de prioridade.")
else:
    print("Você não tem acesso à fila de prioridade.")