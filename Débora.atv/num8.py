situacao = input("Você é idoso, gestante, PCD ou nenhum destes? ").strip().lower()
if situacao in ['idoso', 'gestante', 'pcd']:
    print("Você tem acesso à fila de prioridade.")
else:
    print("Você não tem acesso à fila de prioridade.")